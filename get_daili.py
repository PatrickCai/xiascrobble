import requests
import cPickle

urls = "http://www.kuaidaili.com/api/getproxy/?orderid=902372486112839&num=6100&browser=1&protocol=1&method=1&sort=0&sep=3"
result = requests.get(urls)
ips = result.content.split(' ')
cPickle.dump(ips, open('constants/best_daili', "w"))
