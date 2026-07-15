from docker pull python:trixie
COPY ./main.py ~/main.py
RUN pip install fastmcp
CMD [python][~/main.py]
