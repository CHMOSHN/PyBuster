"""
This file contains all of the important stuff that's crutial to run this code
Basically it's the whole freaking program dude! wtf do u want to do with that?
Want to delete it? I will be sad :(
Want to modify? Pffft. Go through this spaghetti code. I was drunk writing this
"""

#Imports
from requests import get
from colorama import Fore
from functools import lru_cache
from time import sleep
from random import randrange
import decorations

#Search function
@lru_cache
def search(url: str, txt_file: str) -> None:
    
    #Reading txt file
    with open(txt_file) as f:
        read = f.readlines()
    
    #This part of code is searching through the URL via requests.
    #! WARNING! MODIFY THIS PART IF U'RE USING IT FOR BUGBOUNTY!(Stupid idea)
    
    for line in read:
        r = get(fr"{url}{line}")
        
        if r.status_code == 200:
            print(Fore.GREEN + f"Found {line}")
        elif r.status_code == 404:
            print(Fore.RED + f"{url}{line} not found")
        elif r.status_code == 403:
            print(Fore.BLUE + f"{url}{line} FORBIDDEN!")
        else:
            print(Fore.CYAN + f"Something went wrong with {url}{line}\nError code:{r.status_code}")
        
        decorations.loading() #! <- Loading animation. DELETE THIS IF U DELETED decorations.py!
        sleep(randrange(6, 8))

#Main function            
def main() -> None:
    try:
        print(Fore.LIGHTGREEN_EX + 
            r"""
                 /$$$$$$$            /$$$$$$$                        /$$                         
                | $$__  $$          | $$__  $$                      | $$                         
                | $$  \ $$ /$$   /$$| $$  \ $$ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$  
                | $$$$$$$/| $$  | $$| $$$$$$$ | $$  | $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$ 
                | $$____/ | $$  | $$| $$__  $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/ 
                | $$      | $$  | $$| $$  \ $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$       
                | $$      |  $$$$$$$| $$$$$$$/|  $$$$$$/ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$       
                |__/       \____  $$|_______/  \______/ |_______/    \___/   \_______/|__/       
                            /$$  | $$|                                                            
                            |  $$$$$$/                                                            
                            \______/                                                              """ + Fore.RESET)
        while True:
            url: str = input("Enter your URL: ")
            
            if url.startswith("https://") or url.startswith("http://"):
                if "youtube" in url:
                    print(Fore.RED + "WARNING! You can find a dude with a nickname that's can possibly be in your txt!!!" + Fore.RESET)
                else:
                    print(Fore.GREEN + "All okay!" + Fore.RESET)
                
            else:
                print(Fore.RED + "NOT A URL!")
                continue
            
            txt_file: str = input("Enter txt file that will be used for search: ")
            
            if txt_file.endswith(".txt"):
                print(Fore.GREEN + "All okay!" + Fore.RESET)
                break
            else:
                print(Fore.RED + "NOT A TXT!")
                
            
        search(url=url, txt_file=txt_file)
    except KeyboardInterrupt:
        print(Fore.GREEN + "\nProgramm succesfully stoped!" + Fore.RESET)
        
if __name__ == '__main__':
    main()