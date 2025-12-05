FROM python:3.11-slim
WORKDIR /app
# Copy service requirements (located at service root)
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy application sources
COPY src/ ./src
# Run the Flask app
CMD ["python", "src/app.py"]
