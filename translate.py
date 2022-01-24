from googletrans import Translator

# 번역기 만들기
translator = Translator()

# 언어감지 원하는 문장 작성하기
# sentence = "구글번역기를 이용해 번역하기!"
sentence = input("언어감지하고 싶은 문장을 작성해주세요: ")

# 언어 감지 후 돌려주는 함수 작성하기
detected = translator.detect(sentence)  # Translator의 기본 내장함수 이용!

# print(detected) => Detected(lang=ko, confidence=None)
print(detected.lang)