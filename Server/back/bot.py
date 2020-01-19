import sys
from .text_generators import *
from nlp import *
from .cognitive_distortions import find_distortion
from model_loader import *

def flag_detect(message):
        if "sadness" in emergency_model.predict(message)[0]:
            return True
        else:
            return False



class Bot:
    
    def __init__(self, 
                 user,
                 sympathetic_responses = BASE_REPLIES["sympathetic"],
                 clarification_responses = (BASE_REPLIES["clarify"], BASE_REPLIES["clarify_entity"]),
                 reframe_responses = BASE_REPLIES["reframing"],
                 cog_responses = BASE_REPLIES["cog_dist"],
                 flag_detect = flag_detect,
                 explorations_left = 3,
                 stage_12_threshold = 1/3,
                 stage_23_threshold = 2/3,
                 ):
        
        self.user = user
        self.done = False
        self.sympatheticResponse = randomResponses(sympathetic_responses)
        self.clarificationResponse = clarificationResponse(clarification_responses[0], clarification_responses[1])
        self.reframeResponse = reFrame(reframe_responses)
        self.cogResponse = cogDist(cog_responses)
        
        self.flag_check = flag_detect
        self.seq1 = Sequence(
            [self.get_initial_message,
            self.follow_exploration,]
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

    def evaluate(self, message):
        
        self.profile.update(message)
    
    def exit(self):
        score = self.profile.sl_scores[-1]
        msg1 = "Thank you for sharing today {}. I know it can be tricky to navigate your thoughts.".format(self.user)
        
        if score < self.stage_12_threshold:
            msg2 = "I'd like to recommend you to reach out to your closest therapist. While I'm always here for you, I believe you'd be most benefited by in-person professional. Click the About Me page to see some suggestions."
        else:
            msg2 = "Keep up the great work, and remember, I'm always here to listen :)"
        
        msg3 = "Chao!"     
        
        self.send_sequential_message(msg1, msg2, msg3)
        self.done = True
    
    def emergency_reply(self):
        
        self.send("{0}, I know this is a hard time with, especially with {1}. Take a deep breath because you're more powerful than you know. I'll be auto-dialing 9-1-1 in ten seconds unless you stop me.")
        self.done = True
        
    def check_leave_intent(self, message):
        words = ["bye", "bye!", "goodbye"]
        for word in words:
            if word in message.lower():
                return True
    
    def follow_exploration(self, message):
        
        recent_score = self.profile.sl_scores[-1]
        
        if self.explorations_left <= 0:
            self.exit()
            
        if recent_score > self.stage_23_threshold:
            stage = self.get_stage3_response
        elif recent.score < self.stage_12_threshold:
            stage = self.get_stage1_response
        else:
            stage = self.get_stage2_response
        
        self.explorations_left -= 1
        stage(message)
    
    def get_response(self, message):
        
        if not self.done:
        
            self.evaluate(message)
            
            if self.flag_check(message):
                self.emergency_reply()
                return 
            
            if self.check_leave_intent(message):
                self.exit()
            
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
            self.cogResponse.generate(message),
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

        entity = self.profile.fine_worst_entity()
        self.send_sequential_message(
            self.proudResponse.generate(entity),
        )
        self.exit()
        
class Profile:
    
    def __init__(self):
#         self.user = user
        self.sl_scores = []
        self.entities = {}
    
    def fine_worst_entity(self):
        
        all_e = self.entities
        lowest_score = 100
        lowest_ent = None
        
        for ent in all_e:
            if all_e[ent] < lowest_score:
                lowest_score = all_e[ent]
                lowest_ent = ent
    
        return lowest_ent
    
    def update_entities(self, entity_dict):
        pass
        
    def update(self, message):
        
        self.update_entities(get_entity_sentiment(message))
        l1,l2 = love_model.id2label[0], love_model.id2label[1]
        prediction, scores = love_model.predict(message)
        
        joy_id, sad_id = None, None
        
        if "joy" in l1:
            joy_id = 0
            sad_id = 1
        else:
            joy_id = 1
            sad_id = 0
            
        self.sl_scores.append(joy_id)
    
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
