import os
import slackclient

BOT_SLACK_NAME = os.environ.get('BOT_SLACK_NAME')
BOT_SLACK_TOKEN = os.environ.get('BOT_SLACK_TOKEN')
# initialize slack client
bot_slack_client = slackclient.SlackClient(BOT_SLACK_TOKEN)
# check if everything is working alright
print(BOT_SLACK_NAME)
print(BOT_SLACK_TOKEN)
is_ok = bot_slack_client.api_call("users.list").get('ok')
print(is_ok)
# find the id of our slack bot
if(is_ok):
    for user in bot_slack_client.api_call("users.list").get('members'):
        if user.get('name') == BOT_SLACK_NAME:
            print(user.get('id'))