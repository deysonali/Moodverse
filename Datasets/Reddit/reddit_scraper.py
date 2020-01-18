import praw
import re
import pickle
from credentials import *

reddit = praw.Reddit(
          client_id=client_id,
          client_secret=client_secret,
          user_agent='Moodverse'
          )

# Define subreddits 
subs = {
  "depression" : None,
  "confessions" : None,
  "depression_help" : None,
  "Anxiety" : None
}
THREAD_LIMIT = 100

def remove_emoji_and_url(str):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    str = RE_EMOJI.sub(r'', str)
    str = re.sub(r'^https?:\/\/.*[\r\n]*', '', str, flags=re.MULTILINE)
    str = str.replace('\n','')
    return str  
  
def find_max_comment(comments):
    max_score = 0
    max_comment = None
    for comment in comments:
      if hasattr(comment, "score") and hasattr(comment, "body"):
        if comment.score > max_score:
            max_comment = comment
            max_score = comment.score
  #  if not max_comment:
   #     print(max_score)
    #    max_comment = comments[0]

    return max_comment

def download_top(sub=str, limit=int):
  posts = reddit.subreddit(sub).top(limit=limit)
  post_comments = []
  
  for submission in posts:
    post = remove_emoji_and_url(submission.title) + "\n" + remove_emoji_and_url(submission.selftext)
    if submission.comments.list():
        comment = remove_emoji_and_url(find_max_comment(submission.comments.list()[:1000]).body)
        post_comments.append([post, comment])
  
  return post_comments

print("Downloading")

for sub in subs:
  print(sub)
  posts = download_top(sub, THREAD_LIMIT)
  subs[sub] = posts
  
pickle.dump(subs, open("post_comments.pickle", "wb" ))
  
print("Saved")
