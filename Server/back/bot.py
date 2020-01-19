import sys
from text_generators import *
from utilities.cognitive_distortions import find_distortion

class Bot:
    
    def __init__(self, 
                 sympathetic_responses = BASE_REPLIES["sympathetic"],
                 clarification_responses = (BASE_REPLIES["clarify"], BASE_REPLIES["clarify_entity"]),
                 flag_detect = lambda x: False
                 ):
        
        self.sympatheticResponse = randomResponses(sympathetic_responses)
        self.cogResponse = cogDist(BASE_REPLIES["cog_dist"])
        self.clarificationResponse = clarificationResponse(clarification_responses[0], clarification_responses[1])
        
        self.flag_check = flag_detect
        self.seq = Sequence(
            self.get_initial_message,
            self.follow_exploration,
            )
        self.profile = Profile()

    def capture(self, message):
        
        # Grab self-love score
        self.profile.last_sl = self_love_score(message)
        # Grab top negative / top positive entities
        
    
    def check_leave_intent(self, message):
        words = ["bye", "bye!", "goodbye"]
        for word in words:
            if word in message.lower():
                return True
    
    def get_response(self, message):
        
        self.capture(message)
        
        if self.flag_check(message):
            self.emergency_reply()
            return 
        
        if self.check_leave_intent(message):
            self.exit(1)
            return
        
        response = self.seq.next()(message)
    
    def send(message):
        sys.stdout.write(format_reply(str(message)))
    
    def format_reply(message):
        
        # capitalize first letter
        message[0] = message[0].upper()
        # end with a period
        if message[-1] != '.':
            message[-1] = '.'
        
        return message
    
    def send_sequential_message(self, **kwargs):
        message = ""
        for arg in kwargs:
            message += self.format_reply(arg) + " "
        self.send(message)
    
    def get_initial_message(self, message):
        
        self.send_sequential_message(
            self.sympatheticResponse.generate(),
            # Generate categorical insight response
            self.cogResponse.generate(self.initial_message),
            # Ask for general clarification
            self.clarificationResponse.generate(),
        )

    # def 

class Profile:
    
    def __init__(self, user):
        self.user = user
        self.last_sl = 0. # last_self-love score (out of 1)
        self.entities = {}
    
    def get_history(self):
        #TODO: Implement w/ firebase
        pass

class Sequence:
    
    def __init__(self, methods):
        self.methods = methods
        self.last = self.methods[0]

    def _get_pos(self, method):
        return self.methods.index(method)
    
    def next(self):
        i = self._get_pos(self.last)
        if i+1 < len(self.methods)-1:
            self.last = self.methods[i+1]
            return self.methods[i+1]