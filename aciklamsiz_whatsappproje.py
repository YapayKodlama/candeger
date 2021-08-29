import pandas as pd
import pywhatkit as kit
import time

x=0
df = pd.read_csv('data.csv')
while True:
    num = df.iloc[x,1]
    kit.sendwhatmsg_instantly((num), "Merhaba, yeni numaram bu kaydedebilirsiniz.")
    x=x+1
    time.sleep(5)
    if num==None:
        break
