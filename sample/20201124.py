# 7. 제어문 if - elif - else 문을 배워보자

fee = float(input('통행료를 책정하세요: '))
if fee > 0:
    print(f'통행료로 ${fee}를 지불하세요.')
elif fee == 0:
    print('무료로 통행할 수 있습니다')
else:
    print('올바르지 않은 통행료입니다')
