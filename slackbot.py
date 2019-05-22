
from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os
import urllib.request
import pandas as pd
    

slack_signing_secret = os.environ["SLACK_SIGNING_SECRET"]
slack_events_adapter = SlackEventAdapter(slack_signing_secret, "/slack/events")

    # Create a SlackClient for your bot to use for Web API requests
slack_bot_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = SlackClient(slack_bot_token)

    # Our app's Slack Event Adapter for receiving actions via the Events API

# Example responder to greetings
@slack_events_adapter.on("message")
def handle_message(event_data):
    jtown = pd.read_html('https://apis.opendatani.gov.uk/translink/rendercis.asp?file=3044C2.xml',header=0,)

    stuff = jtown[0].values.tolist()

    try:
     train1 = stuff[0]
    except IndexError:
     train1 = ''

    try:
     train2 = stuff[2]
    except IndexError:
     train2 = ''

    try:
     train3 = stuff[4]
    except IndexError:
     train3 = ''

    bfstrain = 0
    whtrain = 0
    belfast = "next train belfast"
    whitehead = "next train whitehead"
    message = event_data["event"]

    for x in stuff[0][1]:
     x
    # If the incoming message contains "hi", then respond with a "Hello" message
     if message.get("subtype") is None and whitehead in message.get('text') and stuff[0][1] == "Whitehead":
       whtrain = 1
     if whtrain == 1:
       channel = message["channel"]
       test = "The next train from Jordanstown is the", stuff[0][0], "Train to", stuff[0][1], "on platform", stuff[0][2]
       message = ' '.join(map(str, test))
       slack_client.api_call("chat.postMessage", channel=channel, text=message)
       break
     if message.get("subtype") is None and belfast in message.get('text') and stuff[2][1] == "Great Victoria St":
       bfstrain = 1
     if bfstrain == 1:
       channel = message["channel"]
       test = "The next train from Jordanstown is the", stuff[2][0], "Train to", stuff[2][1], "on platform", stuff[2][2]
       message = ' '.join(map(str, test))
       slack_client.api_call("chat.postMessage", channel=channel, text=message)
       break
    else: print("test")



# Example reaction emoji echo
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    channel = event["item"]["channel"]
    text = ":%s:" % emoji
    slack_client.api_call("chat.postMessage", channel=channel, text=text)

# Error events
@slack_events_adapter.on("error")
def error_handler(err):
    print("ERROR: " + str(err))

# Once we have our event listeners configured, we can start the
# Flask server with the default `/events` endpoint on port 3000
slack_events_adapter.start(port=3000)
