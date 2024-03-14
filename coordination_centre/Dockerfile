FROM python:3
WORKDIR /coordination_centre
RUN pip install --upgrade pip
COPY requirements.txt /coordination_centre

RUN pip install -r /coordination_centre/requirements.txt
COPY . /coordination_centre

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]