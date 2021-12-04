import requests,bs4


#ここに取得したい地域のURLを指定。(東京であれば /13/4410.html、広島であれば /34/6710.html)
URL = "https://weather.yahoo.co.jp/weather/jp/34/6710.html"
TIMEOUT = 10
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0"}


#サイトにアクセスする
try:
    result = requests.get(URL, timeout=TIMEOUT, headers=HEADERS)
    result.raise_for_status()
except Exception as e:
    print("ERROR_DOWNLOAD:{}".format(e))
else:
    soup    = bs4.BeautifulSoup(result.content,"html.parser")

    #今日の天気の取得
    today_weather_elem  = soup.select("div.forecastCity > table > tr > td:nth-child(1) > div > p.pict")

    for t in today_weather_elem:
        print(t.text.strip())


    #今日の最高気温の取得
    today_temp_high_elem    = soup.select("div.forecastCity > table > tr > td:nth-child(1) > div > ul.temp > li.high")

    for t in today_temp_high_elem:
        print(t.text.strip())

    #今日の最低気温の取得
    today_temp_low_elem     = soup.select("div.forecastCity > table > tr > td:nth-child(1) > div > ul.temp > li.low")

    for t in today_temp_low_elem:
        print(t.text.strip())


    #明日の天気の取得
    tommorow_weather_elem   = soup.select("div.forecastCity > table > tr > td:nth-child(2) > div > p.pict")

    for t in tommorow_weather_elem:
        print(t.text.strip())

    #明日の最高気温の取得
    tommorow_temp_high_elem = soup.select("div.forecastCity > table > tr > td:nth-child(2) > div > ul.temp > li.high")

    for t in tommorow_temp_high_elem:
        print(t.text.strip())

    #明日の最低気温の取得
    tommorow_temp_low_elem  = soup.select("div.forecastCity > table > tr > td:nth-child(2) > div > ul.temp > li.low")

    for t in tommorow_temp_low_elem:
        print(t.text.strip())













