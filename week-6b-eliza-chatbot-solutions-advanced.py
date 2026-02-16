import re
import random as random
from chatbot_base import ChatbotBase

"""
Eliza-esque chatbot that performs therapy in the style of the original Eliza chatbot: https://web.njit.edu/~ronkowit/eliza.html
"""

class ELIZA(ChatbotBase):
    def __init__(self, name="ELIZA"):
        ChatbotBase.__init__(self,name)
        self.conversation_is_active = True
        
        # List of tuples with regex and replace string pairs
        self.pronoun_pairings = [
            (r"\b(am)\b", "are"),
            (r"\b(was)\b", "were"),
            (r"\b(i)\b", "you"),
            (r"\b(i'd)\b", "you would"),
            (r"\b(i'?ve)\b", "you have"),
            (r"\b(i'll)\b", "you will"),
            (r"\b(my)\b", "your"),
            (r"\b(are)\b", "am"),
            (r"\b(you'?ve)\b", "I have"),
            (r"\b(you'?ll)\b", "I will"),
            (r"\b(your)\b", "my"),
            (r"\b(your'?s)\b", "mine"),
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
        
        # List of tuples with contain a regex and a set of reponses
        self.regex_and_response = [
            ("i need (.+)", [
                "Why do you need {x}?",
                "Would it really help you to get {x}?",
                "Are you sure you need {x}?"
            ]),

            ("why don'?t you ([^?]+)?", [
                "Do you really think I don't {x}?",
                "Perhaps eventually I will {x}.",
                "Do you really want me to {x}?"
            ]),

            ("why can'?t i ([^?]+)?", [
                "Do you think you should be able to {x}?",
                "If you could {x}, what would you do?",
                "I don't know -- why can't you {x}?",
                "Have you really tried?"
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

            ("i'm (.+)", [
                "How does being {x} make you feel?",
                "Do you enjoy being {x}?",
                "Why do you tell me you're {x}?",
                "Why do you think you're {x}?"
            ]),

            ("are you ([^?]+)?", [
                "Why does it matter whether I am {x}?",
                "Would you prefer it if I were not {x}?",
                "Perhaps you believe I am {x}.",
                "I may be {x} -- what do you think?"
            ]),

            ("what (.+)", [
                "Why do you ask?",
                "How would an answer to that help you?",
                "What do you think?"
            ]),

            ("how (.+)", [
                "How do you suppose?",
                "Perhaps you can answer your own question.",
                "What is it you're really asking?"
            ]),

            ("because (.+)", [
                "Is that the real reason?",
                "What other reasons come to mind?",
                "Does that reason apply to anything else?",
                "If {x}, what else must be true?"
            ]),

            ("(.*) sorry (.*)", [
                "There are many times when no apology is needed.",
                "What feelings do you have when you apologize?"
            ]),
            ("i think (.+)", [
                "Do you doubt {x}?",
                "Do you really think so?",
                "But you're not sure {x}?"
            ]),

            ("(.*) friend (.*)", [
                "Tell me more about your friends.",
                "When you think of a friend, what comes to mind?",
                "Why don't you tell me about a childhood friend?"
            ]),

            ("yes", [
                "You seem quite sure.",
                "OK, but can you elaborate a bit?"
            ]),

            ("(.*) computer(.*)", [
                "Are you really talking about me?",
                "Does it seem strange to talk to a computer?",
                "How do computers make you feel?",
                "Do you feel threatened by computers?"
            ]),

            ("is it (.+)", [
                "Do you think it is {x}?",
                "Perhaps it's {x} -- what do you think?",
                "If it were {x}, what would you do?",
                "It could well be that {x}."
            ]),

            ("it is (.+)", [
                "You seem very certain.",
                "If I told you that it probably isn't {x}, what would you feel?"
            ]),

            ("can you ([^?]+)?", [
                "What makes you think I can't {x}?",
                "If I could {x}, then what?",
                "Why do you ask if I can {x}?"
            ]),

            ("can i ([^?]+)?", [
                "Perhaps you don't want to {x}.",
                "Do you want to be able to {x}?",
                "If you could {x}, would you?"
            ]),

            ("you are (.+)", [
                "Why do you think I am {x}?",
                "Does it please you to think that I'm {x}?",
                "Perhaps you would like me to be {x}.",
                "Perhaps you're really talking about yourself?"
            ]),

            ("you'?re (.+)", [
                "Why do you say I am {x}?",
                "Why do you think I am {x}?",
                "Are we talking about you, or me?"
            ]),

            ("i don'?t (.+)", [
                "Don't you really {x}?",
                "Why don't you {x}?",
                "Do you want to {x}?"
            ]),

            ("i feel (.+)", [
                "Good, tell me more about these feelings.",
                "Do you often feel {x}?",
                "When do you usually feel {x}?",
                "When you feel {x}, what do you do?"
            ]),

            ("i have (.+)", [
                "Why do you tell me that you've {x}?",
                "Have you really {x}?",
                "Now that you have {x}, what will you do next?"
            ]),

            ("i would (.+)", [
                "Could you explain why you would {x}?",
                "Why would you {x}?",
                "Who else knows that you would {x}?"
            ]),

            ("is there (.+)", [
                "Do you think there is {x}?",
                "It's likely that there is {x}.",
                "Would you like there to be {x}?"
            ]),

            ("my (.+)", [
                "I see, your {x}.",
                "Why do you say that your {x}?",
                "When your {x}, how do you feel?"
            ]),

            ("you (.+)", [
                "We should be discussing you, not me.",
                "Why do you say that about me?",
                "Why do you care whether I {x}?"
            ]),

            ("why (.+)", [
                "Why don't you tell me the reason why {x}?",
                "Why do you think {x}?"
            ]),

            ("i want (.+)", [
                "What would it mean to you if you got {x}?",
                "Why do you want {x}?",
                "What would you do if you got {x}?",
                "If you got {x}, then what would you do?"
            ]),

            ("(.*) mother(.*)", [
                "Tell me more about your mother.",
                "What was your relationship with your mother like?",
                "How do you feel about your mother?",
                "How does this relate to your feelings today?",
                "Good family relations are important."
            ]),

            ("(.*) father(.*)", [
                "Tell me more about your father.",
                "How did your father make you feel?",
                "How do you feel about your father?",
                "Does your relationship with your father relate to your feelings today?",
                "Do you have trouble showing affection with your family?"
            ]),

            ("(.*) child(.*)", [
                "Did you have close friends as a child?",
                "What is your favorite childhood memory?",
                "Do you remember any dreams or nightmares from childhood?",
                "Did the other children sometimes tease you?",
                "How do you think your childhood experiences relate to your feelings today?"
            ])
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

    # Check and simplify input string
    def process_input(self, user_input):
        # Check input is string
        if not isinstance(user_input, str):
            raise ValueError('I can only understand text!')
        
        # Check input is less than 500 characters
        if len(user_input) > 500:
            raise ValueError('Too much information! Please only tell me one thing at a time!')

        # Remove non-ascii characters from string
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

        # If no match return None
        if re_match is None:
            return None
        # If no subgroups then just give a random response
        if len(re_match.groups()) < 1:
            response = random.choice(responses)
            return response
        # If there is a subgroup then replace {x} with extracted text 
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
            
    # Main response function, print out input message, receive a new input, process it and return a new response
    def respond(self, out_message = None):
        if isinstance(out_message, str): 
            print(out_message)

        received_input = self.receive_input()
        try:
            processed_input = self.process_input(received_input)
            response = self.generate_response(processed_input)
            return response
        except ValueError as e:
            return ValueError.message
    
if __name__ == "__main__":
    
    eliza = ELIZA()
    eliza.greeting()

    response = 'How can I help you today?'

    while eliza.conversation_is_active:
        response = eliza.respond(response)
































