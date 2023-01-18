result=[]
print('[스마트 카페 메뉴 목록]\n')
menu=[['에스프레소',2000,'커피'],['아메리카노',2500,'커피'],['카푸치노',3000,'커피'],
      ['카페라떼',3000,'커피'],['모카라떼',3500,'커피'],['바닐라라떼',3500,'커피'],
      ['소이라떼',3500,'커피'],['피넛라떼',3700,'커피'],['토피넛라떼',3700,'커피'],
      ['화이트모카',3700,'커피'],['카라멜마끼아또',4000,'커피'],['프라프치노',4000,'커피'],
      ['핫초코',3500,'음료'],['레몬에이드',3500,'음료'],['청포도에이드',3500,'음료'],
      ['자몽에이드',3500,'음료'],['스무디',3500,'음료'],['망고스무디',3500,'음료'],
      ['딸기스무디',3500,'음료'],['초코쿠키',2000,'디저트'],['화이트쿠키',2000,'디저트'],
      ['피넛쿠키',2000,'디저트'],['당근케이크',5000,'디저트'],['초코케이크',5000,'디저트'],
      ['치즈케이크',5000,'디저트']]
for i in menu:
        print(i[0], end=' ')
print('\n')
a=0
t=0
hap=0
while True:
    choice=eval(input('1.가격별 메뉴 조회 2.종류별 메뉴 조회 3.주문 0.종료: '))
    result=[]
    if choice<0 or choice>3:
        print('없는 번호!')
        continue
    elif choice==1:
        min,max=eval(input('최저가격, 최고가격 입력(예:1000,2000) '))
        for i in menu:
            if i[1]>=min and i[1]<=max:
                result.append(i[:2])
        print('\n<입력조건의 메뉴 목록>')
        print(result, end='\n\n')
    elif choice==2:
        category=input('종류별 메뉴 입력(예:커피,음료,디저트) ')
        for i in menu:
            if i[2]==category:
                result.append(i[:2])
        print('\n<입력조건의 메뉴 목록>')
        print(result, end='\n\n')
    elif choice==3:
        order=input('주문 메뉴 입력(0:종료) ')
        while a<25:
            if menu[a][0]==order:
                count=int(input('수량 입력: '))
                result.append(menu[a][:2])
                result[t].append(count)
                order=input('주문 메뉴 입력(0:종료) ')
                t=t+1
                a=-1
            elif order=='0':
                break
            a=a+1
        print('\n주문 내역 확인: {}'.format(result))
        for i in result:
                money=i[1]*i[2]
                hap+=money
        print('지불 총금액: {}원'.format(hap), end='\n\n')
        cash=int(input('결재를 위한 현금 입력: '))
        change=cash-hap
        print('지불 총금액: {}원, 거스름돈: {}원'.format(hap,change))
    elif choice==0:
        print('스마트 카페 메뉴조회 시스템 종료!')
        break
