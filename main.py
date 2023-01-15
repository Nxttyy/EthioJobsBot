import telebot
from scrapper import getLatestJobs

API_TOKEN = '5880195559:AAG_1dy2rThAiLFq5OZyfDqjyGHkQ87efl8'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Hi, send '/jobs' to get latest job opportunities")


# Handle '/jobs' and '/Jobs'
@bot.message_handler(commands=['Jobs', 'jobs'])
def send_welcome(message):

	jobs = getLatestJobs()

	for job in jobs:
		bot.send_message(message.chat.id, f'''Job-Title: { job["Job-Title"] }
												Company: { job["Company"] }
												Location: { job["Location"] }
												Date: { job["Date"] }
												Link: { job["Link"] }''')
		
bot.polling()
