import requests
import sys
import time
import pymysql
import schedule
import hashlib
from datetime import datetime
from bs4 import BeautifulSoup as bs


        
def mayo(db):
    url="https://kr.soccerway.com/teams/spain/real-club-deportivo-mallorca/2027/matches/"
    
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)

        if req.status_code == 200:
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("tr.match")
            # print(bsi)            
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    matchId=data["data-event-id"]
                    matchTime=data["data-timestamp"]
                    teamA=data.select_one(".team-a").get_text().strip()
                    score=data.select_one(".score-time").get_text().strip()
                    
                    if "P" in score:
                        score="P"
                        
                    if "E" in score:
                        score="e"
                    
                    teamB=data.select_one(".team-b").get_text().strip()
                    
                    my_list.append((matchId, str(datetime.fromtimestamp(int(matchTime))), '이강인', teamA, score, teamB))                    
                except Exception as e:
                    pass
            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
                
                sql="INSERT INTO smatch (mid, mtime, league, teama, score, teamb) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE score=VALUES(score)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(matchId + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
        else:
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception as e:
        now=time
        print(now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception | " + e)
        
def wc22(db):
    url="https://kr.soccerway.com/international/world/world-cup/2022-qatar/group-stage/r49519/matches/"
    
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)

        if req.status_code == 200:
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("tr.match")
            # print(bsi)            
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    matchId=data["data-event-id"]
                    matchTime=data["data-timestamp"]
                    teamA=data.select_one(".team-a").get_text().strip()
                    score=data.select_one(".score-time").get_text().strip()
                    teamB=data.select_one(".team-b").get_text().strip()
                    
                    my_list.append((matchId, str(datetime.fromtimestamp(int(matchTime))), 'WC2022', teamA, score, teamB))                    
                except Exception:
                    pass
            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
                
                sql="INSERT INTO smatch (mid, mtime, league, teama, score, teamb) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE score=VALUES(score)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(matchId + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
        else:
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception as e:
        now=time
        print(now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception | " + e)
        
def wctt(db):
    url="https://kr.soccerway.com/international/world/world-cup/2022-qatar/s16394/final-stages/"
    
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)

        if req.status_code == 200:
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("tr.match")
            # print(bsi)            
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    matchId=data["data-event-id"]
                    matchTime=data["data-timestamp"]
                    teamA=data.select_one(".team-a")
                    teamA = teamA.select_one("a")["title"].strip()
                    # print(teamA)
                    score=data.select_one(".score-time").get_text().strip()
                    teamB=data.select_one(".team-b")
                    teamB = teamB.select_one("a")["title"].strip()
                    
                    my_list.append((matchId, str(datetime.fromtimestamp(int(matchTime))), 'WC2022', teamA, score, teamB))                    
                except Exception as e:
                    # print(e)
                    pass
            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
                
                sql="INSERT INTO smatch (mid, mtime, league, teama, score, teamb) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE score=VALUES(score)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(matchId + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
        else:
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception as e:
        now=time
        print(now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception | " + e)
        
def champ(db):
    url="https://kr.soccerway.com/international/europe/uefa-champions-league/20222023/s21847/final-stages/matches/"
    
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)

        if req.status_code == 200:
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("tr.match")
            # print(bsi)            
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    matchId=data["data-event-id"]
                    matchTime=data["data-timestamp"]
                    teamA=data.select_one(".team-a").get_text().strip()
                    score=data.select_one(".score-time").get_text().strip()
                    
                    if "P" in score:
                        score="P"
                        
                    if "E" in score:
                        score="e"
                    
                    teamB=data.select_one(".team-b").get_text().strip()
                    
                    if matchId == "":
                        matchId=hashlib.md5((teamA + teamB + matchTime).encode()).hexdigest()
                        
                    my_list.append((matchId, str(datetime.fromtimestamp(int(matchTime))), 'uefa', teamA, score, teamB))                    
                except Exception as e:
                    pass
            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
                
                sql="INSERT INTO smatch (mid, mtime, league, teama, score, teamb) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE score=VALUES(score)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(matchId + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
        else:
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception as e:
        now=time
        print(now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception | " + e)

def germ(db):
    url="https://kr.soccerway.com/national/germany/bundesliga/20232024/regular-season/r76158/matches/"
    
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)

        if req.status_code == 200:
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("tr.match")
            # print(bsi)            
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    matchId=data["data-event-id"]
                    matchTime=data["data-timestamp"]
                    teamA=data.select_one(".team-a").get_text().strip()
                    score=data.select_one(".score-time").get_text().strip()
                    teamB=data.select_one(".team-b").get_text().strip()
                    
                    my_list.append((matchId, str(datetime.fromtimestamp(int(matchTime))), 'GBL', teamA, score, teamB))                    
                except Exception:
                    pass
            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
                
                sql="INSERT INTO smatch (mid, mtime, league, teama, score, teamb) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE score=VALUES(score)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(matchId + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
        else:
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception as e:
        now=time
        print(now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception | " + e)

def spain(db):
    url="https://kr.soccerway.com/national/spain/primera-division/20232024/regular-season/r76831/matches/"
    
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)

        if req.status_code == 200:
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("tr.match")
            # print(bsi)            
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    matchId=data["data-event-id"]
                    matchTime=data["data-timestamp"]
                    teamA=data.select_one(".team-a").get_text().strip()
                    score=data.select_one(".score-time").get_text().strip()
                    teamB=data.select_one(".team-b").get_text().strip()
                    
                    my_list.append((matchId, str(datetime.fromtimestamp(int(matchTime))), 'spain', teamA, score, teamB))                    
                except Exception:
                    pass
            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
                
                sql="INSERT INTO smatch (mid, mtime, league, teama, score, teamb) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE score=VALUES(score)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(matchId + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
        else:
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception as e:
        now=time
        print(now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception | " + e)

def epl(db):
    url="https://kr.soccerway.com/national/england/premier-league/20232024/regular-season/r76443/matches/"
    
    try:
        headers={"User-Agent":"Mozilla/5.0"}
        req=requests.get(url, headers=headers)

        if req.status_code == 200:
            html=req.text
            soup=bs(html, "html.parser")
            bsi=soup.select("tr.match")
            # print(bsi)            
            
            my_list = list()
            for data in bsi:
                # print(data)
                try:
                    matchId=data["data-event-id"]
                    matchTime=data["data-timestamp"]
                    teamA=data.select_one(".team-a").get_text().strip()
                    score=data.select_one(".score-time").get_text().strip()
                    teamB=data.select_one(".team-b").get_text().strip()
                    
                    my_list.append((matchId, str(datetime.fromtimestamp(int(matchTime))), 'EPL', teamA, score, teamB))                    
                except Exception:
                    pass
            
            if db:
                con=pymysql.connect(user="root", passwd="shine20406!", host="localhost", db="secretnews", charset="utf8")
                cur=con.cursor()
                
                sql="INSERT INTO smatch (mid, mtime, league, teama, score, teamb) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE score=VALUES(score)"
                cur.executemany(sql, my_list)
                
                now=time
                print(now.strftime(matchId + " | " + '%Y-%m-%d %H:%M:%S') + " | " + str(cur.rowcount))
                
                cur.close()
                con.commit()
                con.close()
            else:
                print(my_list)
        else:
            print(sys._getframe().f_code.co_name + "=" + str(req.status_code))
    except Exception as e:
        now=time
        print(now.strftime('%Y-%m-%d %H:%M:%S') + " | request exception | " + e)

def batch():
    now=time
    print("Start : " + now.strftime('%Y-%m-%d %H:%M:%S'))
    
    dbWrite=True
    schedule.every(5).hours.do(epl, dbWrite)
    schedule.every(5).hours.do(spain, dbWrite)
    schedule.every(5).hours.do(germ, dbWrite)
    # schedule.every(6).hours.do(spain, dbWrite)
    # schedule.every(12).hours.do(champ, dbWrite)
    # schedule.every(4).hours.do(wc22, dbWrite)
    # schedule.every(4).hours.do(wctt, dbWrite)
    
    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ == "__main__":
    batch()
    # epl(True)
    # spain(False)
    # germ(True)
    # wctt(False)
    # wc22(True)
    
    # champ(True)
    # mayo(True)