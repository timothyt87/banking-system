FROM python:3

WORKDIR /bank_api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./
CMD ["python", "server.py"]

EXPOSE 8000