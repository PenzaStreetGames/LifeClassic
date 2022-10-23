FROM python:3.10.5-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add tk

ENV PYTHONUNBUFFERED=1
ENV DISPLAY=$DISPLAY

COPY . .

CMD [ "python", "main.py" ]