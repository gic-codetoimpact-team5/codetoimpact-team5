FROM python:3.9

WORKDIR /code/app

# Copy requirements.txt for the specific project
COPY ingestor/requirements.txt /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the "common" folder
COPY common /code/common

# Copy the specific project code
COPY ingestor /code/app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
