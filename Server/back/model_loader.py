from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle 
import numpy as np

love_hate_path = "../../Models/joy_v_sad.hd5"
love_hate_vars = "../../Models/joy_sad_vars.p"
emergency_path = "../../Models/joy_v_reddit.hd5"
emergency_vars = "../../Models/joy_reddit_vars.p"

class Model:
    
    def __init__(self, model_path, variables_path):
        
        self.model = load_model(model_path)
        self.word2id, self.max_words, self.id2label = pickle.load(open(variables_path, "rb"))
        
    def encode(self, sentence):
        X = []
        for word in sentence.split(" "):
            try:
                X.append(self.word2id[word])
            except:
                pass
        # Apply Padding to X
        X = pad_sequences([X], self.max_words)
        return X
    
    def predict(self, message):
        o = self.model.predict(self.encode(message.lower()))
        return self.id2label[np.argmax(o[0])], o[0]
        

love_model = Model(love_hate_path, love_hate_vars)
emergency_model = Model(emergency_path, emergency_vars)
