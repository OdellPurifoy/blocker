import time
from datetime import datetime as dt

host_path = '/etc/hosts'
temp_path = 'hosts'
redirect = '127.0.0.1'
website_blacklist = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'instagram.com', 'www.tmz.com', 'tmz.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_blacklist:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+'\n')
    else:
        print("Fun hours...")
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_blacklist):
                    file.write(line)
            file.truncate()


    time.sleep(5)
