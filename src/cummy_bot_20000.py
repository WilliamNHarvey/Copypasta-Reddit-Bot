#Call this using a crontab on your server with the following settings to run once per minute:
#* * * * * cd ~/python/reddit_script_template/src; python reddit_script_template.py

#If you don't own a server, consider using vagrant https://www.vagrantup.com/intro/getting-started/
#* * * * * cd /vagrant/reddit_script_template/src; python reddit_script_template.py

import praw
import re
import datetime

def login():
    reddit = praw.Reddit('reddit_script_template')
    return reddit

def run(r):
    copypasta = r.subreddit("copypasta")
    localSub = r.subreddit("copypasta")

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
            for result in copypasta.search(title):
                if (result.selftext != body):
                    responseText = result.selftext

            submission.add_comment(responseText);

run(login())
