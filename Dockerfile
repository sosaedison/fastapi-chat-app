FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./chatapp /code/chatapp

CMD ["uvicorn", "chatapp.main:app", "--host", "0.0.0.0", "--port", "80"]