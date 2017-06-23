#!/usr/bin/env python
from dotenv import load_dotenv
from slackclient import SlackClient
from watson_developer_cloud import ConversationV1

import os
import time
import datetime
import logging
logging.basicConfig()

# Load your env file
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Your bot's ID as an environment variable
BOT_ID = os.environ.get('SLACK_BOT_ID')

# Constants
AT_BOT = "<@" + BOT_ID + ">"

# Instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

# Instantiate workspace and credentials for Watson Conversation service
WORKSPACE_ID = os.environ.get('WORKSPACE_ID')
USERNAME = os.environ.get('CONVERSATION_USERNAME')
PASSWORD = os.environ.get('CONVERSATION_PASSWORD')

conversation = ConversationV1(
    username=USERNAME,
    password=PASSWORD,
    version='2017-04-21')


def handle_command(command, channel, user):
    """
        Receives commands directed at the bot and determines if they
        are valid commands.
        If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean."

    # Get response from Watson Conversation
    responseFromWatson = conversation.message(
        workspace_id=WORKSPACE_ID,
        message_input={'text': command}
    )

    # Get intent of the query
    intent = responseFromWatson['intents'][0]['intent']

    # Render response on Bot
    response = responseFromWatson['output']['text'][0]

    slack_client.api_call("chat.postMessage", as_user=True, channel=channel, text=response)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        This parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # Return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip(), \
                       output['channel'], output['user']
    return None, None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("watsonbot connected and running!")
        while True:
            command, channel, user = parse_slack_output(slack_client.rtm_read())
            if command and channel and user:
                handle_command(command, channel, user)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
