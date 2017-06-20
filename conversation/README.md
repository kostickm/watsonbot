# Watson Conversation Service

An example of setting up the Watson Conversation service for use in a chat bot. Feel free to change the content of your chat bot and be creative!

### Set up the Watson Conversation Service
1. Create an instance of the [Watson Conversation Service](https://console.bluemix.net/catalog/services/conversation) in Bluemix.

  * Give the service a unique name and click **Create**.

  <img src="media/ConversationCreate.png" width="700">

2. Once your new Conversation Service is created, click **Launch tool** to start working with your Conversation Service.

  <img src="media/ConversationLaunch.png" width="500">

3. Click **Create** to create a new Workspace.

  <img src="media/ConversationWorkspace.png">

  * Give the new Workspace a name and description. Click **Create**.

  <img src="media/ConversationWorkspaceCreate.png">

  * Once the workspace is created, you will see three tabs labeled: **Intents**, **Entities**, and **Dialog**.

4. From the Intents tab, click **Create new**.

  <img src="media/ConversationIntents.png" width="700">

  * Intents define the various types of user input to expect.

  * Start by creating a **greetings** Intent. Add typical greetings similar to the ones listed below.

  <img src="media/ConversationIntentGreetings.png">

  * Create a **complaint** Intent.

  <img src="media/ConversationIntentComplaint.png">

  * Create a **return** Intent

  <img src="media/ConversationIntentReturn.png">

  * Finish up your Intents by adding a **goodbyes** and **anything_else** Intent.

  <img src="media/ConversationIntentsComplete.png" width="700">

  * The goal of the **anything_else** Intent is to catch random user input that is unexpected.

5. From the Entities tab, click **Create new**.

  <img src="media/ConversationEntities.png" width="700">

  * Entities further break down specific pieces of an Intent, allowing your bot to respond to each particular case.

  * Name your Entity **returnItems**, and add various various values and synonyms to your Entity.

  <img src="media/ConversationReturnItems.png" width="700">

6. From the Dialog tab, click **Create**.

  <img src="media/ConversationDialog.png" width="700">

  * The Dialog connects the Intents and Entities into a conversation based on user input and your bot's responses.

  * Start with creating the **Welcome** card. The trigger is **#greetings**, and enter a response for Watson.

  <img src="media/ConversationGreetingExpanded.png" width="700">

  * Your **Welcome** card will now appear as follows.

  <img src="media/ConversationDialogWelcome.png">

  * Below the **Welcome** card, click the plus sign and create a **Complaint** card. The trigger is **#complaint**, and enter a response for Watson.

  * Below the **Compaint** card, click the plus sign and create a **Return** card. The trigger is **#return**, and in this case Watson will respond conditionally based on the Entities created. You specific the Entity condition as **@<entity_name>:<specific_entity_value>**.

  <img src="media/ConversationDialogReturnDetails.png" width="700">

  * Your **Return** card will now appear as follows.

  <img src="media/ConversationDialogReturn.png">

  * Finish up your Dialog by adding a **Goodbye** card and an **Anything else** card.

  <img src="media/ConversationDialogComplete.png">

7. You can test out your Dialog in the browser by chatting with Watson.

  * Click the chat bubble located in the top right corner of your Watson Conversation workspace.

  <img src="media/ConversationWatsonChatBubble.png">

  * Try chatting with Watson and see how your Dialog flows.

  <img src="media/ConversationWatsonChat.png">

8. For the next part of this demo you will need to copy some service credentials.

  * Click the **Back to workspaces** button from the left-side menu.

  <img src="media/ConversationWorkspaces.png">

  * Click the drop down menu on your Workspace and click **View details**.

  <img src="media/ConversationViewDetails.png">

  * Copy the **Workspace ID** for future use.

  <img src="media/ConversationWorkspaceID.png">

  * Return to your Bluemix Dashboard and click on your Conversation service.

  * From the left-side menu, click **Service Credentials**.

  * Expand the **View credentials** twisty and copy the `username` and `password`.

  <img src="media/ConversationCredentials.png">
