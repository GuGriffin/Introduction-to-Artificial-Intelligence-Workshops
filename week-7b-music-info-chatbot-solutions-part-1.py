import re
import random as random
from chatbot_base import ChatbotBase

# Imports for local data retrieval (part 1)
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize

"""
Retrieval based chatbot that recommends songs and finds biographical info about musicians.

See Week-6a-Retrieval-based-chatbots.ipynb for the tasks that guide you through developing this bot. 
"""

class MusicBot(ChatbotBase):
    def __init__(self, name="MusicBot"):
        ChatbotBase.__init__(self,name)
        
        self.dataset_path = 'class-datasets/lyric_data.tsv'
        self.column_names = ['ARTIST_NAME-SONG_NAME', 'SONG_NAME', 'LYRICS']
        self.dataset_separator = '\t'

        self.df = self.load_lyrics(self.dataset_path, self.dataset_separator, self.column_names)
        self.vectorizer, self.lyrics_matrix = self.lyrics_to_tfidf(self.df)
    
    def greeting(self):
        print(f"Hello I am {self.name}, I am here to give you song recommendations and information about your favourite artists!")

    def process_input(self, user_input):
        processed_input = re.sub(r'[^\x00-\x7f]',r'', user_input) 
        processed_input = processed_input.lower()
        return processed_input
    
    def load_lyrics(self, file_path, separator, column_names):
        df = pd.read_csv(file_path, sep=separator, usecols=column_names)
        return df

    def lyrics_to_bow(self, df):
        vectorizer = CountVectorizer(stop_words='english')
        lyrics_matrix = vectorizer.fit_transform(df['LYRICS'])
        return vectorizer, lyrics_matrix

    def lyrics_to_tfidf(self, df):
        vectorizer = TfidfVectorizer(stop_words='english')
        lyrics_matrix = vectorizer.fit_transform(df['LYRICS'])
        return vectorizer, lyrics_matrix

    def find_nearest_song(self, input_query):
        input_vec = self.vectorizer.transform([input_query])
        similarities = cosine_similarity(input_vec, self.lyrics_matrix).flatten()
        nearest_index = similarities.argmax()
        
        artist_song_id = self.df.iloc[nearest_index][self.column_names[0]]
        artist_id, song_id = artist_song_id.split('-')
        lyrics = self.df.iloc[nearest_index][self.column_names[2]]
        
        return artist_id, song_id, lyrics

    def generate_response(self, processed_input):
        song_regex = r'(give|recommend) me a song about (.+)'
        
        song_match = re.match(song_regex, processed_input)
        if song_match:
            query_str = song_match.group(2)
            artist_id, song_id, lyrics = self.find_nearest_song(query_str)
            return f"For a song about '{query_str}' I can recommend '{song_id}' by '{artist_id}'. Here is a sample of the lyrics: \n \n ''{lyrics[:250]}'' \n \n I hope that helps! Try putting in a different prompt to get a recommendation for another song."

        else:
            return "I did not understand, try asking 'give me a song about ...'"
    
if __name__ == "__main__":
    music_bot = MusicBot()
    music_bot.greeting()

    response = 'How can I help you?'

    while music_bot.conversation_is_active:
        response = music_bot.respond(response)

