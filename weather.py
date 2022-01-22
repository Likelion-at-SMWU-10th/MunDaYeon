import requests
import json

city = "Seoul"
apikey = "APP_API_KEY"
lang = "kr"

# python의 fstring 기능 사용해서, 문자열에 원하는 변수 넣기!!
# api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}" => 이렇게 앞에 f 붙여주고, {변수명}
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

result = requests.get(api)
# print(type(result.text)) => 결과: <class 'str'>
data = json.loads(result.text) # 파이썬 내장함수인 json을 사용해서 result.txt를 데이터 변수에 담아 dictionary로 type 변경!
# print(type(data)) => 결과 : <class 'dict'>

# 지역 : name
print(data["name"],"의 날씨입니다.")
# 자세한 날씨 : weather - description
print("날씨는 ",data["weather"][0]["description"],"입니다.")
# 현재 온도 : main - temp
print("현재 온도는 ",data["main"]["temp"],"입니다.")
# 체감 온도 : main - feels_like
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# 습도 : main - humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
# 기압 : main - pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data["wind"]["speed"],"입니다.")