# watsonbot
Watson Conversation Slack Bot

## Prerequistes
### Slack
* [Slack](https://slack.com)
* [Slack API](https://api.slack.com/) - Create a bot

### Bluemix
* [Bluemix Account](https://console.bluemix.net/)
* [Bluemix CLI](https://clis.ng.bluemix.net/ui/home.html)

### Python
* [Python 2.7.x](https://www.python.org/downloads/)
* slackclient: `pip install slackclient`

### Git
* [Github Account](https://github.com)
* [Git](https://git-scm.com/downloads)

## Steps
### Set up the Watson Conversation Service
1. See the [instructions](conversation/README.md) for setting up and configuring your [Watson Conversation Service](https://console.bluemix.net/catalog/services/conversation).

### Clone project and update for Slack bot
1. Git clone this sample project

`$    git clone git@github.com:kostickm/watsonbot.git`

2. Change to your the newly cloned repo

`$    cd watsonbot/`

3. Copy the `env.sample` file to a new file named `.env`

`$    cp env.sample .env`

4. Open and update the `.env`. file with your Slack credentials

`$    vi .env`

```
# Slack
SLACK_BOT_TOKEN=<add_slack_bot_token>
SLACK_BOT_ID=<add_slack_bot_id>
```

5. Open and update the `.env`. file with your Watson Conversation credentials

```
# Watson conversation
CONVERSATION_USERNAME=<add_conversation_username>
CONVERSATION_PASSWORD=<add_conversation_password>
WORKSPACE_ID=<add_conversation_workspace>
```

6. *Optional: Run locally to test*

`$    python watsonbot.py`

Chat with your `watsonbot` by sending a Slack message starting with `@watsonbot`.

### Deploy to Bluemix
You are now ready to deploy your application to Bluemix.

1. Log into Bluemix CLI using your Bluemix credentials

  `$    bluemix api https://api.ng.bluemix.net`

  `$    bluemix login`

2. Push app to Bluemix

  `$    bluemix app push watsonbot`

### Chat with Watson
1. Check that app is running in Bluemix

<Insert Photo>

2. Test out your deployed app in Slack. Chat with your `watsonbot` by sending a Slack message starting with `@watsonbot`.

## Next Steps
* Check out the other Watson Python SDK [examples](https://github.com/watson-developer-cloud/python-sdk/tree/master/examples)
* Add in the Watson Language Translation service
* Add in the Watson Tone Analyzer service
* Incorporate an API (Weather, Calendar, Github, etc.)
* Have Watson tell a joke
