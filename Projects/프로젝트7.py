a=open('library3.csv')
lines=a.readlines()

data=[]

for line in lines:
    libList=line.rstrip('\n')
    name,address,contact=libList.split(',')
    data.append([name,address,contact])
    data.sort(key=lambda x:x[0])
    
while True:
    i=input('\n검색어 입력(종료:0) ')
    if i!='0':
        print('\n[도서관 정보 검색 결과]')
    for b in data:
        if i in b[0]:
            print(b[0],'/',b[1],'/',b[2])
        elif i=='0':
            break
    if i=='0':
        break
