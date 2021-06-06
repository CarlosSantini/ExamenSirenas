FROM python:3.8.10

ADD main.py .

RUN pip install pandas matplotlib sklearn

CMD ["python", "./main.py"]