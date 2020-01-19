import random
from cognitive_distortions import find_distortion
from nlp import *

BASE_REPLIES = {
    "sympathetic" : ["I'm sorry you feel that way.", 
                     "Thank you for sharing.", 
                     "That sounds like a tough situation."
                     "I'm here for you, let's work through this."],
    "cog_dist" : ["It seems like you follow a {0} cognitive distortion method of thinking. {0} occurs when {1}."],
    "clarify" : ["I'm sorry you are feeling down. What is bothering you?",
                "What's causing you to feel like that?",
                "What's the main reason for you feeling like that right now?",
                "Maybe you could tell me more about why?"],
    "clarify_entity" : ["I'm sorry you are feeling that way. Why do you think {} is bothering you?",
                "What's causing you to feel like that about {}?",
                "Do you honestly believe that about {} right now?",
                "Maybe you could tell me more about {}?"],
    "reframing" : ["Can you tell me about a time that {} made you think highly of yourself?", 
                   "What about a time {} had a positive impact on you?",
                    "Could you try and reframe your feelings about {} as a more balanced reflection of yourself?",
                    "If your friend came to you worrying about {}, what would you tell them? How does that make you feel about yourself now?"],
    "proud" : ["I hope you're feeling better, you're pretty fly.", "I'm proud of you for recognizing how amazing you are! {} can't hold you down.",
         "I'm glad you see how awesome you are!", "I'm happy you recognize your worth!", "I know it's hard talking about {0} and {1}, and you did such a good job. I'm proud of you!"],
}

class randomResponses:
    
    def __init__(self, available_prompts):
        self.available_prompts = available_prompts
    
    def generate(self):
        return self.get_random()

    def get_random(self):
        i = random.randint(0, len(self.available_prompts)-1)
        return self.available_prompts[i]

class cogDist(randomResponses):
    
    def __init__(self, available_prompts):
        randomResponses.__init__(self, available_prompts)
    
    def generate(self, message):
        distortion = find_distortion(message)
        resp = self.get_random()
        return resp.format(distortion, self.lookUp(distortion))
    
    def lookUp(self, distortion):
        
        return {
            "mind_reading" : "assuming other people's thoughts about you",
            "overgeneralization" : "using one piece of evidence as the full truth",
            "polarized_thinking" : "you have an all or nothing attitude",
            "catastrophizing" : "when you make mountains out of molehills"
         }[distortion]

class reFrame(randomResponses):
    
    def __init__(self, available_prompts):
        randomResponses.__init__(self, available_prompts)
    
    def generate(self, message):
        entity = fine_worst_entity(message)
        distortion = find_distortion(message)
        resp = self.get_random()
        return resp.format(entity)
    
class proud(randomResponses):
    
    def __init__(self, available_prompts):
        randomResponses.__init__(self, available_prompts)
    
    def generate(self, entity):
        distortion = find_distortion(message)
        resp = self.get_random()
        if "{}" in resp:
            return resp.format(entity)
        return resp

class clarificationResponse:
    
    def __init__(self, general_responses, entity_responses):
        self.general_responses = general_responses
        self.entity_responses = entity_responses
    
    def generate(self, entity = None):
        
        if entity:
            i = random.randint(0, len(self.entity_responses)-1)
            return self.entity_responses[i].format(entity)
        else:
            i = random.randint(0, len(self.general_responses)-1)
            return self.general_responses[i]
