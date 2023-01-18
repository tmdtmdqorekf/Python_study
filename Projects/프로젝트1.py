def menu_price():
    print('** 자판기 판매 메뉴 **')
    for i in range(5):
        print('{} : {} {}'.format(i+1,menu[i],price[i]))
print()

def drinking(price):
    global money
    while True:
        num=int(input('메뉴 선택 (종료:0): '))
        if num==0:
            break
        elif money<price[num-1]:
            print('잔액부족')
        else:
            print(menu[num-1],'구입완료')
            money=money-price[num-1]
        print('잔액:',money)
        print()

def change():
    global money
    coin500=money//500
    coin100=(money%500)//100
    leftover=money%100
    print('자판기 종료, 잔액 {} 반환'.format(money))
    print('coin500: %d개 반환' %(coin500))
    print('coin100: %d개 반환' %(coin100))
    print('나머지: %d 반환' %(leftover))

menu=['콜라', '사이다', '환타', '커피', '생수']
price=[500, 500, 600, 600, 400]
menu_price()

money=int(input('돈을 투입하세요: '))
print()
drinking(price)
change()