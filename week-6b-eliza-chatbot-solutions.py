import re
import random as random
from chatbot_base import ChatbotBase

"""
Eliza-esque chatbot that performs therapy in the style of the original Eliza chatbot: https://web.njit.edu/~ronkowit/eliza.html
"""

class Eliza(ChatbotBase):
    def __init__(self, name="Eliza"):
        ChatbotBase.__init__(self,name)
        self.conversation_is_active = True
        
        # List of tuples with regex and replace string pairs
        self.pronoun_pairings = [
            (r"\b(am)\b", "are"),
            (r"\b(was)\b", "were"),
            (r"\b(i)\b", "you"),
            (r"\b(i'd)\b", "you would"),
            (r"\b(i've)\b", "you have"),
            (r"\b(i'll)\b", "you will"),
            (r"\b(my)\b", "your"),
            (r"\b(are)\b", "am"),
            (r"\b(you've)\b", "I have"),
            (r"\b(you'll)\b", "I will"),
            (r"\b(your)\b", "my"),
            (r"\b(yours)\b", "mine"),
            (r"\b(you)\b", "me"),
            (r"\b(me)\b", "you")
        ]

        # List of default responses if no matches are made
        self.default_responses = ["Please tell me more.",
                            "Let's change focus a bit... Tell me about your family.",
                            "Can you elaborate on that?",
                            "Why do you say that?",
                            "I see.",
                            "Very interesting.",
                            "I see.  And what does that tell you?",
                            "How does that make you feel?",
                            "How do you feel when you say that?"]
        
        # List of default responses if no matches are made
        self.regex_and_response = [
            ("i need (.+)", [
                "Why do you need {x}?",
                "Would it really help you to get {x}?",
                "Are you sure you need {x}?"
            ]),
            ("i can'?t (.+)", [
                "How do you know you can't {x}?",
                "Perhaps you could {x} if you tried.",
                "What would it take for you to {x}?"
            ]),
            ("i am (.+)", [
                "Did you come to me because you are {x}?",
                "How long have you been {x}?",
                "How do you feel about being {x}?"
            ]),
        ]
    
    def greeting(self):
        print(f"Hello I am {self.name}, you're friendly therapist for today")

    def farewell(self):
        self.conversation_is_active = False
        responses = ['Goodbye',
                    'Have a nice day',
                    'I hope you had a productive therapy session, see you next time']           
        
        print(random.choice(responses))
        return "You're therapy session has now ended"

    # Simplify input string
    def process_input(self, user_input):
        processed_input = re.sub(r'[^\x00-\x7f]',r'', user_input) 
        processed_input = processed_input.lower()
        return processed_input
    
    # Swap pronouns in extracted text, break when a substitution has been made
    def swap_pronoun(self, extract_str):        
        for regex, replacement_str in self.pronoun_pairings:
            extract_str, sub_n = re.subn(regex, replacement_str, extract_str)
            if sub_n > 0:
                break
        return extract_str        
    
    # Use regex to find a match, swap pronouns and replace text in response string
    def match_and_respond(self, input_str, regex, responses):
        re_match = re.match(regex, input_str)

        if re_match is None:
            return None
        else:
            extracted_str = re_match.group(1)
            extracted_str = self.swap_pronoun(extracted_str)
            response = random.choice(responses)
            response = re.sub(r'{x}', extracted_str, response)
            return response 
    
    # Function that generates a response based on the processed input
    def generate_response(self, processed_input):
        hello_regex = r'\b(hello|hi|hey)\b'
        bye_regex = r'\b(bye|goodbye|end|exit|quit)\b'
        
        # Iterate over all regex's and reset responses in self.regex_and_response
        for regex, responses in self.regex_and_response:
            response = self.match_and_respond(processed_input, regex, responses)
            if response is not None:
                return response
            else:
                pass
        
        # If no matches in regex_and_response check for a greeting message
        if re.search(hello_regex, processed_input):
            responses = ['Hello',
                         'Nice to meet you',
                         'We have already introduced ourselves...']
            return random.choice(responses)
        
        # Then check for a farewell message
        elif re.search(bye_regex, processed_input):
            self.farewell()

        # If no matches have been made then give a default response
        else:
            return random.choice(self.default_responses)

    # Identical to respond function in ChatbotBase        
    def respond(self, out_message = None):
        if isinstance(out_message, str): 
            print(out_message)

        received_input = self.receive_input()
        processed_input = self.process_input(received_input)
        response = self.generate_response(processed_input)
        return response
    
if __name__ == "__main__":
    
    eliza = Eliza()
    eliza.greeting()

    response = 'How can I help you today?'

    while eliza.conversation_is_active:
        response = eliza.respond(response)

