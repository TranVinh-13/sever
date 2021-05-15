import requests,os,re,sys,threading,os.path
from colorama import  Fore
from time import sleep
do = Fore.RED
vang = Fore.YELLOW
xanh = Fore.GREEN
blue = Fore.BLUE
magenta = Fore.MAGENTA
trang = Fore.WHITE
mau = Fore.LIGHTCYAN_EX
import random
logo = xanh+f"""
 /$$    /$$ /$$$$$$ /$$   /$$ /$$   /$$ /$$   /$$      
| $$   | $$|_  $$_/| $$$ | $$| $$  | $$| $$  / $$      
| $$   | $$  | $$  | $$$$| $$| $$  | $$|  $$/ $$/      
|  $$ / $$/  | $$  | $$ $$ $$| $$$$$$$$ \  $$$$/       
 \  $$ $$/   | $$  | $$  $$$$| $$__  $$  >$$  $$       
  \  $$$/    | $$  | $$\  $$$| $$  | $$ /$$/\  $$      
   \  $/    /$$$$$$| $$ \  $$| $$  | $$| $$  \ $$      
    \_/    |______/|__/  \__/|__/  |__/|__/  |__/      
                         
                         {do}Telegram:@vinhZ007    
                         {magenta}Script: Lọc Mail/Check Live/Die    
"""
os.system("clear")
print(logo)
print(f"""
{xanh}[1] {vang}Check Live Die Yahoo
{xanh}[2] {vang}Check Live Die Facebook
{xanh}[3] {vang}Random Mail """)
chon = input(f"{magenta}Chọn:")
if(chon=="1"):
  os.system('clear')
  print(logo)
  print(vang+"Mail Chưa Tạo Yahoo Sẽ Được Lưu Vào File maildie.txt")
  file = input(xanh+"Nhập Tên File Chứa list mail:")
  try:
    f = open(file,"r") 
  except:
    print(do+"Không Tìm Thấy file ")
    exit(0)
  email = f.readlines()
  
  def check(email):
      try:
        a = requests.get(f"https://vinh2007.000webhostapp.com/yahoo.php?email={email}")
        return a.json()
      except requests.exceptions.ConnectionError:
        print(do+"Vui Lòng Tắt Vpn Hoặc Kiểm Tra Mạng")
        exit()
      
      
  die = []
  live = []
  
  def chiamang(thread_step):
    for i in range(thread_step,len(email),thread_count):
      run = check(email[i])
      if run['code'] == '200':
        msg = (xanh + email[i] +do+"|"+xanh+ "Mail Chưa Đăng Ký").replace("\n"," ")
        print(msg)
        open("maildie.txt","a").write(email[i])
        live.append(email[i])
      elif run['code'] == '403':
        
        msg = (xanh + email[i] +do+"|"+xanh+ "Mail Đã Đăng Ký").replace("\n"," ")
        print(msg)
        die.append(email[i])
      if i == len(email):
        print(f"{xanh}Tổng Số Mail Live/Die:{len(live)}/{len(die)}")
  thread_count = int(input('Nhập Số Luồng:'))
  for k in range(thread_count):
    newt = threading.Thread(target=chiamang,args=(k,))
    newt.start()
elif chon=="2":
  os.system('clear')
  print(logo)
  print(vang+"Mail Đã Tạo Facebook Sẽ Được Lưu Vào File fbdie.txt")
  file = input(xanh+"Nhập Tên File Chứa list mail:")
  try:
    f = open(file,"r") 
  except:
    print(do+"Không Tìm Thấy file ")
    exit(0)
  email = f.readlines()


      
      
  die = []
  live = []
  
  def chiamang(thread_step):
    for i in range(thread_step,len(email),thread_count):
      try:
        ua = requests.get('https://gist.githubusercontent.com/pzb/b4b6f57144aea7827ae4/raw/cf847b76a142955b1410c8bcef3aabe221a63db1/user-agents.txt').text.split('\n')
      except requests.exceptions.ConnectionError:
        print(do+"Vui Lòng Tắt Vpn Hoặc Kiểm Tra Mạng")
        exit()
      try:
        run = requests.get(f"https://vinh2007.000webhostapp.com/vaildfb.php?email={email[i]}",headers={'user-agent':random.choice(ua)}).text
      except requests.exceptions.ConnectionError:
        print(do+"Vui Lòng Tắt Vpn Hoặc Kiểm Tra Mạng")
        exit()
      if "VAILED" in run:
        msg = (xanh + email[i] +do+"|"+xanh+ "Mail Đã Đăng Ký Facebook").replace("\n"," ")
        print(msg)
        open("fbdie.txt","a").write(email[i])
        live.append(email[i])
      elif "INVAILD" in run :
        
        msg = (xanh + email[i] +do+"|"+xanh+ "Mail Chưa Đăng Ký Facebook").replace("\n"," ")
        print(msg)
        die.append(email[i])
      elif "LOCKED" in run:
        msg = (xanh + email[i] +do+"|"+xanh+ "Acc LOCKED").replace("\n"," ")
        print(msg)
      elif "ERROR" in run:
        print(do+"Bạn Đã Bị Facebook Chặn Bui Lòng Quay Lại Sau")
        exit()
      if len(live)+len(die) == len(email):
        print(f"{xanh}Tổng Số Mail Live/Die:{len(live)}/{len(die)}")
  thread_count = int(input('Nhập Số Luồng:'))
  for k in range(thread_count):
    try:
      newt = threading.Thread(target=chiamang,args=(k,))
      newt.start()
    except Exception as e:
      print(f"{do} ĐÃ XẢY RA SỰ CỐ")
      exit()
   
   
elif chon=="3":
  os.system("clear")
  print(logo)
  ten = input(xanh+"Nhập Tên Cần Check: ")
  s1 = int(input(xanh+"Nhập Số Đầu:"))
  s2 = int(input(xanh+"Nhập Số Cuối"))
  type_mail = input(xanh+"Nhập Loại Mail(@+loạimail.com:")
  file_save = input(xanh+"Nhập File Lưu Mail:"+trang)
  for i in range(s1,s2+1):
    email= ten+str(i)+type_mail
    print(xanh+email)
    open(file_save,"a").write(email+"\n")