FROM python:3.6-slim

RUN apt-get update \
    && apt-get -y --no-install-recommends install \
        build-essential \
        curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /var/app

ADD . /var/app

RUN make build

EXPOSE 80

CMD ["python", "app.py"]