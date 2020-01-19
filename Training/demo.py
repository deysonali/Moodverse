import random

# from Utilities import google_nlp
import cognitive_distortions

flagger = ["kill myself", "death", "die", "suicide", "suicidal", "end myself"]
emergency_responses = ["If you feel you are at risk of hurting yourself or someone else, please call 911 immediately.",
                 "If you are in an emergency situation, please call 911 to get help.",
                 "Please call 911.",
                 "If you are in a crisis, please call 911."]

clarifying_questions = ["I'm sorry you are feeling down. What is bothering you?",
                        "What's causing you to feel like that?",
                        "What's the main reason for you feeling like that right now?",
                        "Maybe you could tell me more about why?"]

sympathy = ["I'm sorry you feel that way.", "Thank you for sharing.", "That sounds like a tough situation."
            "I'm here for you, let's work through this."]

pride = ["I hope you're feeling better!", "I'm proud of you for recognizing how amazing you are!",
         "I'm glad you see how awesome you are!", "I'm happy you recognize your worth!"]

identification = ["It seems you're feeling strongly about {}.", "It seems {} is the main thing on your mind today."
                  "Looks like {} is weighing on your mind mainly."]

cog_dist = ["Your negative thought seems to be a {} though.", "Consider that this pattern of thinking could be {}.",
            "Your thought sounds like it could be a case of {}."]

reframing = ["Can you tell me about a time that {} made you think highly of yourself?", "What about a time {} had"
                                                                                        "a positive impact on you?",
             "Could you try and reframe your feelings about {} as a more balanced reflection of yourself?",
             "If your friend came to you worrying about {}, what would you tell them? How does that make you feel about yourself now?"]



def clarify():
    return clarifying_questions[random.randint(0,len(responses)-1)]
    pass
def emergency_protocol():
    return responses[random.randint(0,len(responses)-1)]

def low_response():
    pass
def mid_response():
    pass
def high_response():
    pass
def end_chat():
    pass
if __name__ == '__main__':
    print("Welcome to Moodverse! How are you feeling?")

    initial = input()
    emergency = False
    for word in initial:
        if word in flagger:
            emergency = True
            break
    if emergency:
        print(emergency_protocol())
    else:
        en_dict = categorize(initial)
