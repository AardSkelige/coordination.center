FROM python:3
WORKDIR /coordination_centre
RUN pip install --upgrade pip
COPY requirements.txt /coordination_centre

RUN pip install -r /coordination_centre/requirements.txt
COPY . /coordination_centre

EXPOSE 8000

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
