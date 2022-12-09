from wsgiref import headers
import schedule
import time
import requests
import sys
import pymysql
import hashlib
from bs4 import BeautifulSoup as bs

def bestdd(db):
    url="https://www.ddanzi.com/index.php?mid=free&statusList=HOT%2CHOTBEST%2CHOTAC%2CHOTBESTAC"
    cpName="The ddanzi"
    category="best"
    
    try:
        req=requests.get(url)
        
        if req.status_code == 200:        
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("ul.list>li")
            
            my_list = list()
            for data in bsi:
                try:
                    title=data.get_text().strip()
                    link=data.select_one("a")["href"]
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, link, category))
                except Exception:
                    pass
                
            if db:                
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content_best (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def bestcl(db):
    url="https://www.clien.net/service/recommend"
    host="https://www.clien.net"
    cpName="Clien Best"
    category="best"
    
    try:
        req=requests.get(url)
    
        if req.status_code == 200:        
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select(".list_subject")
            
            my_list = list()
            for data in bsi:
                try:
                    title=data.select_one(".subject_fixed").get_text()
                    link=data["href"]
                    # print(title + ":" + host+link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content_best (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
    
def bestbb(db):
    url="https://www.bobaedream.co.kr/list?code=best"
    host="https://www.bobaedream.co.kr"
    cpName="Bobaedream"
    category="best"
    
    try:
        req=requests.get(url)
        req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".pl14")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.select_one("a").get_text()
                    link=data.select_one("a")["href"]
                    # print(title + ":" + host+link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content_best (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")

def bestit(db):
    url="https://itssa.co.kr/hot"
    host="https://itssa.co.kr"
    cpName="itssa"
    category="news"
    
    try:
        # req=requests.get(url)
        # req.encoding='UTF-8'
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)
    
        if req.status_code == 200:        
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select(".subject")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=(data.get_text()).strip()
                    link=data["href"]
                    # print(title + ":" + host+link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def xartpd(db):
    url="https://www.podong.kr/community/17k.dong"
    host="https://www.podong.kr"
    cpName="Podong"
    category="xart"
    
    try:
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select("span.desc")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.select_one("a").get_text().strip()
                    link=data.select_one("a")["href"]
                    # print(title + ":" + host+link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def xartbb(db):
    url="https://www.bobaedream.co.kr/list?code=girl"
    host="https://www.bobaedream.co.kr"
    cpName="Bobaedream"
    category="xart"
    
    try:
        req=requests.get(url)
        req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".pl14")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.select_one("a").get_text()
                    link=data.select_one("a")["href"]
                    # print(title + ":" + host+link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def soccfm(db):
    url="https://www.fmkorea.com/?mid=football_news&sort_index=pop&order_type=desc"
    host="https://www.fmkorea.com"
    cpName="FM코리아"
    category="socc"
    
    try:
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".li_best2_pop0")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.select_one("img")["alt"]
                    link=data.select_one("a")["href"]
                    # print(title + ":" + host+link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def baseml(db):
    url="https://mlbpark.donga.com/mp/best.php?b=mlbtown&m=like"
    host="https://mlbpark.donga.com/mp/"
    cpName="MLB Park"
    category="base"
    
    try:
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".txt")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.get_text()
                    link=data["href"]
                    # print(title + ":" + link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def basekb(db):
    url="https://mlbpark.donga.com/mp/best.php?b=kbotown&m=like"
    host="https://mlbpark.donga.com/mp/"
    cpName="KBO Park"
    category="base"
    
    try:
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".txt")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.get_text()
                    link=data["href"]
                    # print(title + ":" + link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def moviex(db):
    url="https://extmovie.com/bestboard"
    host="https://extmovie.com"
    cpName="extmovie"
    category="movi"
    
    try:
        headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url, headers=headers)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".title_area")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.select_one("a").get_text().strip()
                    link=data.select_one("a")["href"]
                    # print(title + ":" + host+link)
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def girlpn(db):
    url="https://m.pann.nate.com/talk/today"
    host="https://m.pann.nate.com"
    cpName="PAN"
    category="girl"
    
    try:
        # headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select("ul.list_type2>li")
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    temp=data.select_one(".tit").get_text()
                    remo=len(data.select_one(".count").get_text())
                    # print(temp+":"+str(remo))
                    title=temp[0:-remo]
                    link=data.select_one("a")["href"]                    
                        
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def girl82(db):
    url="https://www.82cook.com/entiz/enti.php?bn=15"
    host="https://www.82cook.com"
    cpName="82Cook"
    category="girl"
    
    try:
        # headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select("ul.most>li")
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    title=data.select_one("a")["title"]
                    link=data.select_one("a")["href"]
                    
                    if len(link) > 2 and len(title) > 2:
                        # print(title + ":" + host+link)
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))
                except Exception:
                    pass
                            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def shoppp(db):
    url="https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu&hotlist_flag=999"
    host="https://www.ppomppu.co.kr"
    cpName="ppomppu"
    category="shop"
    
    try:
        # headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select("td>div")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.select_one(".list_title").get_text()
                    link=data.select_one("a")["href"]
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        if(link[0] == '/'):
                            # print(title + ":" + host+link)
                            my_list.append((enc, cpName, title, host+link, category))
                        else:
                            # print(title + ":" + host+"/zboard/"+link)
                            my_list.append((enc, cpName, title, host+"/zboard/"+link, category))                    
                except Exception:
                    pass
                            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def newspp(db):
    url="https://ppss.kr/archives"
    host="https://www.ppomppu.co.kr"
    cpName="PPSS"
    category="news"
    
    try:
        # headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".entry-title-link")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.get_text()
                    link=data["href"]
                    
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, link, category))                                        
                except Exception:
                    pass
                            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def poxnet(db):
    url="http://www.paxnet.co.kr/tbbs/list?tbbsType=L&id=N10584"
    host="http://www.paxnet.co.kr/tbbs/view?id=N10584&seq="
    cpName="Poxnet"
    category="stoc"
    
    try:
        # headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".best-title")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.get_text().strip()
                    linko=data["href"]
                    link=linko[linko.find("(")+1:len(linko)-2]
                    # print(title + ":" + host+link)
                    # http://www.paxnet.co.kr/tbbs/view?id=N10584&seq=150357587129889
                    if len(link) > 2 and len(title) > 2:
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))                                        
                except Exception:
                    pass
                            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")

