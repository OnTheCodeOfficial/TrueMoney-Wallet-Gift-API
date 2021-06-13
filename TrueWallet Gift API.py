# Code by Michael
# Aka. OnTheCode Official

import requests, json, threading, os, validators
from time import sleep

os.system('cls') #ล้างเทอร์มินัล


#SETTING
reciver_phone_number = '0629401996' #เบอร์ผู้รับเงิน


#INPUT
url = input('True Wallet Gift URL: ') #อินพุทที่รับกรอกลิ้งค์ซองของขวัญทรูวอลเลท



print('\n') #แสดงเ้นช่องเพื่อไม่ให้ข้อความขึ้นซ้อนกัน


url_valid_check=validators.url(url)  #เช็คว่า ลิ้งค์ซองของขวัญมันเป็น URL ไหม
if url_valid_check is False:
    print('คุณกรอก URL ผิดพลาดกรุณาเช็คใหม่ ต้องเป็น URL เท่านั้น') #แสดงผลว่า ลิ้งค์ยูอาร์แอล ที่กรอกนั้นผิดพลาดให้ไปเช็คใหม่ เพราะมันไม่ใช่ URL

elif url_valid_check is True: #หาก URL ถูกต้อง


    #----------------------------------------------------------ตัวเชคข้อมูลซองว่าที่ให้มาเป็นซองของ TrueWallet Gift หรือไม่-------------------------------------------------------


    voucher_standard_link_check = 'https://gift.truemoney.com/campaign/?v='
    if voucher_standard_link_check not in url:
        print('''
        ลิ้งค์ที่ให้ไม่ใช่ลิ้งค์ซองของขวัญที่ถูกต้อง ต้องนำหน้าด้วย https://gift.truemoney.com/campaign/?v=
        ละตามด้วย รหัสซอง หลัง ?v= ตัวอย่าง aFlfkeT9zan8Ej7Wed จะเป็นรหัสหลังซอง ของ ลิ้งค์ที่ถูกต้อง
        โดย มาจาก https://gift.truemoney.com/campaign/?v=aFlfkeT9zan8Ej7Wed
        ''')                                                                        #แจ้งเตือนว่าลิ้งค์ซองที่ให้มาไม่ใช่เป็นลิ้งค์ซองของขวัญทรูวอลเลท หรือ ให้มาผิดพลาด

    elif voucher_standard_link_check in url:
        print('พบเจอลิ้งค์ ซองของขวัญ ของ TrueWallet แล้ว')         #แจ้งเตือนว่าลิ้งค์ซองที่ให้มาถูกต้องแล้วเป็นลิ้งค์ซองของขวัญทรูวอลเลท

        request_status_code = requests.get(url).status_code #รับรหัสการโต้ตอบ

        if request_status_code != 200:
            print('ล้มเหลว ซองไม่พบเจอ') #หากการตอบสนองอื่นๆ


        elif request_status_code == 200: #หากโต้ตอบสำเร็จ


            #---------------------------------------------ตัวแปลงลิ้งค์จากซองที่่ใช้กรอกเป็นซองที่ระบบทำการส่งคำขอและตอบสนองเพื่อรับข้อมูล---------------------------------------


            truewallet_gift_voucher_code = (url.split("https://gift.truemoney.com/campaign/?v=",1)[1]) 
            url = f'https://gift.truemoney.com/campaign/vouchers/{truewallet_gift_voucher_code}/verify?mobile={reciver_phone_number}'




            #--------------------------------------------------ตัวรับข้อมูลการตอบสนองของ URL ซองที่ดัดแปลงสำหรับคำขอไป-------------------------------------------------


            r = requests.get(url).json()

            print(type(r))
            print(r,'\n')

            json_str = json.dumps(r)
            resp = json.loads(json_str)  #แปลงชนิดข้อมูลตอบสนองและเก็บข้อมูลการตอบสนองต่างๆ



            #--------------------------------------------------ตัวแปรที่เก็บข้อมูลซอง TrueWallet gift ที่ตอบกลับจากคำขอ-------------------------------------------------



            truewallet_gift_owner = (resp['data']['owner_profile']['full_name'])
            truewallet_gift_message = (resp['status']['message'])
            truewallet_gift_amount = (resp['data']['voucher']['amount_baht'])
            truewallet_gift_status = (resp['data']['voucher']['status'])
            truewallet_gift_redeemed = (resp['data']['voucher']['redeemed'])
            truewallet_gift_redeemed_available = (resp['data']['voucher']['available'])
            truewallet_gift_url = (resp['data']['voucher']['link'])
            truewallet_gift_owner = truewallet_gift_owner.replace(' ***','')
            truewallet_gift_owner = truewallet_gift_owner.replace(' ','')

            truewallet_gift_amount_int = int(float(truewallet_gift_amount))



            #------------------------------------------------------ตัวแสดงผลข้อมูลของลิ้งค์ซอง TrueWallet gift-------------------------------------------------------



            print(f'เจ้าของซอง : {truewallet_gift_owner}')
            print(f'จำนวนเงินในซอง ทั้งหมด : {truewallet_gift_amount} บาท')
            print(f'จำนวนเงินในซอง จำนวนเต็ม : {truewallet_gift_amount_int} บาท')
            print(f'ข้อมูลซอง : {truewallet_gift_message}')
            print(f'ลิ้งค์ซอง : {truewallet_gift_url}')
            print(f'สถานะของลิ้งค์ซอง : {truewallet_gift_status}')
            print(f'ซองนี้ถูกใช้ไปแล้ว : {truewallet_gift_redeemed} ครั้ง')
            print(f'ซองนี้ใช้ได้ : {truewallet_gift_redeemed_available} ครั้ง\n')

            if truewallet_gift_redeemed_available == 0 or truewallet_gift_message == 'Voucher ticket is out of stock':
                print('ซองที่คุณกรอกมันหมดแล้วระบบใช้ไม่ได้')
            elif truewallet_gift_redeemed_available > 1:
                print('ซองนี้ใช้ได้มากกว่า 1 คน')
            elif truewallet_gift_redeemed_available == 1:
                print('ซองนี้รับได้คนเดียว')

                if truewallet_gift_status == 'active': #หากซองนี้ใช้ได้
                    if truewallet_gift_redeemed >= 1:
                        print(f'ซองนี้ถูกใช้ไปแล้ว {truewallet_gift_redeemed} ครั้ง')
                    elif truewallet_gift_redeemed == 0:
                        print('ซองนี้ยังไม่ผ่านการใช้งานสักครั้ง')



            #-------------------------------------------------------ตัวรับโอนเงินจากซองเข้าไปเบอร์ที่กรอกไว้ข้างบนสุด-------------------------------------------------------



            print('\nระบบกำลังทำการ รับเงินเข้า')

            payload = {
                "Host": "gift.truemoney.com",
                "Content-Length": "59",
                "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="90"',
                "Accept": "application/json",
                "Sec-Ch-Ua-Mobile": "?0",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                "Content-Type": "application/json",
                "Origin": "https://gift.truemoney.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": f"https://gift.truemoney.com/campaign/?v={truewallet_gift_voucher_code}",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Connection": "close"
        }

            get_url = (f"https://gift.truemoney.com/campaign/vouchers/{truewallet_gift_url}/redeem")
            data = {"mobile":f"{reciver_phone_number}","voucher_hash":f"{truewallet_gift_url}"}
            r = requests.post(get_url, data=json.dumps(data), headers=payload)
            print(r.text)
            if r.status_code != 200:
                print("โอนไม่สำเร็จ")
            elif r.status_code == 200:
                print(f'\nรับซองและโอนเข้าบัญชี Truewallet เบอร์ {reciver_phone_number} สำเร็จแล้ว')

            else:
                pass #อยากทำไรก็ทำ
