Our goals are to grasp the global view of how DialogFlow works and, more precisely, how it integrates with a webhook.
We will finally create a python webhook responsible for turning on or off lights.




What is DialogFlow ?

DialogFlow is a tool that does NLP and can be used to detect keywords and intents in a user’s sentence. Its role is to help building chatbots using Machine Learning. All you need to do is provide a set of training phrases a user could potentially say, highlight the parameters you want to retrieve and let DialogFlow train itself.


Integrations
As stated earlier, DialogFlow supports a wide range of integrations, it knows how to communicate with various services such as Facebook Messenger, Actions on Google, Skype, etc. which means your agent will work with every one of these platforms if you set up the integrations properly.

Webhook for DialogFlow
Every time DialogFlow matches an intent, you have the possibility to ask DialogFlow to send a request to a specific endpoint. An endpoint which you’ll obviously have to code.
That will allow you to retrieve the matched intent, as well as the matched parameters and contexts, and do some useful work with those.


Creating an agent
Getting started
Agent
There are loads of tutorials on the internet on how to get started with DialogFlow. So follow one of them and create a new agent. Remember to activate the v2 API before creating the agent !


Intents
First we’ll need at least one intent. An intent represents what the user is trying to do. When DialogFlow receives what the user just said or wrote, it will try to detect the user’s intent–what he’s trying to achieve. 



Here’s an example of how it would work :

The phrase the user said on the right section of the screenshot isn’t defined in our training phrases. Yet, DialogFlow knows it’s the Search intent and knows that mojito refers to a cocktail name.




Webhook : Introduction

So you’ve started to work on DialogFlow. Your agent is behaving correctly, and now you want to create a webhook to add some logic behind it. 
But after all, you just want to wrap a small piece of the DialogFlow API which is : Receiving a JSON payload and responding with another JSON payload. So you start writing your own package and end up in the WebhookRequest section of the documentation. 


To test and develop your webhook, I’d recommend you use ngrok. Your server will be listening on 127.0.0.1:8001 so simply execute the following command to start ngrok :
$ ngrok http 8001

Then check the Forwarding line, copy the URL that ngrok gave you, and go to the Fulfillment section of your DialogFlow agent. Paste the URL and save. Then head to the intent you want to activate your webhook for, and check the box to enable the webhook call :

Remember to save, and wait for the agent to finish training. Modify your webhook so you can parse what DialogFlow sends you.
Incoming Request

When DialogFlow detects an intent it will send a complex JSON object to your webhook. And there’s only one webhook for all the intents. So we’re going to filter and route on what is called the action.

You can either set this to the value you want or simply let DialogFlow generate the action’s name for you.


We’re now able to receive the request DialogFlow sends to our webhook, thus we can route on the action field. This will allow us to receive different parameters and contexts depending on which intent matched.

We have two different behaviors here. The Random intent doesn’t send parameters whereas the Search one sends the various parameters we defined in our intent. Let’s add two functions :
