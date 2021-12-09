FROM python

RUN pip install --upgrade cython && \
  pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

CMD ["python3", "run.py"]