import praw
import os
import pandas as pd
import datetime

# Creating a reddit obj and authorizing it with client ID and client Secret using Environment variable
reddit = praw.Reddit(
    client_id = os.getenv("clientid"),
    client_secret = os.getenv("clientsecret"),
    user_agent = "FakeNewsClassificaiton by /u/shnk_reddy",
    redirect_uri="http://www.example.com/unused/redirect/uri",
)

subs = ['news', 'WhitePeopleTwitter', 'Politics', 'WorldNews', 'NotTheOnion', 'fakenews']

# setting up columns for dataframe
columns = ['title', 'selftext', 'author', \
            'subreddit', 'created_utc', \
            'upvote_ratio', 'num_comments', \
            'permalink', 'url']

for sub in subs:
    subreddit = reddit.subreddit(sub)

    print("Fetching data for "+sub)
    hot_posts = subreddit.hot()

    data = []

    # collecting data from news sub
    for post in hot_posts:
        data.append([post.title, post.selftext, \
                     post.author, post.subreddit, \
                     post.created_utc, post.upvote_ratio, \
                     post.num_comments, post.permalink, \
                     post.url])


    # creating dataframe
    df = pd.DataFrame(data, columns = columns)

    print("writing data into file")
    # exporting the data
    data_path = 'data'
    file = str(datetime.datetime.now()).replace("-", "").replace(":", "").replace(" ", "_").split(".")[0]+sub+'.csv'
    save_as = data_path+'/'+file

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    df.to_csv(save_as)


