FROM python:3.10-alpine as build

WORKDIR /opt/

COPY dependencies/requirements.txt /tmp/

RUN apk update && \
    apk add build-base && \
    apk add python3-dev && \
    apk add gcc && \
    apk add libffi-dev && \
    apk add cargo && \
    apk add musl-dev && \
    apk add openssl-dev

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN python -m venv .venv && \
    .venv/bin/python -m pip install --upgrade pip && \
    .venv/bin/pip install -U setuptools wheel && \
    .venv/bin/pip install -r /tmp/requirements.txt && \
    .venv/bin/pip cache purge

FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

COPY src src/
COPY --from=build /opt/.venv /src/.venv

ENV PYTHONPATH="/"
ENV PATH="/src/.venv/bin:$PATH"


WORKDIR /src

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /src

USER appuser

CMD ["python", "main.py"]