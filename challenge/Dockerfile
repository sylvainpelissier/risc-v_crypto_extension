FROM python:3-slim
LABEL Description="Acceleration" VERSION='0.1'

RUN apt-get update && apt-get install -y xinetd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m user && chown -R root:root /home/user

COPY aes_encrypt.py /home/user

COPY xinetd /etc/xinetd.d/user

WORKDIR /home/user

EXPOSE 128

CMD ["/usr/sbin/xinetd", "-dontfork"]
