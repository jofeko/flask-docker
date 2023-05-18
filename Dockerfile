FROM python:3.8-alpine

EXPOSE 5000/tcp

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

CMD ["python", "main.py"]
