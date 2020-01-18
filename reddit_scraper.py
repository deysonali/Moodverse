#! python3

import praw
import re
import pandas as pd
import pickle

# max_check = 10

def remove_emoji_url(str):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    str = RE_EMOJI.sub(r'', str)
    str = re.sub(r'^https?:\/\/.*[\r\n]*', '', str, flags=re.MULTILINE)
    str = str.replace('\n','')
    return str

# def is_positive(str):
#     if sentiment>=threshold:
#         return True
#     else:
#         return False


r_depression = reddit.subreddit('depression')
r_confessions = reddit.subreddit('confessions')
r_depression_help = reddit.subreddit('depression_help')
r_Anxiety = reddit.subreddit('Anxiety')

top_depression = r_depression.top(limit=100)
# top_confessions = r_confessions.top(limit=3)
top_depression_help = r_depression_help.top(limit=100)
top_Anxiety = r_Anxiety.top(limit=100)

depression_list = []
confessions_list = []
depression_help_list = []
Anxiety_list = []

for submission in top_depression:
    depression_list.append(remove_emoji_url(submission.title) + remove_emoji_url(submission.selftext))
    depression_list.append([remove_emoji_url(comment.body) for comment in submission.comments if (hasattr(comment, "body")
                                    and comment.distinguished==None)][0])
# for submission in top_confessions:
#     confessions_list.append(remove_emoji_url(submission.title) + remove_emoji_url(submission.selftext))
#     confessions_list.append([remove_emoji_url(comment.body) for comment in submission.comments if (hasattr(comment, "body")
#                                     and comment.distinguished==None)][0])
for submission in top_Anxiety:
    Anxiety_list.append(remove_emoji_url(submission.title) + remove_emoji_url(submission.selftext))
    Anxiety_list.append([remove_emoji_url(comment.body) for comment in submission.comments if (hasattr(comment, "body")
                                    and comment.distinguished==None)][0])
for submission in top_depression_help:
    depression_help_list.append(remove_emoji_url(submission.title) + remove_emoji_url(submission.selftext))
    depression_help_list.append([remove_emoji_url(comment.body) for comment in submission.comments if (hasattr(comment, "body")
                                    and comment.distinguished==None)][0])

pickle.dump(depression_list, open( "depression", "wb" ) )
pickle.dump(depression_help_list, open( "depression_help.p", "wb" ) )
pickle.dump(Anxiety_list, open( "Anxiety.p", "wb" ) )



# print(depression_list)
# print(Anxiety_list)
# print(confessions_list)
# print(depression_help_list)