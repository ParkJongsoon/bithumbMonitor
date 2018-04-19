import json
import urllib.request
from urllib.request import Request, urlopen
import datetime
from tkinter import *

main = Tk()

currentTime = StringVar()
bithumbBTC = StringVar()
bithumbXRP = StringVar()
bithumbETH = StringVar()
bithumbDASH = StringVar()
bithumbLTC = StringVar()
bithumbETC = StringVar()

lbTile = Label(main, relief=RIDGE, width=20, text = "빗썸 모니터링").grid(row= 0)
lbTimeLabel = Label(main, relief=RIDGE, width=20, textvariable=currentTime).grid(row=0, column =1)

lbBTCTitle = Label(main, relief=RIDGE,width=20, text="빗썸 비트코인").grid(row =1, column= 0 )
lbBTCInfo = Label(main, relief=RIDGE,width=20, textvariable=bithumbBTC).grid(row = 1, column = 1)

lbXRPTitle = Label(main, relief=RIDGE,width=20, text="빗썸 리플").grid(row =2, column= 0 )
lbXRPInfo = Label(main, relief=RIDGE,width=20,  textvariable=bithumbXRP).grid(row = 2, column = 1)

lbETHTitle = Label(main, relief=RIDGE,width=20, text="빗썸 이더리움").grid(row =3, column= 0 )
lbETHInfo = Label(main, relief=RIDGE,width=20, textvariable=bithumbETH).grid(row = 3, column = 1)

lbDASHTitle = Label(main, relief=RIDGE,width=20, text="빗썸 대쉬").grid(row = 4, column= 0 )
lbDASHInfo = Label(main, relief=RIDGE,width=20, textvariable=bithumbDASH).grid(row = 4, column = 1)

lbLTCTitle = Label(main, relief=RIDGE,width=20, text="빗썸 라이트코인").grid(row = 5, column= 0 )
lbLTCInfo = Label(main, relief=RIDGE,width=20, textvariable=bithumbLTC).grid(row = 5, column = 1)

lbETCTitle = Label(main, relief=RIDGE,width=20, text="빗썸 이더리움클래식").grid(row = 6, column= 0 )
lbETCInfo = Label(main, relief=RIDGE,width=20, textvariable=bithumbETC).grid(row = 6, column = 1)

    
def findPrice():
    try :
        urlTicker = urllib.request.urlopen('https://api.bithumb.com/public/ticker/all')
        jsonData = json.loads(urlTicker.read())    
        FindBTC = jsonData['data']['BTC']['sell_price']
        bithumbBTC.set(FindBTC)
        FindETH = jsonData['data']['ETH']['closing_price']
        bithumbETH.set(FindETH)
        FindDASH = jsonData['data']['DASH']['closing_price']
        bithumbDASH.set(FindDASH)
        FindLTC = jsonData['data']['LTC']['closing_price']
        bithumbLTC.set(FindLTC)
        FindETC = jsonData['data']['ETC']['closing_price']
        bithumbETC.set(FindETC)
        FindXRP = jsonData['data']['XRP']['closing_price']
        bithumbXRP.set(FindXRP)
        currentTime.set(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
        main.after(500, findPrice)

    except StopIteration:
        main.destroy()
    
findPrice()
main.mainloop()


    



    


