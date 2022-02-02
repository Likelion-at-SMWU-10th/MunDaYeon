# 메뉴 한번 랜덤 출력하기
# import time -> time.sleep(n) 쓰기 위해 import 해주어야 함
import random
print("randomly printed menu is:")
print(random.choice(["creampasta", "oilpasta", "tomatopasta","risotto"])) #["~", "~", "~", ...] -> 리스트형태

print("-----------------------------------------------------------")

# 메뉴 30번 랜덤 출력하기
print("randomly printed 30 menus are:")
for i in range(30):
    print(i+1,random.choice(["cream pasta", "oil pasta", "tomato pasta", "risotto", "chicken", "steak"]))

# time.sleep(n) -> n초씩 쉬기!
print("-----------------------------------------------------------")

# 딕셔너리
print("<딕셔너리 형태 출력>")
information = {"이름":"문다연", "나이":"24", "특이사항":"고양이 키움"}
print(information)
print("\n")

print("<딕셔너리 속 항목 하나 꺼내오는 방법 : .get('항목명')")
print(information.get("나이"))
print("\n")

print("<딕셔너리에 항목과 내용 추가하기 : 딕셔너리명['항목']='추가할내용'>")
information["취미"]="유튜브보기"
information["좋아하는것"]="뒹굴거리기"
print(information)
print("\n")

print("<딕셔너리에 항목과 내용 삭제하기 : del딕셔너리명['항목']>")
del information["나이"]
print(information)
print("\n")
# print(len(딕셔너리명)) -> 딕셔너리 안의 항목 개수 출력
# 딕셔너리명.clear -> 딕셔너리 안의 내용 모두 삭제

# 리스트
foods = ["김밥","마라탕","초밥"]
print(foods)

print("<리스트에 추가하기: 리스트명.append('추가할내용')>")
foods.append("우동")
print(foods)
print("\n")

print("<리스트에 삭제하기: del foods[인덱스번호]>")
del foods[2]
print(foods)
print("\n")

#set -> 집합
print("<집합>")
foods = ["김밥","마라탕","초밥","김밥"]
print(foods)
foods_set = set(foods)
print(foods_set)

# 합집합 |
print("\n","<합집합>")
menu1=set(["귤","대추차","초콜릿","고구마"])
menu2=set(["된장찌개","소고기","닭가슴살","고구마"])
menu3=menu1|menu2
print(menu3)

# 교집합 &
print("\n","<교집합>")
menu1=set(["귤","대추차","초콜릿","고구마"])
menu2=set(["된장찌개","소고기","닭가슴살","고구마"])
menu3=menu1&menu2
print(menu3)

# 차집합 -
print("\n","<차집합>")
menu1=set(["귤","대추차","초콜릿","고구마"])
menu2=set(["된장찌개","소고기","닭가슴살","고구마"])
menu3=menu1-menu2
menu4=menu2-menu1
print(menu3)
print(menu4)
