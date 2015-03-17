import requests
dat = {'validator' : 'banana', 'theirVote' : 'Gabe Newell'}
c = 0;
while True:
    c += 1
    r = requests.post("http://hunks.heatworld.com/appender.php", data=dat)
    print(str(c) + " : " + str(r.status_code))

