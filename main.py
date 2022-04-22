import requests

headers = {

  "Host": "www.banglane.ac.th",

  "Connection": "keep-alive",

  "Content-Length": "55",

  "Cache-Control": "max-age=0",

  "Upgrade-Insecure-Requests": "1",

  "Origin": "http://banglane.ac.th",

  "Content-Type": "application/x-www-form-urlencoded",

  "User-Agent": "Mozilla/5.0 (Linux; Android 12; OPPO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",

  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

  "Referer": "http://banglane.ac.th/",

}

data = {

  "month":"13",

  "year":"2050",

  "studentid":"13992",

  "weight":"156",

  "height":"38"

}

wh = requests.post("http://www.banglane.ac.th/wh/whsubmit",data=data, headers=headers)
