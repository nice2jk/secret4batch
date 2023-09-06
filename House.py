import csv
import os
import datetime

def batch(ref, ref2, type, dong):
    cwd = os.getcwd()
    file_path=os.path.join(cwd, ref+'.txt')
    f=open(file_path, 'rt', encoding='UTF8')
    
    print(ref)
    
    check = 0
    count = 0
    sta=False
    # result=""
    list = []
    wData = []
    
    for line in f.readlines():        
        if ref+ref2 in line:
            count += 1
            sta=True
            # result += str(count)
            list.append(count)
            list.append(ref)
            
        if "확인매물" in line:
            idx = line.find('중개사')
            if idx == -1:
                # result += " : " + line
                list.append(line[4:].strip())
                # print(str(count) + " : " + str(check) + " : " + line.strip())
                # print(result)
            else:
                # result += " : " + line[0:idx] + '\n'
                list.append(line[4:idx])
                # print(str(count) + " : " + str(check) + " : " + line[0:idx])
                # print(result)
            check=0
            sta=False
            # print(list)
            wData.append(list)
            list =[]
        elif "등록일" in line:
            idx = line.find('중개사')
            if idx == -1:                
                list.append(line[4:].strip())                
            else:                
                list.append(line[4:idx])                
            check=0
            sta=False
            # list.append(line[3:].strip())
            wData.append(list)
            list =[]
        
        if sta == True:
            if check == 0: # 동수
                # result += " : " + line[line.find(ref2):line.find("동")].strip()
                # print(line)
                # list.append(line[line.find(ref2):line.find("동")].strip())
                list.append(line[line.find(ref2):len(line) - 2].strip())
                # print(line[line.find(ref2):len(line) - 2])
                
                # print(str(count) + " : " + str(check) + " : " + line[line.find(ref2):].strip())
            elif check == 1: #매매
                # print(line[:2])
                list.append(line[:2])
                list.append(line[2:].strip())
            elif check == 2: #아파트
                # if "아파트" in line:
                #     line = line[3:]
                # result += " : " + line.strip()
                result = line[3:].strip().split(",")
                # print(result)
                list.append(result[0])
                list.append(result[1])                
                # list.append(line[3:].strip())
                # print(str(count) + " : " + str(check) + " : " + line.strip())
            check += 1
            
    print(len(wData))
    
    f = open("data" + str(datetime.datetime.now().date()) + "_" + str(dong) + ".csv", type, newline='', encoding='UTF8')
    writer = csv.writer(f)
    
    writer.writerows(wData)
    f.close()
    
def prt():
    tt = "115.77/84.96㎡, 중/18층, 동향"
    ttt = tt.split(",")
    print(ttt)
    # print(datetime.datetime.now().date())
    
def sang2dong():
    batch("행복한서해그랑블", "24", "w", 2)
    batch("푸른창보밀레시티", "25", "a", 2)
    batch("푸른한라비발디", "25", "a", 2)
    batch("행복한금호어울림", "24", "a", 2)
    batch("행복한한양수자인", "24", "a", 2)
    batch("하얀마을아이파크", "26", "a", 2)
    batch("하얀경남", "26", "a", 2)
    batch("백송상동자이", "27", "a", 2)
    batch("백송LG,SK", "27", "a", 2)
    batch("백송동남디아망", "27", "a", 2)
    batch("백송풍림아이원", "27", "a", 2)
    
def sang3dong():
    batch("다정한금강KCC", "21", "w", 3)    
    batch("다정한쌍용", "21", "a", 3)
    batch("다정한삼성래미안", "21", "a", 3)
    batch("다정한경남아너스빌", "21", "a", 3)
    batch("라일락대우,유림", "23", "a", 3)
    batch("라일락서해그랑블", "23", "a", 3)
    batch("라일락동양덱스빌", "23", "a", 3)
    batch("라일락경남아너스빌", "23", "a", 3)
    batch("라일락신성미소지움", "23", "a", 3)
    batch("진달래대우", "22", "a", 3)
    batch("진달래대림e-편한세상", "22", "a", 3)
    batch("진달래신동아파밀리에", "22", "a", 3)
    batch("진달래써미트빌", "22", "a", 3)
    batch("진달래효성", "22", "a", 3)
    
    
if __name__ == "__main__":    
    # prt()
    sang2dong()
    sang3dong()
    