import praw
import datetime
import time

r = praw.Reddit('cummy_bot_20000')
copypasta = r.subreddit("copypasta")
localSub = r.subreddit("copypasta")


def run():
    #Checks the top 10 posts in the "new" category in the subreddit
    num_posts_to_check = 5
    for submission in localSub.new(limit=num_posts_to_check):
        time_now = datetime.datetime.utcnow()
        submission_time = datetime.datetime.utcfromtimestamp(submission.created_utc)
        time_since = int((time_now - submission_time).total_seconds())
        if time_since <= 10: #change according to frequency script is run
            title = submission.title
            body = submission.selftext

            #this can be made to almost always find a relevant response using a while loop
            #making the search query less specific every loop until something new is found
            #base case of no response would then occur when search query is most basic ie one word
            #not searching with the body because the query can be too big

            for result in copypasta.search(title.encode("utf8"), 'relevance', 'plain', 'all'):
                if result.selftext.encode("utf8") != '' and result.selftext.encode("utf8") != body.encode("utf8"):
                    submission.reply(result.selftext.encode("utf8"))
                    break


def main():
    while(1):
        run()
        time.sleep(10)

if __name__ == '__main__':
    main()
