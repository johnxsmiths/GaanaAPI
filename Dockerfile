FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "[IP_ADDRESS]", "--port", "8000", "--reload"]