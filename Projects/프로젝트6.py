data=[]

hap=0
avg=0
t=0

while True:
    choice=eval(input('\n1.수강 강좌정보 입력 2.평점평균 확인 3.졸업여건 확인 4.종료: '))
    if choice==1:
        lecture=input('\n수강한 강좌 입력(종료:0): ')
        for i in lecture:
            if lecture!='0':
                credit=int(input('학점수 입력(예:1,2,3): '))
                grade=float(input('취득학점 입력(0.0~4.5): '))
                data.append((lecture, int(credit), int(grade)))
                hap+=data[t][2]
                t+=1
                avg=hap/t
                lecture=input('수강한 강좌 입력(종료:0): ')
            if lecture=='0':
                break
    elif choice==2:
        print('평점평균: %.1f' %(avg))
        if avg>=4.0:
            print('장학 대상자입니다')
        elif avg<4.0:
            print('장학 대상자가 아닙니다')
    elif choice==3:
        semester=int(input('총 등록학기: '))
        if semester>=8:
            print('졸업학기 충족')
        elif semester<8:
            print('학기 부족')
        credit=int(input('총 학점수: '))
        if credit>=120:
            print('졸업학점 충족')
        elif credit<120:
            print('졸업학점 부족')
        avg2=eval(input('총 평균평점: '))
        if avg2>=2.5:
            print('졸업 평균평점을 충족')
        elif avg2<2.5:
            print('졸업 평균평점 부족')
        if semester>=8 and credit>=120 and avg2>=4.0:
            print('\n졸업장학 대상자입니다')
    elif choice==4:
        print('종료합니다')
        break
