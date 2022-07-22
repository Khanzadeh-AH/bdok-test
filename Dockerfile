FROM python:3.9.13-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade -r /code/requirements.txt
COPY ./ /code
ENV MONGO_HOST="127.0.0.1"
ENV MONGO_PORT="27017"
ENV MONGO_USERNAME="mongodb"
ENV MONGO_PASSWORD="mongodb"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]