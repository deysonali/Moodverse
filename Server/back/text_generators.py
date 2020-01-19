import random
from utilities.cognitive_distortions import find_distortion

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
}

class randomResponses:
    
    def __init__(self, available_prompts):
        self.available_prompts = available_prompts
    
    def generate(self):
        i = random.randint(0, len(self.available_prompts)-1)
        return self.available_prompts[i]

class cogDist(randomResponses):
    
    def __init__(self, available_prompts):
        super().__init__(self, available_prompts)
    
    def generate(self, message):
        distortion = find_distortion(message)
        i = random.randint(0, len(self.available_prompts)-1)
        resp = self.available_prompts[i]
        return resp.format(distortion, self.lookUp(distortion))
    
    def lookUp(self, distortion):
        #TODO: Lookup basic summary of each
        return ""

class clarificationResponse:
    
    def __init__(self, general_responses, entity_responses):
        self.general_responses = general_responses
        self.entity_responses = entity_responses
    
    def generate(entity = None):
        
        if entity:
            i = random.randint(0, len(self.entity_responses)-1)
            return self.entity_responses[i].format(entity)
        else:
            i = random.randint(0, len(self.general_responses)-1)
            return self.general_responses[i]