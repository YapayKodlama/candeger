import pandas as pd
import pywhatkit as kit
import time

x=0 #Sıfırdan Başlattım.
df = pd.read_csv('data.csv')#data.csv belgesini okuttum.
while True:#Döngü başlattım.
    num = df.iloc[x,1]#Numaraları değişkene atamaya başladım.
    kit.sendwhatmsg_instantly((num), "Merhaba, yeni numaram bu kaydedebilirsiniz.")#Direkt olarak numaraya gönderdim mesajı.
    x=x+1#Bir sonraki numaraya geçirdim
    time.sleep(5)#Çift sekme'de açınca hata veriyor o gönderdikten sonra devam etmesi adına beklettim.
    if num==None:#Eğer num değişkeni boşa düşerse kodu durdurdum.
        break