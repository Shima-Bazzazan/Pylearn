
import gtts
import os

def read_from_database():
    
    global words_bank
    file = open("G:\python_project\pylearn7\sessions\session8\words.txt", "r")
    temp = file.read().split("\n")
    words_bank = []
    for i in range (0 , len(temp),2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)
    file.close()


def translate_english_to_persian():    
    user_text= input("Please enter english text: ")
    user_words= user_text.split(".")
    output=""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output= output + word["fa"] + " "
                break
        else:
            output= output + user_word +" "
    
    output_voice=gtts.gTTS(output, lang="ur", slow=False)
    output_voice.save("sessions/session8/output_voice.mp3")
    print()
    print("Translate your text is:",output)  


def translate_persian_to_english():    
    user_text= input("Please enter persian (Finglish) text: ")
    user_words= user_text.split(".")
    output=""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output= output + word["en"] + " "
                break
        else:
            output= output + user_word + " "
    
    output_voice=gtts.gTTS(output, lang="ar", slow=False)
    output_voice.save("sessions/session8/output_voice.mp3")
    print()
    print("Translate your text is:",output)  

def add_word( ) :
        en_word = input("Please enter new English word: ")
        fa_word = input("Please enter Persian (Finglish) meaning: ")
        new_word = {"en" : en_word , "fa" : fa_word}
        words_bank.append(new_word)
        f = open("G:\python_project\pylearn7\sessions\session8\words.txt" , "a")
        f.write("\n")
        f.write(en_word + "\n")
        f.write(fa_word)
        f.close()

def show_menu():
    print()
    print("Welcome to my translate")
    print("1. Translate English To Persian")
    print("2. Translate Persian To English")
    print("3. Add a New word to Database")
    print("4. Exit")
    print()


read_from_database()

file_path = "G:\python_project\pylearn7\sessions\session8\words.txt"
file_exist = os.path.isfile(file_path)

if file_exist == True :
    while True:
        show_menu()
        user_choice= int(input("Please enter your choice: "))

        if user_choice==1:
            translate_english_to_persian()
        elif user_choice==2:
            translate_persian_to_english()
        elif user_choice==3:
            add_word()
        elif user_choice==4:
            exit(0)
else:
    print("The File didnt exist in the path")

 