def itctcl(db):
    url="https://www.clien.net/service/board/news"
    host="https://www.clien.net"
    cpName="Clien"
    category="itct"
    
    try:
        # headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text        
            soup=bs(html, "html.parser")
            bsi=soup.select(".list_subject")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.get_text().strip()
                    link=data["href"]
                    
                    if len(link) > 2 and len(title) > 2:
                        # print(title + ":" + host+link)
                        if(link.find("rule") < 0):
                            enc=hashlib.md5(title.encode()).hexdigest()
                            my_list.append((enc, cpName, title, host+link, category))                                        
                except Exception:
                    pass
                            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")
        
def devpdc(db):
    url="https://gall.dcinside.com/board/lists/?id=programming"
    host="https://gall.dcinside.com"
    cpName="DC"
    category="devp"
    
    try:
        headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"}
        req=requests.get(url, headers=headers)
        # req.encoding='UTF-8'
        
        if req.status_code == 200:        
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select(".us-post")
            
            my_list = list()
            for data in bsi:
                try:
                    # print(data)
                    title=data.select_one("a").get_text()
                    link=data.select_one("a")["href"]
                    
                    if len(link) > 2 and len(title) > 2:
                    #     # print(title + ":" + host+link)
                    #     if(link.find("rule") < 0):
                        enc=hashlib.md5(title.encode()).hexdigest()
                        my_list.append((enc, cpName, title, host+link, category))                                        
                except Exception:
                    pass
                            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
            
                sql="INSERT IGNORE INTO content (cid, cpname, title, link, category) VALUES (%s, %s, %s, %s, %s)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(cpName + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
            
        else :
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception:
        now=time
        print(cpName + " | " + now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception")

def batch():
    now=time
    print("Start : " + now.strftime('%Y-%m-%d %H:%M:%S'))
    
    dbWrite=True
    schedule.every(52).minutes.do(bestdd, dbWrite)
    schedule.every(41).minutes.do(bestcl, dbWrite)
    schedule.every(93).minutes.do(bestbb, dbWrite)
    schedule.every(121).minutes.do(bestit, dbWrite)
    schedule.every(133).minutes.do(xartpd, dbWrite)
    schedule.every(92).minutes.do(xartbb, dbWrite)
    schedule.every(151).minutes.do(soccfm, dbWrite)
    schedule.every(152).minutes.do(baseml, dbWrite)
    schedule.every(153).minutes.do(basekb, dbWrite)
    schedule.every(99).minutes.do(moviex, dbWrite)
    schedule.every(125).minutes.do(girlpn, dbWrite)
    schedule.every(122).minutes.do(girl82, dbWrite)
    schedule.every(181).minutes.do(shoppp, dbWrite)
    schedule.every(201).minutes.do(newspp, dbWrite)
    schedule.every(185).minutes.do(poxnet, dbWrite)
    schedule.every(111).minutes.do(itctcl, dbWrite)
    schedule.every(51).minutes.do(devpdc, dbWrite)

    # schedule.every(4).seconds.do(bestdd, dbWrite)
    # schedule.every(4).seconds.do(bestcl, dbWrite)
    # schedule.every(6).seconds.do(bestbb, dbWrite)
    # schedule.every(8).seconds.do(bestit, dbWrite)
    # schedule.every(10).seconds.do(xartpd, dbWrite)
    # schedule.every(11).seconds.do(xartbb, dbWrite)
    # schedule.every(12).seconds.do(soccfm, dbWrite)
    # schedule.every(14).seconds.do(baseml, dbWrite)
    # schedule.every(3).seconds.do(basekb, dbWrite)
    # schedule.every(4).seconds.do(moviex, dbWrite)
    # schedule.every(6).seconds.do(girlpn, dbWrite)
    # schedule.every(7).seconds.do(girl82, dbWrite)
    # schedule.every(1).seconds.do(shoppp, dbWrite)
    # schedule.every(2).seconds.do(newspp, dbWrite)
    # schedule.every(4).seconds.do(poxnet, dbWrite)
    # schedule.every(6).seconds.do(itctcl, dbWrite)
    # schedule.every(9).seconds.do(devpdc, dbWrite)
    
    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ == "__main__":
    # bestit(True)
    # devpdc(True)
    batch()


