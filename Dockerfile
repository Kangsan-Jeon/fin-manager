FROM python:3.8

WORKDIR /code/
COPY . /code/
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0:8000"]

EXPOSE 8000