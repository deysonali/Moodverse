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
THREAD_LIMIT = 1000

print("Downloading")

for sub in subs:
  print(sub)
  posts = download_top(sub, THREAD_LIMIT)
  subs[sub] = posts
  print("Found {} posts".format(len(posts)))
print("Saving")

f = open(r"reddit_posts.txt", "w" )
[[f.write(text.lower().replace('"', '') + "\n") for text in subs[sub]] for sub in subs]
f.close()

print("Saved")
