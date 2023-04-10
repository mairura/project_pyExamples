import twint
import telegram

bot_token = "6103569551:AAGqjOG8mlI8m-YgrRvWZ6rAN7xQfQJeC9s"
chat_id = "288307809"

# Configure Twint
c = twint.Config()
c.Search = 'hack'
c.Limit = 10
c.Store_object = True

# Run Twint
twint.run.Search(c)

# Get the tweets
tweets = twint.output.tweets_list

# Send a message to your Telegram group/channel for each tweet
bot = telegram.Bot(token=bot_token)
for tweet in tweets:
    message = f"New tweet found:\n\n{tweet.username}: {tweet.tweet}"
    bot.send_message(chat_id=chat_id, text=message)
