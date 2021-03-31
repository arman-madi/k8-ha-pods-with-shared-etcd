FROM python:3-slim-buster

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
CMD ["python", "/app/main.py"]