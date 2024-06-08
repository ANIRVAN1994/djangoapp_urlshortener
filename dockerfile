FROM python:3-alpine3.12
WORKDIR /urlshortproject
COPY . /urlshortproject
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python manage.py runserver