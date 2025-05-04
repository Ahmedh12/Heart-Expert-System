FROM python:3.8

RUN apt-get update && apt-get install -y \
    vim \
    curl \
    net-tools \
    iputils-ping \
    procps \
    tk-dev \
    libtcl8.6 \
    libtk8.6 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["tail", "-f", "/dev/null"]