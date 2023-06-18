FROM python:3

WORKDIR /bank_api/backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

WORKDIR /bank_api/backend/src
CMD ["python", "server.py"]

EXPOSE 8000
