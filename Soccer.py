import requests
import sys
from bs4 import BeautifulSoup as bs

url="https://kr.soccerway.com/national/england/premier-league/20222023/regular-season/r69471/matches/"
# url="https://www.ddanzi.com/index.php?mid=free&statusList=HOT%2CHOTBEST%2CHOTAC%2CHOTBESTAC"
headers={"User-Agent":"Mozilla/5.0"}
req=requests.get(url, headers=headers)

if req.status_code == 200:
    html=req.text
    soup=bs(html, "html.parser")
    print(soup)
else:
    print(sys._getframe().f_code.co_name + "=" + str(req.status_code))