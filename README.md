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
1. Create service in Bluemix: https://console.bluemix.net/catalog/services/conversation
2. Launch the service
3. Create a new workspace
4. Create intents, entities, and dialog
5. Test out conversation in browser
6. Copy service credentials

### Clone project and update for Slack bot
1. Git clone this sample project

`git clone git@github.com:kostickm/watsonbot.git`

2. Copy the `env.sample` file to `.env`
3. Update slack credentials
4. Update Watson Conversation credentials
5. *Optional: Run locally to test*

### Deploy to Bluemix
1. Log into Bluemix/CF CLI

  `bluemix api https://api.ng.bluemix.net`
  
  `bluemix login`
  
2. Push app to Bluemix

  `bluemix app push <app_name>`

### Chat with Watson
1. Check that app is running in Bluemix
2. Test out deployed app in Slack

## Next Steps
* Check out [Watson Python SDK](https://github.com/watson-developer-cloud/python-sdk/tree/master/examples) examples
* Add in Watson Language Translation
* Add in Watson Tone Analyzer
* Incorporate an API
* Have Watson tell some jokes
