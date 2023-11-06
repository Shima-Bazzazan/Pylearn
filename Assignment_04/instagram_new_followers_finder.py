
import getpass
import instaloader

username = input("Username: ")
password = getpass.getpass ("Password: ")
selective_username = input("\nThe username of your choice: ")

load = instaloader.Instaloader()
load.login(username, password)
profile = instaloader.Profile.from_username(load.context, selective_username)

old_followers = []

file = open("Followers.txt", "r")
for line in file:
    old_followers.append(line.strip())
file.close()

new_followers = []

for follower in profile.get_followers():
    new_followers.append(follower.username)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

file = open("Followers.txt", "w")
for new_follower in new_followers:
    file.write(new_follower + "\n")
file.close()