FROM python:2.7

COPY . /app

ENV CONTACTS_DIRECTORY=/contacts
# ENV SLACKBOT_API_TOKEN=<override when running container>

ENTRYPOINT cd /app && \
           python -m easy_install pip && \
           python -m pip install -r requirements.txt && \
           python run.py

