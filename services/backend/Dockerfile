FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./psmaa /code/psmaa
COPY ./models /code/models
COPY ./utils /code/utils
COPY ./main.py /code/

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
