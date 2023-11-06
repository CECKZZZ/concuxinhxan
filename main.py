import requests
import random
import time
import os
from colorama import Fore

print("===========================================")
print('Spam Discord - Diminuto - Xóm Chùa With Love')
print("===========================================\n")

time.sleep(1)

channel_id = input("Nhập ID kênh: ")
waktu1 = int(input("Đặt thời gian gui tin nhắn: "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("noidung.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(words).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.YELLOW + "Sent message: Thanh Cong")
        #print(Fore.YELLOW + payload['content'])
        time.sleep(waktu1)

       # response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

