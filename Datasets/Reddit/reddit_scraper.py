#! python3

import praw
import re
import pickle
from credentials import *

def remove_emoji_url(str):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    str = RE_EMOJI.sub(r'', str)
    str = re.sub(r'^https?:\/\/.*[\r\n]*', '', str, flags=re.MULTILINE)
    str = str.replace('\n','')
    return str

reddit = praw.Reddit(
          client_id=client_id,
          client_secret=client_secret,
          user_agent='Moodverse',
          username=username,
          password=password
          )

depression_list = []
confessions_list = []
depression_help_list = []
Anxiety_list = []

for submission in top_depression:
    flag = False
    depression_list.append(remove_emoji_url(submission.title) + remove_emoji_url(submission.selftext))
    for comment in submission.comments:
      if (hasattr(comment, "body") and comment.distinguished==None):
        depression_list.append(remove_emoji_url(comment.body))
        flag = True
        break
    if flag == False:
      depression_list.pop()


for submission in top_Anxiety:
    flag = False
    Anxiety_list.append(remove_emoji_url(submission.title) + remove_emoji_url(submission.selftext))
    for comment in submission.comments:
      if (hasattr(comment, "body") and comment.distinguished==None):
        Anxiety_list.append(remove_emoji_url(comment.body))
        flag = True
        break
    if flag == False:
      Anxiety_list.pop()

for submission in top_depression_help:
    flag = False
    depression_help_list.append(remove_emoji_url(submission.title) + remove_emoji_url(submission.selftext))
    for comment in submission.comments:
      if (hasattr(comment, "body") and comment.distinguished==None):
        depression_help_list.append(remove_emoji_url(comment.body))
        flag = True
        break
    if flag == False:
      depression_help_list.pop()

pickle.dump(depression_list, open("depression.p", "wb" ))
pickle.dump(depression_help_list, open( "depression_help.p", "wb" ))
pickle.dump(Anxiety_list, open("Anxiety.p", "wb" ))
