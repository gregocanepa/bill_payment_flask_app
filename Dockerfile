FROM python

RUN pip install --upgrade cython && \
  pip install --upgrade pip

WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt

CMD ["flask", "db init"]
CMD ["flask", "db migrate"]
CMD ["flask", "db upgrade"]
CMD ["python3", "run.py"]