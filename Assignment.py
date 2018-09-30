import tweepy
import time

ACCESS_TOKEN = '701354914526531584-CPFbtrNzJ61VmMqG0COy8uJGAwgTOwM'
ACCESS_SECRET = 'conAKsJVyjpOhS79IjUrmTq4DQOIJ8U4QtdL0GHYjzkf2'
CONSUMER_KEY = 'dh3JNULEFUP8kUM6CwUmpt6bK'
CONSUMER_SECRET = '9qPNB5ZsFiMHT8BSLkdi3MZ5ucWJWsyZ87Cvya16M2pz0ZnGpW'
SEARCH=input("Enter the search string ")
FROM=input("Enter the from date (YYYY-MM-DD format) ")
TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

i=0;


f = open(INPUT_FILE_PATH,'w',encoding='utf-8')

for res in tweepy.Cursor(api.search, q = SEARCH, rpp=100, count=100, result_type="recent", since = FROM,until =TO, include_entities=True, lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write(' ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')	
	f.write(" ")
	f.write('"')
	f.write(res.text.replace('\n',''))
	f.write('"')
	f.write(" ")
	f.write(str(res.user.followers_count))
	f.write(" ")
	f.write(str(res.retweet_count))
	f.write('\n')
f.close
print("Tweets retrieved ",i)


