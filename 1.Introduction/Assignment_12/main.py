
from Actor_class import Actor
from Clip_class import Clip
from Media_class import Media
from Film_class import Film
from Series_class import Series 
from Documentary_class import Documentary


def show_menu():
    print("1. Add Media")
    print("2. Edit Media")
    print("3. Delete Media")
    print("4. Search")
    print("5. Download Media")
    print("6. Show Media")
    print("7. Exit")

Video = []

def read_from_database():
    file = open('G:\python_project\pylearn7\sessions\Assignment1\mordam.py\data.txt','r')

    rows = file.read().split("\n")
    for i in range(len(rows)):
        info = rows[i].split(",")
        if info[0] == "film":
            actors = info[6].split("-")
            casts= []
            for j in range(len(actors)):
                cast = actors[j].split(" ") 
                actor =Actor(cast[0],cast[1])
                casts.append(actor)
            film = Film(info[0],info[1],info[2],info[3],info[4],info[5],casts)
            Video.append(film)
        elif info[0] == "serial":
            actors = info[7].split("-")
            casts = []
            for j in range(len(actors)):
                cast = actors[j].split(" ") 
                actor = Actor(cast[0],cast[1])
                casts.append(actor)
            series = Series(info[0],info[1],info[2],info[3],info[4],info[5],info[6],casts,info[8])
            Video.append(series)
        elif info[0] == "documentary":
            actors = info[7].split("-")
            casts = []
            for j in range(len(actors)):
                cast = actors[j].split(" ") 
                actor = Actor(cast[0],cast[1])
                casts.append(actor)
            documentary = Documentary(info[0],info[1],info[2],info[3],info[4],info[5],casts,casts,info[8])
            Video.append(documentary)
        elif info[0] == "clip":
            actors = info[6].split("-")
            casts = []
            for j in range(len(actors)):
                cast = actors[j].split(" ") 
                actor = Actor(cast[0],cast[1])
                casts.append(actor)
            clip = Clip(info[0],info[1],info[2],info[3],info[4],info[5],casts)
            Video.append(clip)
    file.close()

def add_media():
    actors=[]
    type_media = input("Please enter Media's type: ")
    if type_media.lower() == "film":
        name_media = input("Please enter the Name of Media: ")
        director_media = input("Please enter the name of Director: ")
        imdb_score_media = float(input("Please enter Media's IMDB Score: "))
        url_media = input("Please enter Media's Url (Uniform Resource Locator): ")
        duration_media = int(input("Please enter Media's Duration: "))
        actor_media= input("Please enter the name and lastname of the actor: ")
        actors.append(actor_media)
        while True:
            user_choice = input("Do you want to add an actor? (y/n) ")
            if user_choice == "y":
                actor_media = input("Please enter the name and lastname of the actor: ")
                actors.append(actor_media)
            elif user_choice == "n":
                break
        Video.append(Film(type_media, name_media, director_media, imdb_score_media, url_media, duration_media, actors))
        print("Added successfully")

    elif type_media.lower() == "serial":
        name_media = input("Please enter the Name of Media: ")
        director_media = input("Please enter the name of Director: ")
        imdb_score_media =float(input("Please enter Media's IMDB Score: "))
        url_media = input("Please enter Media's Url (Uniform Resource Locator): ")
        duration_media = int(input("Please enter the name and lastname of the actor: "))
        actors.append(actor_media)
        while True:
            user_choice = input("Do you want to add an actor? (y/n) ")
            if user_choice == "y":
                actor_media = input("Please enter the name and lastname of the actor: ")
                actors.append(actor_media)
            elif user_choice == "n":
                break
        part_media = int(input("Please enter Media's Part: "))
        season_media = int(input("Please enter Media's Season: "))
        Video.append(Series(type_media, name_media, director_media, imdb_score_media, url_media, duration_media , part_media, actors, season_media))
        print("Added successfully")
    
    elif type_media.lower() == "documentary":
        name_media = input("Please enter the Name of Media: ")
        director_media = input("Please enter the name of Director: ")
        imdb_score_media =float(input("Please enter Media's IMDB Score: "))
        url_media = input("Please enter Media's Url (Uniform Resource Locator): ")
        duration_media = int(input("Please enter the name and lastname of the actor: "))
        actors.append(actor_media)
        while True:
            user_choice = input("Do you want to add an actor? (y/n) ")
            if user_choice == "y":
                actor_media = input("Please enter the name and lastname of the actor: ")
                actors.append(actor_media)
            elif user_choice == "n":
                break
        part_media = int(input("Please enter Media's Part: "))
        season_media = int(input("Please enter Media's Season: "))
        Video.append(Documentary(type_media, name_media, director_media, imdb_score_media, url_media, duration_media, part_media, actors, season_media))
        print("Added successfully")
    
    elif type_media.lower() == "clip":
        name_media = input("Please enter the Name of Media: ")
        director_media = input("Please enter the name of Director: ")
        imdb_score_media =float(input("Please enter Media's IMDB Score: "))
        url_media = input("Please enter Media's Url (Uniform Resource Locator): ")
        duration_media = int(input("Please enter the name and lastname of the actor: "))
        actors.append(actor_media)
        while True:
            user_choice = input("Do you want to add an actor? (y/n) ")
            if user_choice == "y":
                actor_media = input("Please enter the name and lastname of the actor: ")
                actors.append(actor_media)
            elif user_choice == "n":
                break
        Video.append(Clip(type_media, name_media, director_media, imdb_score_media, url_media, duration_media, actors))
        print("Added successfully")
    else:
        print("Incorrect value!\n")


