from docker pull python:trixie
COPY ./main.py ~/main.py
RUN python ~/main.py
