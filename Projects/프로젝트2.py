def save(day, att_book):
    for i in range(day):
        print('%d주차 강의에 출석하셨나요?' %(i+1))
        att_book[i]=int(input('출석은 1, 결석은 0 >>> '))

def count():
    global cnt, att
    cnt=att_book.count(0)
    att=att_book.count(1)

def ratio_print():
    global x_ratio, o_ratio
    x_ratio=(cnt/day)*100
    o_ratio=(att/day)*100

day=int(input('한 학기 수업주차 입력: '))
att_book=[0]*day

save(day, att_book)
count()
ratio_print()

if (cnt/day)>=0.3:
    print('수업일수 부족입니다.')

print('결석 횟수: %d' %cnt)
print('출석 횟수: %d' %att)
print('결석률은: %.f%%' %x_ratio)
print('출석률은: %.f%%'%o_ratio)
