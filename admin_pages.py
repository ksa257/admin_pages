import urllib.request


print("""
                                _       _       
               _               | |     (_)      
  ____ _____ _| |_    _____  __| |____  _ ____  
 / _  | ___ (_   _)  (____ |/ _  |    \| |  _ \ 
( (_| | ____| | |_   / ___ ( (_| | | | | | | | |
 \___ |_____)  \__)  \_____|\____|_|_|_|_|_| |_|
(_____| cyber_security 
        Ahmed_ALrehilei
        Ethical_hacking
        V1.0                                        

get Domain Name https url+/
---------------------------
ex:
URL: https://google.com/
    
DONE 
""")

def admin_page(url):
    try:
        url_open = urllib.request.urlopen(url)
        adminlist = open("admin2.txt", "r")
        for x in adminlist:
            x = x.rstrip("\n",)
            Curl = url + "" +x
            try:
                url_open = urllib.request.urlopen(Curl)
                print(Curl+ "\nFOUND pages![+]\n")
            except urllib.error.HTTPError as msg:
                print(Curl+ "\nNOT FOUND [-]\n")
                print(msg)
    except urllib.error.URLError as msg:
        print(url)
        print(msg)
admin_page(input("\nGET URL Name:"))
