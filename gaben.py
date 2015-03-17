import requests
import time
dat = {'validator' : 'banana', 'theirVote' : 'Gabe Newell'}
c = 0;
while True:
    c += 1
    r = requests.post("http://hunks.heatworld.com/appender.php", data=dat)
    if r.status_code != 200:
        print("Endpoint is kill, waiting 60 seconds")
        time.sleep(60)

    print(str(c) + " : " + str(r.status_code))