def edit_media():
    name_media = input("Please enter the name of Media: ")
    for i in range(len(Video)):
        if Video[i].name == name_media:
            while True:
                choice = int(input("Please choose from edit menue:\n1. type\n2. Director name\n3.Imdb Score\n4. Url\n5. Duration\n6. Exit\n"))

                if choice == 1:
                    Video[i].type = input("Please enter new type: ")
                elif choice == 2:
                    Video[i].director = input(" Please enter new Director name:")
                elif choice == 3:
                    Video[i].score = float(input(" Please enter new IMDB Score: "))
                elif choice == 4:
                    Video[i].link = input("Please enter new Url: ")
                elif choice == 5:
                    Video[i].duration = int(input("Please enter new Duration: "))
                elif choice == 6:
                    break
        else:
            print("This Media dose not exist!")
            
def delete_media():
    name_media = input("Please enter the name of Media: ")
    for i in range(len(Video)):
        if Video[i].name == name_media:
            Video.pop(i)
            print("Media Deleted!")
            break       

def search_media():
    result = []
    min_time = int(input("Please enter minimum time: "))
    max_time = int(input("please enter maximum time: "))
    for i in range(len(Video)):
        if min_time < int(Video[i].duration) < max_time and Video[i].type == "film":
            result.append(Video[i].name)

    for j in range(len(result)):
        print(result[j])

def download():
    name_media = input("Please enter the name of Media: ")
    for i in range(len(Video)):
        if Video[i].name == name_media:
            Video[i].download()
            print("Downloaded")

def write_to_database():
    file= open('G:\python_project\pylearn7\sessions\Assignment1\mordam.py\data.txt','w')
    for i in range(len(Video)):
        if i < (len(Video)-1):
            if Video[i].type== "film":
                row = Video[i].type +','+ Video[i].name +','+ Video[i].director +','+ str(Video[i].imdb_score).format() +','+Video[i].url +','+ str(Video[i].duration).format() + '\n'
                file.write(row)
        if i == (len(Video)-1):
            row = Video[i].type +','+ Video[i].name +','+ Video[i].director +','+ str(Video[i].imdb_score).format() +','+Video[i].url +','+ str(Video[i].duration).format()  
            file.write(row)  
        
    file.close()     

def show_media():
    for media in Video:
        media.show_info()


print("\nWelcome to Media store\n")
print("Loading...")
read_from_database()
print("Data Loaded\n")

while True:
    show_menu()
    user_choice = int(input("Please enter your choice: "))

    if user_choice == 1:
        add_media()
    elif user_choice == 2:
        edit_media()
    elif user_choice == 3:
        delete_media()
    elif user_choice == 4:
        search_media()
    elif user_choice == 5:
        download()
    elif user_choice == 6:
        show_media()
    elif user_choice == 7:
        write_to_database()
        exit(0)
    else:
        print("Please enter a number betwwen 1 to 7")