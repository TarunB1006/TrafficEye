
FROM python:3.9-slim

WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6




COPY app.py app.py
COPY deep_sort_realtime/ deep_sort_realtime/
COPY best.pt best.pt

CMD ["python", "app.py"]
