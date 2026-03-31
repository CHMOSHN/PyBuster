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
from socket import gethostbyaddr
from ipaddress import ip_address
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
        
        if url.startswith("https://"):
            r = get(fr"{url}/{line}")
        else:
            r = get(fr"https://{url}/{line}")
        
        if r.status_code == 200:
            print(Fore.GREEN + fr"Found https://{url}/{line}")
        elif r.status_code == 404:
            print(Fore.RED + fr"https://{url}/{line} not found")
        elif r.status_code == 403:
            print(Fore.BLUE + fr"https://{url}/{line} FORBIDDEN!")
        else:
            print(Fore.CYAN + f"Something went wrong with {url}{line}\nError code:{r.status_code}")
        
        decorations.loading() #! <- Loading animation. DELETE THIS IF U DELETED decorations.py!
        sleep(randrange(6, 8))

#Function that validates IP address that user had typed in.
def validate_ip(ip: str) -> bool:
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False

#Main function            
def main() -> None:
    try:
        decorations.logo() # <- Moved this massive logo to a deco file with a bit of randomizing.
        while True:
            url: str = input("Enter your URL or IP address: ")
            
            if validate_ip(url):
                url = gethostbyaddr(url)[0]
            else:
                pass
                
            if any(url.endswith(ext) for ext in decorations.container.domain_extensions()):
                if "youtube" in url:
                    print(Fore.RED + "WARNING! You can find a dude with a nickname that's can possibly be in your txt!!!" + Fore.RESET)
                else:
                    print(Fore.GREEN + "All okay!" + Fore.RESET)        
            else:
                print(Fore.RED + "NOT A URL OR A KNOWN DOMAIN!")
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