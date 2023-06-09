import tweepy
from datetime import datetime

api_key = "OAnGbodODWCBG2VTGQXpIdr4g"
api_secret = "sqohsh5fs4pQb2VpBaBiJALcRbWHEb4Lklbv2JIhSQWaZj99xq"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAAgHoAEAAAAA%2F0fHkIXvaZpZRt4EtgVWAElg5aw%3D9WIRNq5sTcE7SW3hY2pPmJXhT3wW3cEpxObPMjgGbQvArc1ial"
access_token =  "1666054722246045697-N6I2GBLbSd5ZxoSZGz5R53F03JGo0X"
access_token_secret = "pYXhdgG5fZnAjaLbcKsuSzYva6HV7NNn79JyXgaocptf6"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.like(1088288799342448641)