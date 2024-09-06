
import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary NLTK resources
nltk.download('punkt')

# Define the reflections dictionary
reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}

# Define the pairs of patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, How are you today?"]],
    [r"hi|hey|hello", ["Hello!", "Hey there!"]],
    [r"what is your name", ["I am a chatbot created for you. You can call me Chatbot!"]],
    [r"how are you", ["I'm doing great, thanks! How about you?"]],
    [r"sorry (.*)", ["It's alright.", "No problem."]],
    [r"I am fine", ["Great to hear that! How can I assist you today?"]],
    [r"i'm (.*) doing good", ["Nice to hear that! How can I help you?"]],
    [r"(.*) age", ["I'm a computer program, so age doesn't apply to me."]],
    [r"what (.*) want", ["I want to assist you with any questions you have!"]],
    [r"(.*) created you", ["I was created by developers using Python's NLTK library."]],
    [r"(.*) (location|city)", ["I am based in the digital realm, but I have information about various cities."]],
    [r"how is the weather in (.*)", ["The weather in %1 is generally nice."]],
    [r"i work in (.*)", ["%1 sounds like a great place to work!"]],
    [r"(.*)raining in (.*)", ["I can't check the weather, but you can use weather apps for up-to-date information."]],
    [r"how (.*) health", ["I'm a computer program, so I'm always in perfect health!"]],
    [r"(.*) (sports|game)", ["I enjoy keeping up with sports like cricket and football."]],
    [r"who (.*) sportsperson", ["Some popular sportspersons are Shahid Afridi, Babar Azam, and Misbah-ul-Haq."]],
    [r"who (.*) (moviestar|actor)", ["Some famous actors are Mahira Khan, Humayun Saeed, and Fawad Khan."]],
    [r"i am looking for online guides and courses to learn data science, can you suggest", ["You can check out platforms like Coursera, Udacity, and DataCamp for comprehensive data science courses."]],
    [r"quit", ["Goodbye! Take care and see you soon!"]],
    # Additional relevant questions for a Pakistani audience
    [r"what is the capital of Pakistan", ["The capital of Pakistan is Islamabad."]],
    [r"what languages are spoken in Pakistan", ["In Pakistan, Urdu and English are the official languages, and there are many regional languages like Punjabi, Sindhi, Pashto, and Balochi."]],
    [r"what is Pakistan famous for", ["Pakistan is famous for its rich history, cultural heritage, beautiful landscapes, and delicious cuisine."]],
    [r"tell me about the food in Pakistan", ["Pakistani cuisine includes dishes like Biryani, Nihari, Chapli Kebab, and delicious street food such as Golgappa and Chaat."]],
    [r"what are some popular tourist destinations in Pakistan", ["Some popular tourist destinations include Murree, Hunza Valley, Skardu, and Lahore."]],
    [r"who is the current Prime Minister of Pakistan", ["As of now, the Prime Minister of Pakistan is Shehbaz Sharif."]],
    [r"what is the national animal of Pakistan", ["The national animal of Pakistan is the Markhor."]],
    [r"what is the national flower of Pakistan", ["The national flower of Pakistan is the Jasmine."]],
    [r"what is the national sport of Pakistan", ["The national sport of Pakistan is field hockey."]],
    [r"how can I get a visa to Pakistan", ["You can apply for a visa to Pakistan through the official embassy or consulate of Pakistan in your country."]],
    [r"what are the major festivals celebrated in Pakistan", ["Major festivals in Pakistan include Eid-ul-Fitr, Eid-ul-Adha, Basant, and Independence Day."]],
    [r"what is the currency of Pakistan", ["The currency of Pakistan is the Pakistani Rupee (PKR)."]],
    [r"what is the major industry in Pakistan", ["Major industries in Pakistan include textiles, agriculture, and manufacturing."]],
    [r"how is the education system in Pakistan", ["The education system in Pakistan includes primary, secondary, and higher education with many public and private institutions."]],
    [r"what are some popular TV shows in Pakistan", ["Popular TV shows include drama serials like 'Humsafar', 'Zindagi Gulzar Hai', and 'Meri Zindagi Hai Tu'."]],
    [r"what is the time zone of Pakistan", ["Pakistan is in the Pakistan Standard Time (PKT) time zone, which is UTC+5."]],
    [r"tell me about the history of Pakistan", ["Pakistan was established in 1947 following the partition of British India. It has a rich history with influences from various civilizations."]],
    [r"what are some traditional Pakistani clothes", ["Traditional Pakistani clothes include Shalwar Kameez for both men and women, as well as traditional dresses for special occasions."]],
    [r"where can I buy Pakistani traditional clothes", ["You can buy traditional Pakistani clothes from local markets, boutiques, and online stores specializing in ethnic wear."]],
    [r"what are some popular Pakistani songs", ["Popular Pakistani songs include 'Dil Dil Pakistan', 'Jeevay Jeevay Pakistan', and tracks by artists like Atif Aslam and Ali Zafar."]],
    [r"who is the founder of Pakistan", ["The founder of Pakistan is Muhammad Ali Jinnah."]],
    [r"what is the population of Pakistan", ["The population of Pakistan is over 220 million people."]],
    [r"what are some famous Pakistani landmarks", ["Famous landmarks include the Badshahi Mosque, Lahore Fort, and the Faisal Mosque."]],
    [r"what is the weather like in Karachi", ["Karachi typically has a hot and humid climate, with milder temperatures in winter."]],
    [r"what is the education system like in Karachi", ["Karachi has a diverse education system with many well-known schools, colleges, and universities."]],
    [r"how can I contact customer support for a company in Pakistan", ["You can usually contact customer support through the company's website or customer service hotline."]],
    [r"what is the best time to visit Pakistan", ["The best time to visit Pakistan is from October to March when the weather is more pleasant."]],
    [r"what are some famous Pakistani movies", ["Famous Pakistani movies include 'Waar', 'Khuda Ke Liye', and 'Teefa in Trouble'."]],
    [r"how do I make traditional Pakistani tea", ["To make traditional Pakistani tea, you brew tea leaves with milk, sugar, and spices like cardamom and ginger."]],
    [r"where can I find Pakistani cuisine in my city", ["You can find Pakistani cuisine at local Pakistani restaurants or South Asian food outlets."]],
    [r"what are some popular sports in Pakistan", ["Popular sports in Pakistan include cricket, field hockey, and football."]],
    [r"what is the significance of Independence Day in Pakistan", ["Independence Day, celebrated on August 14th, marks the day Pakistan gained independence from British rule in 1947."]],
    [r"who are some famous Pakistani politicians", ["Some famous Pakistani politicians include Benazir Bhutto, Nawaz Sharif, and Imran Khan."]],
    [r"what is the education system like in Lahore", ["Lahore has a robust education system with many prestigious schools, colleges, and universities."]],
    [r"what are some traditional Pakistani dishes", ["Traditional dishes include Biryani, Nihari, Haleem, and Karahi."]],
    [r"what is the local currency exchange rate in Pakistan", ["The exchange rate varies, so you should check with a currency exchange service for current rates."]],
    [r"how can I apply for a job in Pakistan", ["You can apply for jobs through online job portals, company websites, and recruitment agencies."]],
    [r"what are some major events in Pakistan", ["Major events include political rallies, cultural festivals, and sports tournaments."]],
    [r"how do I find local events in Pakistan", ["You can find local events through social media, community boards, and event management websites."]],
    [r"what is the main mode of transportation in Pakistan", ["Common modes of transportation include cars, buses, rickshaws, and trains."]],
    [r"where can I find good shopping places in Pakistan", ["Good shopping places include local markets, malls, and online shopping platforms."]],
    [r"what are some popular Pakistani fashion brands", ["Popular fashion brands include Khaadi, Sana Safinaz, and Gul Ahmed."]],
    [r"how can I learn about Pakistani culture", ["You can learn about Pakistani culture through books, documentaries, cultural festivals, and local experiences."]]
]

def chat():
    print("Hi! I am a chatbot created by mubashir abbas .")
    chat = Chat(pairs, reflections)
    chat.converse()

# Initiate the conversation
if __name__ == "__main__":
    chat()
