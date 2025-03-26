FROM python:3.9-slim

RUN groupadd -r myuser && useradd -r -g myuser myuser

COPY ipc_namespace.py /ipc_namespace.py

RUN chown myuser:myuser /ipc_namespace.py

USER myuser

CMD ["python", "/ipc_namespace.py"]
