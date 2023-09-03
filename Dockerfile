FROM python:3

WORKDIR /

COPY entrypoint.sh /entrypoint.sh
COPY envkey.py /envkey.py

RUN pip3 install envkey

ENTRYPOINT ["/entrypoint.sh"]