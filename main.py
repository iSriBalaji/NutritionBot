# Deploy - https://www.youtube.com/watch?v=-yWuLRJhoNI
# Code - https://www.youtube.com/watch?v=NwBWW8cNCP4 - CS Dojo
# pip install pyTelegramBotAPI

import os
import telebot
# import pip
# pip.main(['install','pyTelegramBotAPI'])
from nltk.tokenize import word_tokenize
question_words = ["what", "why", "when", "where", 
             "name", "is", "how", "do", "does", 
             "which", "are", "could", "would", 
             "should", "has", "have", "whom", "whose", "don't"]

# BOT_KEY = os.getenv('API_KEY')
BOT_KEY = '5510201179:AAGQADd5qbdC4868UxjEsFBsY1ePxY2Ypvs'
baju = telebot.TeleBot(BOT_KEY)

@baju.message_handler(commands=['Greet'])
def greet(message):
    baju.reply_to(message, "Hey! Hows it going?")

@baju.message_handler(commands=['Hello'])
def greet(message):
    baju.send_message(message.chat.id, "Hello Friend, I am Baju!\nYour Personal Nutrition Assistant")

def detect_question(message):
    question = message.text.lower()
    question = word_tokenize(question)
    if any(x in question[0] for x in question_words):
        return True
    else:
        return False

@baju.message_handler(func=detect_question)
def query(message):
    detect = detect_question(message)
    if detect:
        baju.send_message(message.chat.id, "Your query will be answered soon...\nRequire API Integration")
    else:
        baju.send_message(message.chat.id, "This is not a valid question")

def others(message):
    question = message.text.lower()
    question = word_tokenize(question)
    if not any(x in question[0] for x in question_words):
        return True
    else:
        return False

@baju.message_handler(func=others)
def other_query(message):
    detect = detect_question(message)
    if detect:
        baju.send_message(message.chat.id, "This is not a valid question")
    else:
        baju.send_message(message.chat.id, "Sorry, No information is available. This is not a valid question")

baju.polling()