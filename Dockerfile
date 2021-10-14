FROM python:3.8-slim-buster

WORKDIR /opt/code/
COPY . /opt/code/
RUN pip install --upgrade pip \
    -r requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]

EXPOSE 8000