import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By

D = "/html/body/div[1]/div/div[3]/div[1]/div[2]/main/div[1]/div[3]/div/div["
F = 1
G = "]"
H = "/ul[1]/div["
J = 1
A = 0
M = "/li/a/div[2]/div/h3"
J = str(J)
F =str(F)
K = 0
V = "window.scrollBy(0,"
Z = 150
ZZ = ")"
Z = str(Z)

cook = pickle.load(open(r"C:\Users\Long\he\sesison6\Cook.pkl","rb"))
driver = webdriver.Chrome()
driver.set_window_size(700,800)
driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")



try:
    while A < 1:
        ZZZ = V + Z + ZZ
        L = D + F + G + H + J + G + M
        MN =  driver.find_element(By.XPATH,L).text
        MN = str(MN)
        driver.execute_script("window.scrollBy(0,100)")
        AA = MN.rfind("Máy in")
        SS = MN.rfind("May in")
        DD = MN.rfind("may in")
        FF = MN.rfind("máy in")
        GG = MN.rfind("A3")
        HH = MN.rfind("a3")
        time.sleep(1)

        if AA >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                time.sleep(1)
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K + 2

        if SS >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                time.sleep(1)
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K + 2

        if DD >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                time.sleep(1)
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K + 2

        if FF >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                time.sleep(1)
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K + 2

        if GG >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                time.sleep(1)
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                time.sleep(1)
                K = 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K + 2

        if HH >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                time.sleep(1)
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K + 2

         

        else:
            print("Không có gì!")
            J = int(J)
            J = J + 1    
            J = str(J)  
        J = int(J)
        J = J + 1
        J = str(J)
            


except :
    A = A + 1
    F = int(F)
    F = F + 1
    F = str(F)
    while A < 2:
        L = D + F + G + H + J + G + M
        driver.execute_script("window.scrollBy(0,100)")
        MN =  driver.find_element(By.XPATH,L).text

        AA = MN.rfind("Máy in")
        AA = MN.rfind("Máy In")
        SS = MN.rfind("May in")
        DD = MN.rfind("may in")
        FF = MN.rfind("máy in")
        GG = MN.rfind("A3")
        HH = MN.rfind("a3")

    if AA >= 0 :
        if K < 1:
            driver.get("https://www.facebook.com/login")
            time.sleep(1)
            for cook in cook:
                driver.add_cookie(cook)
            driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
            time.sleep(2)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
            time.sleep(1)
            Z = int(Z)
            J = int(J)
            Z = Z * J
            Z = str(Z)
            J = str(J)
            driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
            K = 2
        elif K > 1:
            driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
            time.sleep(2)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
            time.sleep(1)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
            time.sleep(1)
            Z = int(Z)
            J = int(J)
            Z = Z * J
            Z = str(Z)
            J = str(J)
            driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
            K + 2

        if SS >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                time.sleep(1)
                for cook in cook:
                    driver.add_cookie(cook) 
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2


        if DD >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2

        if FF >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                for cook in cook:
                        driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2

        if GG >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2

        if HH >= 0 :
            if K < 1:
                driver.get("https://www.facebook.com/login")
                for cook in cook:
                    driver.add_cookie(cook)
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2
            elif K > 1:
                driver.get("https://www.facebook.com/people/Thuy-Pham/100001919203415")
                time.sleep(2)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").click()
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p").send_keys(MN)
                time.sleep(1)
                driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span[2]/div").click()
                time.sleep(1)
                Z = int(Z)
                J = int(J)
                Z = Z * J
                Z = str(Z)
                J = str(J)
                driver.get("https://www.chotot.com/mua-ban-do-dung-van-phong-cong-nong-nghiep-tp-ho-chi-minh?sp=4&f=p")
                K = K + 2
            else:
                J = int(J)
                J = J + 1
                J = str(J)
            J = int(J)
            J = J + 1
            J = str(J)
            
finally:          
    J = int(J)
    J = 1
    J = str(J)
    F = int(F)
    F = 1
    A = 1
    F = str (F)
    print(L)