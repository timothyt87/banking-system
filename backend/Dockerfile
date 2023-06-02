FROM python:3

WORKDIR /bank_api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./
CMD ["uvicorn", "server:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000