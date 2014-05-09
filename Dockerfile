FROM orchardup/python:2.7

ADD requirements.txt /code/requirements.txt
RUN cd /code; pip install -r requirements.txt

ADD . /code

EXPOSE 5000
CMD ["python", "/src/main.py"]
