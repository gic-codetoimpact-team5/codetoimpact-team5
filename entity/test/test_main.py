import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))

import pandas as pd

from fastapi.testclient import TestClient
from analytics.src.main import app
from analytics.src.routers.etf import get_db
from common.testing_database import DatabaseTest

'''
- Test should be run in the test directory
- Function that starts with test_ will be run by pytest
- Testing functions should not be async
'''

client = TestClient(app)
testDatabase = DatabaseTest()
app.dependency_overrides[get_db] = testDatabase.override_get_db

# Add sample data to test database
df = pd.read_csv('testingData.csv')
testDatabase.add_to_test_database(df, 'daily')


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_etf():
    response = client.get("/etf")
    etf_symbols = response.json()["etf_symbols"]
    assert len(etf_symbols) == 1
    assert etf_symbols[0] == 'AAA'
    assert response.status_code == 200