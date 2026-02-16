# Misc
import os
import re
import random as random
from datetime import datetime

# Import ChatbotBase class
from chatbot_base import ChatbotBase

# ML and sentiment analysis libraries
from setfit import SetFitModel
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Surpress PyTorch warning messages bein printed to terminal
import warnings 
warnings.filterwarnings("ignore")


"""
Intent-based Chatbot that recognises user intents using classification and sentiment analysis and responds accordingly.

See Week-8a-Classifying-user-intents.ipynb & Week-8b-Sentiment-analysis.ipynb for the tasks that guide you through developing this bot. 
"""

class IntentChatbot(ChatbotBase):
    def __init__(self, name="IntentBot"):
        ChatbotBase.__init__(self,name)
        
        # Load in trained model
        # You will need to train the model using the code in Week-8a-Classifying-user-intents.ipynb before this will work
        self.model = SetFitModel.from_pretrained("ckpt/", local_files_only=True)
        self.sid = SentimentIntensityAnalyzer()


    # Clean and process input text
    def process_input(self, user_input):
        processed_input = re.sub(r'[^\x00-\x7f]',r'', user_input) 
        processed_input = processed_input.lower()
        return processed_input
    
    # Respond to Greeting intent
    def greeting(self):
        print(f"Hello I am {self.name}, I recognise your intents and respond accordingly!")
    
    # Respond to Farewell intent
    def farewell(self):
        self.conversation_is_active = False
        responses = ['Goodbye',
                    'Have a nice day',
                    'See you later!',
                    'Take care, bye!']           
        
        print(random.choice(responses))
        return "Conversation has terminated"

    # Respond to Positive Confirmation intent
    def respond_postive_confirmation(self):
        responses = ['Great!',
                    'Happy to be of service!',
                    'Glad I could help.',
                    'no problem.']           
        
        print(random.choice(responses))

    # Respond to Negative Confirmation
    def respond_negative_confirmation(self):
        responses = ["I'm sorry, I will try better next time",
                    'Oh ok.',
                    "I am sorry I couldn't be of assistance, I will try harder in future.",
                    'Sorry about that.']           
        
        print(random.choice(responses))

    # Respond to Small Talk intent
    def respond_small_talk(self):
        responses = ['I am good, how are you?',
                    "I'm doing great!",
                    "All good thanks for asking, how are you?",
                    "I'm doing fine, how has your day been?"]           
        
        print(random.choice(responses))

    # Respond to Time Enquiry intent
    def get_time(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return f"The time is {current_time}"

    # Respond to Help intent
    def help(self):
        return "I am a helpful chatbot that assists you, why don't you try asking me for the time or to tell you a joke."

    # Respond to Escalate To Human intent
    def escalate_to_human(self):
        self.conversation_is_active = False
        print('I am passing you over to a human agent now')
        return "Conversation has terminated"

    # Respond to Request Joke intent
    def get_joke(self):
        # Jokes courtesy of Bob Mortimer, sourced from: https://thenorthernhalf.wordpress.com/2020/11/23/peter-beardsleys-joke-book/
        jokes = [
            "Have you tried that new coconut shampoo? It leaves your coconuts looking fabulous.",
            "This bloke said he was going to attack me with his guitar. I said is that a fret?",
            "I told me wife I got a job at the bowling alley. Ten pin she said. No it’s a permanent post I replied.",
            "I went to the local video shop and said could I borrow Batman Forever? He said, no you have to bring it back tomorrow.",
            "What has 4 wheels and flies? A bin lorry."
        ]
        return random.choice(jokes)

    # Responds if input is not understood
    def did_not_understand(self):
        return "I am sorry, I did not understand that, why don't you try asking me for the time or to tell you a joke."

    # Responds if input is not understood
    def respond_user_upset(self):
        return "I am sorry if I have upset you. Please say 'I want to speak to a real person' to get connect to a human agent."

    # Return true if compound sentiment is less than -0.3
    def user_is_upset(self, input_str):
        user_sentiment = self.sid.polarity_scores(input_str)
        return user_sentiment['compound'] < -0.3

    # Generate response for the user 
    def generate_response(self, processed_input):
        
        # Check sentiment first
        if self.user_is_upset(processed_input):
            return self.respond_user_upset()

        # Get probabilities for classes (Solution to Bonus Task B)
        output_probs = self.model.predict_proba(processed_input)
        output_probs = output_probs.tolist()
        max_conf = max(output_probs)
        
        # Check the max confidence, if too low, give appropraite response
        if max_conf < 0.3:
            return self.did_not_understand()
        
        # Otherwise return with correct class
        else:
            max_class = output_probs.index(max_conf)
            # Use a match/case statement which is a neater version of an if-else-if-else statement
            match max_class:
                case 0:
                    return self.greeting()
                case 1:
                    return self.farewell()
                case 2:
                    return self.respond_postive_confirmation()
                case 3:
                    return self.respond_negative_confirmation()
                case 4:
                    return self.respond_small_talk()
                case 5:
                    return self.get_time()
                case 6:
                    return self.help()
                case 7:
                    return self.escalate_to_human()
                case 8:
                    return self.get_joke()

                # If an exact match is not confirmed, this last case will be used if provided
                case _:
                    return self.did_not_understand()

    
if __name__ == "__main__":
    intent_bot = IntentChatbot()
    intent_bot.greeting()

    response = 'How can I help you?'

    while intent_bot.conversation_is_active:
        response = intent_bot.respond(response)

