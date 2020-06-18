#First step is to get developer permission from Twitter in order to generate API keys
import tweepy

#Put Twitter API keys below
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Put each user you want to pull the most recent tweet from in the user_name list in the format '@UserName'
user_name = ['']
tweetList = []

#GET TEXT AND APPEND TO LIST
def getTweet (user_name):
    for users in user_name:
        user = api.get_user(users)
        tweetInfo = user._json.get('status')
        tweetText = tweetInfo.get('text')
        tweetList.append(tweetText)

#ADD IN TAGS TO A STATUS, put the tags you want added to the tweet in the quotation marks on line 29
def postStatus (tweetList):
    for tweets in tweetList:
        addAt = tweets + ' '
        api.update_status(addAt)

getTweet(user_name)
postStatus(tweetList)
