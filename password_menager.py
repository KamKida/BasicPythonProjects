from time import sleep
from cryptography.fernet import Fernet

def load_key():
      file = open("key.key","rb")
      key = file.read()
      file.close()
      return key

def write_key():
      key = Fernet.generate_key()
      with open("key.key","wb") as key_file:
            key_file.write(key)





key = load_key() 
fer = Fernet(key)

def view():
      with open('password.txt', 'r') as f:
            for line in f.read():
                  data = line.rstrip()
                  user, passw = data.splitlines("/")
                  print("User: ", user,"| Password: ",fer.decrypt(passw.encode()).decode())

def add():
      name = input("Account Name: ")
      pwd = input("Password: ")
      with open('password.txt', 'a') as f:
            f.write(str(name +"/"+ fer.encrypt(pwd.encode()).decode() + "\n"))

while True:

    mode = input("Would you like to add new password or view existing ones (view, add)? Press 'q' to quit:  ").lower()

    if mode == "q":
        print("Login out")
        sleep(5)
        break 


    
    if mode == "view":
            view()
    elif mode == "add":
            add()
   
    else:
        print("Not a valid option , Try Again")
        continue