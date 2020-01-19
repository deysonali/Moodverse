from nltk.corpus import wordnet
import nltk
import torch
import torchtext
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

glove = torchtext.vocab.GloVe(name="6B", # trained on Wikipedia 2014 corpus
 dim=50) # embedding size = 50

# categorizes w/ examples
mind_reading = ["He seems to dislike me", "My girlfriend seems to hate me", "They appear to be mad at me",
                "I assume they won't accept me"]
overgeneralization = ["I will never do well", "I will always be a failure", "I always ruin things",
                      "I never get it right"]
polarized_thinking = ["It would have been perfect if I hadn't failed", "I failed my goals", "It could have been perfect"]
catastrophizing = ["What if I can't", "I'm worried that it won't work", "I panicked because I was going to mess up"]
distortions = [mind_reading, overgeneralization, polarized_thinking, catastrophizing]

def similarity(sentence1, sentence2):
    s1 = sentence1.split()
    s2 = sentence2.split()
    s_1 = [glove[word] for word in s1]
    s_2 = [glove[word] for word in s2]
    len1 = len(s_1)
    len2 = len(s_2)
    one = s_1[0]
    two = s_2[0]
    for i in range(1,len(s_1)):
        one = one.add(s_1[i])
    for i in range(1, len(s_2)):
        two = two.add(s_2[i])
    one = torch.div(one,len1)
    two = torch.div(two,len2)
    sim = torch.cosine_similarity(one.unsqueeze(0), two.unsqueeze(0))
    return sim

def distortion_scores(sentence):
    score = []
    for d in distortions:
        dist_score = 0.0
        for example in d:
            sim = similarity(sentence, example)
            if sim > dist_score:
                dist_score = sim
        score = score + [dist_score]
    return score

def find_distortion(sentence):
    dists = ["Mind Reading", "Overgeneralization", "Polarized thinking", "Catastrophizing"]
    score = distortion_scores(sentence)
    ind = score.index(max(score))
    return dists[ind]
