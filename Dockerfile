FROM amancevice/superset:6.1.0

USER root

COPY requirements-local.txt /tmp/requirements-local.txt

RUN pip install --no-cache-dir \
    -r /tmp/requirements-local.txt

USER superset
