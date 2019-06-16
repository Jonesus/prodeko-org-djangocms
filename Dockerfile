FROM python:3

ENV PYTHONUNBUFFERED 1

# Install Python and Package Libraries
RUN apt-get update && \
      apt-get install -y mysql-client gettext

RUN apt-get update && apt-get install -y dos2unix

WORKDIR /code

COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements-dev.txt

COPY . /code/
COPY docker-entrypoint.sh /usr/local/bin/
RUN dos2unix /usr/local/bin/docker-entrypoint.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]