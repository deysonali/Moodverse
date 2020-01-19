import sys
from .text_generators import *
from .utilities.nlp import *
from .utilities.cognitive_distortions import find_distortion

class Bot:
    
    def __init__(self, 
                 sympathetic_responses = BASE_REPLIES["sympathetic"],
                 clarification_responses = (BASE_REPLIES["clarify"], BASE_REPLIES["clarify_entity"]),
                 reframe_responses = BASE_REPLIES["reframing"],
                 cog_responses = BASE_REPLIES["cog_dist"],
                 flag_detect = flag_detect,
                 explorations_left = 3,
                 stage_12_threshold = 2/3,
                 stage_23_threshold = 1/3,
                 ):
        
        self.sympatheticResponse = randomResponses(sympathetic_responses)
        self.clarificationResponse = clarificationResponse(clarification_responses[0], clarification_responses[1])
        self.reframeResponse = reFrame(reframe_responses)
        self.cogResponse = cogDist(cog_responses)
        
        self.flag_check = flag_detect
        self.seq1 = Sequence(
            self.get_initial_message,
            self.follow_exploration,
            )
        # self.seq2 = CyclicSequence(
        #     self.get_stage1_response,
        #     self.get_stage2_response,
        #     self.get_stage3_response
        #     )
        self.profile = Profile()
        self.explorations_left = explorations_left
        self.stage_12_threshold = stage_12_threshold
        self.stage_23_threshold = stage_23_threshold

    def capture(self, message):
        
        # Grab self-love score
        self.profile.last_sl = self_love_score(message)
        # Grab top negative / top positive entities
        # self
    
    def exit(self, self_love_score):
        pass                   
    
    def check_leave_intent(self, message):
        words = ["bye", "bye!", "goodbye"]
        for word in words:
            if word in message.lower():
                return True
    
    def follow_exploration(self, message):
        
        recent_score = self.profile.sl_scores[-1]
        
        if self.explorations_left <= 0:
            self.exit(recent_score)
            
        if     
    
    def get_response(self, message):
        
        self.capture(message)
        
        if self.flag_check(message):
            self.emergency_reply()
            return 
        
        if self.check_leave_intent(message):
            self.exit(1)
            return
        
        response = self.seq1.next()(message)
    
    def send(message):
        return format_reply(str(message))
        # sys.stdout.write()
    
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

    def get_stage1_response(self, message):

        self.send_sequential_message(
            self.sympatheticResponse.generate(),
            self.clarificationResponse.generate(message),
        )
     
    def get_stage2_response(self, message):

        self.send_sequential_message(
            self.reframeResponse.generate(message),
        )
     
    def get_stage3_response(self, message):

        self.send_sequential_message(
            self.proudResponse.generate(),
        )
        self.exit(self.sl_scores[-1])
        
class Profile:
    
    def __init__(self, user):
        self.user = user
        self.sl_scores = []
        self.entities = {}
    
    def update_entities(self, entity_dict):
        pass
    
    def get_history(self):
        #TODO: Implement w/ firebase
        pass

class Sequence:
    
    def __init__(self, methods):
        self.methods = methods
        self.untouched = True
        self.last = self.methods[0]

    def _get_pos(self, method):
        return self.methods.index(method)
    
    def next(self):
        i = self._get_pos(self.last)
        if self.untouched:
            self.untouched = False
            return self.methods[i]
        
        next_i = i+1
        if next_i <= len(self.methods)-1:
            self.last = self.methods[next_i]
            return self.methods[next_i]

class CyclicSequence:
    
    def __init__(self, methods):
        self.methods = methods
        self.last = self.methods[0]

    def _get_pos(self, method):
        return self.methods.index(method)
    
    def next(self):
        c = self._get_pos(self.last)
        next_c = c+1
        
        if next_c > len(self.methods)-1:
            next_c = next_c % len(self.methods)
            
        self.last = self.methods[next_c]
        return self.methods[next_c]
        
def flag_detect(message):
    if "sadness" in emergency_model.predict(message)[0]:
        return True
    else:
        return False