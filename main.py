import tweepy
import time
import schedule

#storing my authentication keys as variables
api_key = "OAnGbodODWCBG2VTGQXpIdr4g"
api_secret = "sqohsh5fs4pQb2VpBaBiJALcRbWHEb4Lklbv2JIhSQWaZj99xq"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAAgHoAEAAAAA%2F0fHkIXvaZpZRt4EtgVWAElg5aw%3D9WIRNq5sTcE7SW3hY2pPmJXhT3wW3cEpxObPMjgGbQvArc1ial"
access_token =  "1666054722246045697-N6I2GBLbSd5ZxoSZGz5R53F03JGo0X"
access_token_secret = "pYXhdgG5fZnAjaLbcKsuSzYva6HV7NNn79JyXgaocptf6"

#authenticating to twitter using those variables
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#total number of tweets
numberOfTweets = 1

#posts a tweet at 11:11 everyday and saves how many total tweets
def synchronicity():
    global numberOfTweets
    client.create_tweet(text="It's 11:30!")   
    numberOfTweets = numberOfTweets+1

#posts a tweet every hour and saves how many total tweets
def everyHour():
    global numberOfTweets
    client.create_tweet(text="This is tweet #" + str(numberOfTweets))
    numberOfTweets = numberOfTweets+1

# at 11:11 post tweet
schedule.every().day.at("11:30").do(synchronicity)

# every hour post tweet 
schedule.every().hour.do(everyHour)


#keeps scheduling tasks constantly running
while True:
    #checks whether a scheduled task is pending to run or not
    schedule.run_pending()
    time.sleep(1)