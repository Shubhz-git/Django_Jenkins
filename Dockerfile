FROM python:3
RUN pip install django==2.1.15

COPY . . 

RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver","8000"]
