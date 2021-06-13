# TrueMoney-Wallet-Gift-API
เป็นตัวรับข้อมูลและทำการเก็บเงินยันโอนเงินเข้าจาก TrueWallet Gift (ซองของขวัญทรูวอลเลท) เขียนโดยภาษา Python3

**ภาษาโปรแกรมที่พัฒนา:** `Python3`

**ข้อมูลข้างใน:**
    
`มี Comment บอกหลักการทำงานต่างๆ หากใครสนใจจะศึกษาหลักการทำงานของมัน วิธีรับเงิน หรือเช็คข้อมูลต่างๆ`
    
    การทำงานระบบ:
            ระบบ จะทำการติดต่อ โต้ตอบส่งข้อมูลเข้าออก
            ระบบ จะเก็บข้อมูลและแปลงข้อมูลต่างๆในตัวแปรๆหนึ่ง
            ระบบ จะเช็ตและแจ้งเตือนว่า กรอก URL ซองของขวัญถูกหรือผิด
                 และ ที่กรอก เป็นของ TrueWallet Gift ถูกต้อง หรือไม่   
            ระบบ จะรับข้อมูลของซองและนำมาแสดงผลต่างๆเช่น
                 เจ้าของซอง, จำนวนเงินในซองทั้งหมด, จำนวนเงินในซองจำนวนเต็ม
                 ข้อมูลซอง, ซองนี้ใช้ได้กี่ครั้ง, ซองนี้ถูกใช้ไปแล้วกี่ครั้ง, โค้ดรหัสของอั่งเป่า 
            ระบบ จะทำการโอนซองเข้าเบอร์ผู้รับทันทีหลังเมื่อทุกอย่างพร้อม
                 และทำการรายงานว่าโอนสำเร็จหรือผิดพลาด

**โมดูลที่ ต้องการ:**

    requests, validators, json, threading


**ข้อมูลสิทธ์การนำไปใช้งาน:**

    เงื่อนไขการนำไปใช้งาน:

    ห้ามนำไป จำหน่าย หากไม่ได้รับอนุญาต จากผู้พัฒนา
    อนุญาตให้นำไปดัดแปลงและเอาไปใช้ในงานส่วนบุคคลได้และการศึกษา
    หากจะนำไปจำหน่ายต่อ ต้องติดต่ออย่างชัดเจน กับผู้พัฒนา เพื่อรอรับ การอนุญาต และ ผู้พัฒนาจะกำหนดราคาสำหรับผู้ที่ได้รับอนุญาตในการจำหน่าย
    หากได้รับอนุญาต ให้นำไปจำหน่ายจะต้องห้ามจำหน่ายเกินราคาที่ผู้พัฒนาตกลงกันไว้

    การละเมิดลิขสิทธิ์มีโทษทางอาญาทั้งจำคุกและโทษปรับแล้วแต่กรณี และเจ้าของลิขสิทธิ์
