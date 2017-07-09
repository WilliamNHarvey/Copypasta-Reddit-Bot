#* * * * * cd ~/python/CummyBot20000/src; python cummy_bot_20000.py

import praw
import datetime
from time import sleep

def login():
    reddit = praw.Reddit('cummy_bot_20000')
    return reddit

def run(r):
    copypasta = r.subreddit("copypasta")
    localSub = r.subreddit("redditscripttemplate")

    #Checks the top 5 posts in the "new" category in the subreddit
    num_posts_to_check = 5

    for submission in localSub.new(limit=num_posts_to_check):
        time_now = datetime.datetime.utcnow()
        submission_time = datetime.datetime.utcfromtimestamp(submission.created_utc)
        time_since = (time_now - submission_time).total_seconds()
        if time_since <= 60: #change according to frequency script is run
            title = submission.title
            body = submission.selftext
            #url = submission.url

            #this can be made to almost always find a relevant response using a while loop
            #making the search query less specific every loop until something new is found
            #base case of no response would then occur when search query is most basic ie one word
            #not searching with the body because the query can be too big
            responseText = ''
            i = 0
            while(responseText == '' and i <= 5):
                for result in copypasta.search(title):
                    if (responseText == '' and result.selftext and result.selftext != body):
                        responseText = result.selftext
                        break
                i += 1
                if(responseText == ''):
                    sleep(2)

            submission.reply(responseText)

run(login())
