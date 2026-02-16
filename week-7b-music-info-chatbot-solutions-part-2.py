import re
import string
import random as random
from chatbot_base import ChatbotBase

# Imports for web data retrieval
import time
import requests
import urllib.request
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup


"""
Retrieval based chatbot that finds biographical info about musicians.

See Week-6a-Retrieval-based-chatbots.ipynb for the tasks that guide you through developing this bot. 
"""

class MusicBot(ChatbotBase):
    def __init__(self, name="MusicBot"):
        ChatbotBase.__init__(self,name)
        
        self.session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
    
    def greeting(self):
        print(f"Hello I am {self.name}, I am here to give you song recommendations and information about your favourite artists!")

    def process_input(self, user_input):
        processed_input = re.sub(r'[^\x00-\x7f]',r'', user_input) 
        processed_input = processed_input.lower()
        return processed_input
    
    def get_html_content(self, target_url):
        try:
            r = self.session.get(target_url)
            soup = BeautifulSoup(r.content, 'html.parser')
            return soup
        except Exception as e:
            return None

    # Function from here: https://gist.github.com/dehowell/884204?permalink_comment_id=1771089#gistcomment-1771089
    def url_is_alive(self, url):
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'
        try:
            urllib.request.urlopen(request)
            return True
        except urllib.request.HTTPError:
            return False
        
    def name_to_wikipedia_page_name(self, input_str):
        output_str = input_str.lstrip().rstrip().replace(' ', '_')
        output_str = string.capwords(output_str)
        return output_str
    
    def create_wiki_url(self, query_str):
        url_root = 'https://en.wikipedia.org/wiki/'
        url_suffix = self.name_to_wikipedia_page_name(query_str)
        url = url_root+url_suffix
        if self.url_is_alive(url):
            return url
        else:
            return None

    def get_age(self, query_str):
        url = self.create_wiki_url(query_str)
        if url is None:
            return f'I am sorry, I could not find a wikipedia page for {query_str}'
        
        soup = self.get_html_content(url)
        if soup is None:
            return f"I am sorry, something went wrong when decoding the url {url}"
        
        try:
            age = soup.find("span", class_="ForceAgeToShow").get_text(strip=True).replace("(", "").replace(")", "")
        except Exception as e:
            return f"I am sorry, I could not find an age for {query_str}"
        
        return f"{query_str} is {age} years old"
        
    def get_birthplace(self, query_str):
        url = self.create_wiki_url(query_str)
        if url is None:
            return f'I am sorry, I could not find a wikipedia page for {query_str}'
        
        soup = self.get_html_content(url)
        if soup is None:
            return f"I am sorry, something went wrong when decoding the url {url}"
        
        try:
            birthplace = soup.find("div", class_="birthplace").get_text(strip=True)
        except Exception as e:
            return f"I am sorry, I could not find a birthplace for {query_str}"
        
        return f"{query_str} was born in {birthplace}"
    
    def get_genres(self, query_str):
        url = self.create_wiki_url(query_str)
        if url is None:
            return f'I am sorry, I could not find a wikipedia page for {query_str}'
        
        soup = self.get_html_content(url)
        if soup is None:
            return f"I am sorry, something went wrong when decoding the url {url}"
        
        try:
            genres_list = soup.find("th", string="Genres").find_next_sibling("td").find_all("li")
            genres = [genre.get_text(strip=True) for genre in genres_list]
        except Exception as e:
            return f"I am sorry, I could not find musical genres for {query_str}"
        
        return f"{query_str} has made music in the following genres: {', '.join(genres)}"

    def generate_response(self, processed_input):
        age_regex = r'(how old|what age) is (.+)'
        birthplace_regex = r'where (is|was) (.+) (from|born)'
        genre_regex = r'what (music |musical )?genres does (.+) (play|perform|make)'

        age_match = re.match(age_regex, processed_input)
        birthplace_match = re.match(birthplace_regex, processed_input)
        genre_match = re.match(genre_regex, processed_input)
        
        if age_match:
            query_str = age_match.group(2)
            return self.get_age(query_str)
        elif birthplace_match:
            query_str = birthplace_match.group(2)
            return self.get_birthplace(query_str)   
        elif genre_match:
            query_str = genre_match.group(2)
            return self.get_genres(query_str)
        else:
            return 'I did not understand, try asking me for a musicians age, birthplace or what genres of music they play'



if __name__ == "__main__":
    music_bot = MusicBot()
    music_bot.greeting()

    response = 'How can I help you?'

    while music_bot.conversation_is_active:
        response = music_bot.respond(response)

