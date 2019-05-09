print("YAHOO MANUEL DOMAİN SORGULAYICI - BLACK TURTLE\n ")

print("HATIRLATMA : 200 ok dönen domainleri txt olarak bulunduğu klasöre kaydeder.\n ")



while True:
    
 try:

    değer = input("Sublis3t ile çektiğim domainleri görmek istiyormusunuz ? e\h :")
    
    if değer == "e":
        sublsit = open ("TurtleDomainYahoo.txt")
        oku = sublsit.read()
        print(oku)
        continue
    elif değer == "h":
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Program çalışıyor lütfen sabirla bekleyiniz.... ")
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        break
    else:
        print("Buraya sadece Evet(e) veya Hayır(h) harflerini girebilirsiniz.")
 except:
     print("************************************************************************\n")
     print("HATA : Domainleri görebilmeniz için domain.txt dosyasını bu programın yanına koymanız gerekmektedir !\n")
     print("************************************************************************\n")
        
from bs4 import BeautifulSoup
import requests
 
url1 = ('https://za.yahoo.com')
url2 = ('https://uk.118800.yahoo.com')
url3 = ('https://espanol.answers.yahoo.com')
url4 = ('https://de.blog.360.yahoo.com')
url5 = ('https://Erdavis031.yahoo.com')
url6 = ('https://beta.answers.yahoo.com')
url7 = ('https://ar.yahoo.com')
url8 = ('https://maktoob.sports.yahoo.com')
url9 = ('https://static.autos.yahoo.com')
url10 = ('https://att.yahoo.com')
url11 = ("https://sports.yahoo.com")

url12 = ('https://de.eurosport.yahoo.com')
url13 = ('https://football.fantasysports.yahoo.com')
url14 = ('https://tw.games.yahoo.com')
url15 = ('https://help.yahoo.com')
url16 = ('https://labs.yahoo.com')
url17 = ('https://www.visualize.yahoo.com')
url18 = ('https://bas2-1-grd.ne1.yahoo.com')
url19 = ('https://restore-trad-09.hff01.ne1.yahoo.com')
url20 = ('https://store.yahoo.com')


try:

 istek = requests.get(url2)

 html = istek.status_code


 print(url2 , " : " , html)


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url2)
    print("*******************************************************************")

try:
    
 istek = requests.get(url1)

 html = istek.status_code

 if html == 200:
    print(url1 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
    dosya = open("zayahoo.txt","w",encoding="utf-8")
    dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
    dosya.close()
 if html == 404:
     print(url1 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url1 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)")
     


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url1)
    print("*******************************************************************")

try:
    
 istek = requests.get(url3)

 html = istek.status_code


 if html == 200:
     print(url3 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("espanol answers yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url3 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url3 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 



 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url3)
    print("*******************************************************************")

try:
    
 istek = requests.get(url4)

 html = istek.status_code


 if html == 200:
     print(url4 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("de blog 360 yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url4 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url4 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 



 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url4)
    print("*******************************************************************")

try:
    
 istek = requests.get(url5)

 html = istek.status_code


 if html == 200:
     print(url5 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("Erdavis031 yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url5 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url5 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 



 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url5)
    print("*******************************************************************")

try:
    
 istek = requests.get(url6)

 html = istek.status_code

 
 if html == 200:
     print(url6 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("beta answers yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url6 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url6 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 



 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url6)
    print("*******************************************************************")

try:
    
 istek = requests.get(url7)

 html = istek.status_code


 if html == 200:
     print(url7 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("ar yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url7 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url7 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 

    

 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url7)
    print("*******************************************************************")


try:
    
 istek = requests.get(url8)

 html = istek.status_code


 if html == 200:
     print(url8 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("maktoob sports yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url8 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url8 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 



 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url8)
    print("*******************************************************************")


try:
    
 istek = requests.get(url9)

 html = istek.status_code

 if html == 200:
     print(url9 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("static autos yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url9 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url9 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 



 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url9)
    print("*******************************************************************")
    

try:
    
 istek = requests.get(url10)

 html = istek.status_code

 if html == 200:
     print(url10 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("att yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url10 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url10 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 



 print("----------------------------------------------------------------------")

except:
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url0)

try:
    
 istek = requests.get(url1)

 html = istek.status_code

 if html == 200:
     print(url11 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("sports yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url11 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(urll1 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url1)
    print("*******************************************************************")

try:
    
 istek = requests.get(url2)

 html = istek.status_code
 
 if html == 200:
     print(url12 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("de eurosport yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url12 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url12 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url2)
    print("*******************************************************************")

try:
    
 istek = requests.get(url3)

 html = istek.status_code
 if html == 200:
     print(url13 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("football fantasysports yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url13 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url13 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url13)
    print("*******************************************************************")

try:
    
 istek = requests.get(url14)

 html = istek.status_code
 if html == 200:
     print(url14 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("tw games yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url14 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url14 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url14)
    print("*******************************************************************")

try:
    
 istek = requests.get(url15)

 html = istek.status_code

 if html == 200:
     print(url15 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("help yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url15 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url15 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url15)
    print("*******************************************************************")

try:
    
 istek = requests.get(url16)

 html = istek.status_code

 if html == 200:
     print(url16 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("labs yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url16 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url16 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url16)
    print("*******************************************************************")

try:
    
 istek = requests.get(url17)

 html = istek.status_code

 if html == 200:
     print(url17 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("www visualize yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url17 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url17 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url17)
    print("*******************************************************************")

try:
    
 istek = requests.get(url18)

 html = istek.status_code

 if html == 200:
     print(url18 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("bas2 1 grd ne1 yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url18 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url18 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url18)
    print("*******************************************************************")

try:
    
 istek = requests.get(url19)

 html = istek.status_code

 if html == 200:
     print(url19 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("restore trad 09 hff01 ne1 yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url19 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url19 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url19)
    print("*******************************************************************")

try:
    
 istek = requests.get(url20)

 html = istek.status_code

 if html == 200:
     print(url20 , " : " ,"[", html,"]", "Bağlantı Kuruldu")
     dosya = open("store yahoo.txt","w",encoding="utf-8")
     dosya.write("[ 200 ] *OK* - ( ͡° ͜ʖ ͡°) Black Turtle ( ͡° ͜ʖ ͡°)")
     dosya.close()
 if html == 404:
     print(url20 , " : " ,"[", html,"]", "Sunucu Aktif Değil")
     
 if html == 500:
     print(url20 , " : " ,"[", html,"]", "Bunun Ne Olduğunu Bilmiyorum :)") 


 print("----------------------------------------------------------------------")

except:
    print("*******************************************************************")
    print("Bu Sunucu İle Bağlantı Kurulamadı : ",url2)
    print("*******************************************************************")    
