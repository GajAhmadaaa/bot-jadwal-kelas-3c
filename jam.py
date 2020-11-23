import schedule
import time
from kuliah import ads, adscall, rpl, rplcall, imk, pok, ppw, ppwcall, halo, halocall, komdat, metnum, libur

schedule.every().monday.at("07:25").do(adscall)
schedule.every().monday.at("07:30").do(ads, adscall)
schedule.every().tuesday.at("07:25").do(rplcall)
schedule.every().tuesday.at("07:30").do(rpl, rplcall)
schedule.every().tuesday.at("10:15").do(imk)
schedule.every().tuesday.at("13:00").do(pok)
schedule.every().wednesday.at("07:25").do(ppwcall)
schedule.every().wednesday.at("07:30").do(ppw, ppwcall)
schedule.every().thursday.at("07:25").do(halocall)
schedule.every().thursday.at("07:30").do(halo, halocall)
schedule.every().thursday.at("10:15").do(komdat)
schedule.every().thursday.at("13:00").do(metnum)
schedule.every().friday.at("07:30").do(libur)

while True:
    schedule.run_pending()
    time.sleep(1)