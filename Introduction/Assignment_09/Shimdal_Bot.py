
import random
import telebot
import khayyam
from gtts import gTTS
import qrcode

bot = telebot.TeleBot("6956410178:AAHC_GoTsgYhwkWyXAHyjcZCRYzr4tfizzc", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"Dear {message.from_user.first_name};\nWelcome to Shimdal_bot")

@bot.message_handler(commands= ["game"])
def game(message):
    global bot_state
    global random_number
    markup = telebot.types.ReplyKeyboardMarkup(row_width= 1)
    button = telebot.types.KeyboardButton("/New_Game")
    markup.add(button)
    random_number = random.randint(1,100)
    bot.send_message(message.chat.id, "Please enter a number (0,100):" , reply_markup=markup)
    
    @bot.message_handler(func= lambda m:True)
    def guess_number (message):
        global random_number
        if int(message.text) < random_number:
            bot.send_message(message.chat.id, "Go Up", reply_markup= markup )
                
        elif int(message.text) > random_number:
            bot.send_message(message.chat.id, "Go Down", reply_markup= markup ) 
                
        elif int(message.text) == random_number:
            bot.send_message(message.chat.id, "You WIN", reply_markup= telebot.types.ReplyKeyboardRemove(selective=True))


@bot.message_handler(commands= ["age"])
def age(message):
    global bot_state
    user_age = bot.send_message(message.chat.id, "Please enter your date of birth in Hijri (y/m/d):")
    bot.register_next_step_handler(user_age, age_calculator)

def age_calculator(message):
        date_of_birth = (str(message.text)).split("/")
        differnce = khayyam.JalaliDatetime.now() - khayyam.JalaliDatetime(date_of_birth[0], date_of_birth[1], date_of_birth[2])
        year = differnce.days // 365
        differnce = differnce.days % 365
        month = differnce // 30
        day = (differnce % 30) -7
        bot.send_message(message.chat.id, "Your exact age is: "+ str(year) + " years and "+ str(month) + " months and "+ str(day) + " days.")


@bot.message_handler(commands= ["voice"])
def voice(message):
    global bot_state
    user_txt = bot.send_message(message.chat.id, "Please enter a sentence in English:")
    bot.register_next_step_handler(user_txt, voice_output)

def voice_output(message):
    audio = gTTS(text = message.text, lang = "en", slow = False)
    audio.save("voice.mp3")
    audio_file = open("voice.mp3", "rb")
    bot.send_voice(message.chat.id, audio_file)


@bot.message_handler(commands= ["max"])
def max(message):
    global bot_state
    user_numbers = bot.send_message(message.chat.id, "Please enter the list of numbers; separate the numbers with ',':")
    bot.register_next_step_handler(user_numbers, max_number)

def max_number(message):
    numbers = message.text.split(",")
    max = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > max:
            max = int(numbers[i])
    bot.send_message(message.chat.id, "The largest number is: " +str(max) )


@bot.message_handler(commands= ["argmax"])
def argmax(message):
    global bot_state
    user_numbers = bot.send_message(message.chat.id, "Please enter the list of numbers; separate the numbers with ',' :")
    bot.register_next_step_handler(user_numbers, index_max_number)

def index_max_number(message):
    numbers = message.text.split(",")
    max = 0
    index = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > max:
            max = int(numbers[i])
            index = i + 1
    bot.send_message(message.chat.id, "The index of the largest number is: "+ str(index))


@bot.message_handler(commands= ["qrcode"])
def QRcode(message):
    global bot_state
    user_text = bot.send_message(message.chat.id, "Please enter a string; Shimdal_Bot can create its Qrcode:")
    bot.register_next_step_handler(user_text, QR_maker)

def QR_maker(message):
    user_qrcode = qrcode.make(message.text)
    user_qrcode.save("QR.jpg")
    QR_file = open("QR.jpg", "rb")
    bot.send_photo(message.chat.id, QR_file)        

@bot.message_handler(commands=['help'])
def send_game(message):
	bot.send_message(message.chat.id,"You can use this commands:"
				                     "\n1. /start: The welcome message says"
									 "\n2. /game: You play the number guessing game"
									 "\n3. /age: It calculates your age"
									 "\n4. /voice: Converts text to sound"
									 "\n5. /max: Displays the largest number in the list"
									 "\n6. /argmax: Displays the index of largest number in the list"
									 "\n7. /qrcode: Converts text to Qrcode")
	
bot.infinity_polling()