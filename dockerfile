FROM python:3.11-slim

WORKDIR /app

# Copy requirements và cài dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code
COPY app/ .

EXPOSE 8080

CMD ["python", "app.py"]