FROM python:2.7

WORKDIR /app/

RUN python -m easy_install pip

COPY ./requirements.txt .
RUN python -m pip install -r ./requirements.txt

COPY . .

ENV CONTACTS_DIRECTORY=/contacts

ENTRYPOINT ["python"]
CMD ["run.py"]
