from googletrans import Translator

# 번역기 만들기
translator = Translator()

# 번역기에 넣어줄 재료 만들기
sentence = input("번역하고 싶은 문장을 입력해주세요 : ") 
dest = input("어떤 언어로 번역하고 싶으신가요? (영어는 en, 프랑스어는 fr, 베트남어는 vi 를 입력해주세요): ")
'''
번역기에 넣어줄 재료>
1. sentence
2. dest (참고 사이트 : https://py-googletrans.readthedocs.io/en/latest/)
3. src (optional)
'''
# 번역기 사용하기
result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

'''
print(result) 
언어감지하고 싶은 문장을 작성해주세요: 나는 누구인가
Translated(src=ko, dest=en, text=Who am I, pronunciation=None, extra_data="{'confiden...")
'''

print("=======출력결과========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("=======================")
