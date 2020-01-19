import sys
sys.path.append(r"../Reddit")
from reddit_scraper import *

# Define subreddits 
subs = {
  "depression" : None,
  # "confessions" : None,
  "depression_help" : None,
  "Anxiety" : None,
  "SuicideWatch" : None
}
THREAD_LIMIT = 100


print("Downloading")

for sub in subs:
  print(sub)
  posts = download_top(sub, THREAD_LIMIT)
  subs[sub] = posts

print("Saving")

f = open("Datasets/Negative_thoughts/reddit_posts.txt", "w" )
[[f.write(text + "/n") for text in subs[sub]] for sub in subs]
f.close()

print("Saved")
