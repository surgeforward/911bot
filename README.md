911bot is a chatbot specifically meant to be helpful for remote workers in an
emergency. When you are remote and something happens to you and your teammates
are aware, they might have trouble getting you the help you need. So we created
an emergency contact info bot in memory of
[Simon Hancock](http://rochestercremation.com/obituary/joseph-simon-hancock)

The goals are as follows

-   Provide information on how to contact a Surgeon's local emergency services
    and contact person
-   Be as respectful of maintaining the secrecy of personal information as
    possible

By default 911bot integrates with Slack and provides a chat interface for storing emergency contact information and retrieving information on someone. Users are actively discouraged by the bot from retrieving information for any non-emergency purposes and any access is logged and notified. All contact information is accessible only to the system administrator.

# Usage

To interact with the bot send a direct message to `@911bot` with the text
`help`. You can then interact with it via the `store-contact` command.

When storing your info you might consider how someone who saw you collapse on a
call for example might go about getting you help. So for example you might type

    @911bot> store-contact First try my wife Laura at xxx-xxx-xxxx or my brother at xxx-xxx-xxxx.
             The local 911 service number is xxx-xxx-xxxx, I usually work from either home (123
             First St Apt 2, New Orleans) or the local co-working space (555 Main St, New Orleans).
             My cell phone number is xxx-xxx-xxxx.

This information will be stored by \`@911bot\`. You can access a user's
information by messaging the bot with the `emergency @username` command which
will walk you through a short prompt confirming that this is indeed a legitimate
emergency. In order to encourage using this only for true emergencies **all
access of emergency information will be recorded and the user will be notified
when and by whom their information is requested.**

You can check your currently stored info by typing `store-contact` by itself and
check who has accessed your info with `list-access`.


# Running 911Bot

Default storage method is DiskStorage, which requires write access to the current where 
the bot is run. See below to use alternate (S3 storage is available).

1.  Create a new bot under
    ["Custom Integrations"](https://surgellc.slack.com/apps/manage/custom-integrations)
2.  Set the environment variable `SLACKBOT_API_TOKEN` to the API token
3.  Install requirements: `python -m pip install -r requirements.txt`
4.  Start: `python run.py`


# Running a health check:

1.  From your team's admin page, create a test user. (One way is to send an
    invitation to your own email account.)
2.  Give the user a test token under
    ["Test Token Generator"](https://api.slack.com/docs/oauth-test-tokens).
3.  define `HEALTHCHECK_SLACK_TOKEN` with the value of the test token you just
    generated.
4.  run `python run_healthcheck.py` - This process will return 0 if check
    succeeded

# Storage Methods

If `BOT911_STORAGE_METHOD` environment variable is not set, default is `DiskStorage`, set in
`./bot/storage/__init__.py`. Alternate value is `S3Storage` for using AWS S3.

## DiskStorage

### Environment Variables:
    BOT911_STORAGE_METHOD=DiskStorage
    CONTACT_DIRECTORY: directory to store `<userId>.json` files.
                       default: 'contacts'

## S3Storage

NOTE: 991bot will not create the bucket, so create the bucket, a user if need be, and obtain
an AWS Access Key and Secret. Set the following environment variables.

### Environment Variables:
        BOT911_STORAGE_METHOD=S3Storage
        AWS_ACCESS_KEY_ID:      key used directly by boto3
        AWS_SECRET_ACCESS_KEY:  secret used directly by boto3 
        BOT911_S3_BUCKET:       name of a PRE-EXISTING bucket for `<userId>.json` blobs
        

## Custom

911bot supports storage of the contact either on disk or in S3. To create other storage
targets or methods see the `./bot/storage` directory. 

1. Create particular storage class in `./bot/storage/`. It should descend from 
   the Storage class in `./bot/storage/storage.py`. 
1. A new storage class can be created by implementing `_getRecord(..)`, 
   `_storeRecord(..)`, and, if needed, `initialize(..)`. See `./bot/storage/diskstorage.py` 
   as an example. 
1. Add the class to `storageTypes` in `./bot/storage/__init__.py`.
1. The `BOT911_STORAGE_METHOD` env variable cooresponds to the key in the `storageTypes`
   object.

# Testing

To set up a personal testing environment, create a new slack team with a user
and a bot: the former for the health check, the latter for the 911bot.

# Deployment with Docker

    docker build -t 911bot .
    docker volume create --name contacts # or however you want to do it
    
## DiskStorage
    
    docker run -d --name 911bot \
        -e SLACKBOT_API_TOKEN=<API TOKEN> \
        -e BOT911_STORAGE_METHOD="DiskStorage" \
        -v contacts:/contacts 911bot

## S3Storage

    docker run -d --name 911bot \
        -e SLACKBOT_API_TOKEN=<API TOKEN> \
        -e AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY>\
        -e AWS_SECRET_ACCESS_KEY=<AWS_SECRET> \
        -e BOT911_S3_BUCKET=<S3 BUCKET NAME> \
        -e BOT911_STORAGE_METHOD="S3Storage" \
        911bot

# Contributing

See [docs/contributing.md](docs/contributing.md)

# Design

See [design document](docs/design/design.org).

