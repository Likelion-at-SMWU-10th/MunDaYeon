# 메뉴리스트를 만들고, 메뉴를 추가/삭제하는 기능을 넣어서 마지막에 최종적으로 만들어진 리스트에서 하나를 출력하는 코드 만들기
import random
import time

menus=["김치찌개","된장찌개","마라탕"]

while True:
    print(menus)
    item = input("추가할 메뉴를 입력하세요(q를 입력하면 종료됩니다.): ")
    if item == "q":
        break
    else:
        menus.append(item)
print(menus)

set_menus = set(menus)
while True:
    print(set_menus)
    item = input("삭제할 메뉴를 입력하세요(q를 입력하면 종료됩니다.): ")
    if item == "q":
        break
    else:
        set_menus = set_menus - set([item])

print(set_menus,"중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print("선택된 메뉴는!!", random.choice(list(set_menus)), "입니다")