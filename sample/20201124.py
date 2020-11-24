# 7. 제어문 if - elif - else 문을 배워보자

fee = float(input('통행료를 책정하세요: '))
if fee > 0:
    print(f'통행료로 ${fee}를 지불하세요.')
elif fee == 0:
    print('무료로 통행할 수 있습니다')
else:
    print('올바르지 않은 통행료입니다')


# 8. 제어문 while 문을 배워보자

def pay_toll(toll, budget):
    if toll == 0:
        print('무료로 통행하였습니다.')
        return budget

    if 0 < toll <= budget:
        print(f'지불 통행료: ${toll}, 현재 예산: ${budget}')
        return budget - toll
    else:
        print(f'예산 부족: ${budget} => you need to have more ${toll - budget}')
        return -1


_budget = 1000
_toll = 15
_budget = pay_toll(_toll, _budget)
while _budget != -1:
    _budget = pay_toll(_toll, _budget)
