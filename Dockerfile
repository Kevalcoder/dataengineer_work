FROM python:3.9-alpine

COPY problem1.py problem2.py problem3.py problem4.py /app/


RUN pip install -r requirements.txt


WORKDIR /app

CMD ["python", "problem1.py"]
CMD ["python", "problem2.py"]
CMD ["python", "problem3.py"]
CMD ["python", "problem4.py"]
