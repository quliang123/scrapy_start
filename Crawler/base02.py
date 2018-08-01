import urllib2, urllib

values = {"username": "529075990@qq.com", "password": "xxxx"}

data = urllib.urlencode(values)

url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

request = urllib2.Request(url, data)

response = urllib2.urlopen(request)

print response.read() 
