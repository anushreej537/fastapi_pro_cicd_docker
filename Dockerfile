FROM python:3.10-slim

WORKDIR /code

# Copy requirements from root to container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from local root to container /code
COPY . .

# Run uvicorn pointing to the app folder
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]