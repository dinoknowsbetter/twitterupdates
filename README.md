# twitterupdates
Discord webhook bot that checks for new tweets on your profile and send them to a specific channel on discord as an update.


#How to set up and use:
First of all we need to set up the twitter part, go to https://developer.twitter.com/ and sign up for an account, once you do that, create an app and grab the API (consumer_key), API Secret (consumer_secret), Access token (access_token) and Access Token Secret (access_token_secret)

Once you have that ready, insert them into corespnding variables in the file.

Now move on to discord, click on edit channel for the channel you want the announcements to be in, then integrations, webhooks and new. Once you set it up, copy the URL and use the following template to get the Webhook ID and token

https://discordapp.com/api/webhooks/ WEBHOOK_ID / WEBHOOK_TOKEN

Now insert those into coresponding variables in the file.

Change the username variable

Once you're done, you can tweak the message it sends, and the name of the bot you're using to send it and that's it!

