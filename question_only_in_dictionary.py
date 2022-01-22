total_dictionary = {}

while True:
    question = input("질문을 입력하세요: ")
    if question == "q":
        break
    else:
        total_dictionary[question] = "" #total_dictionary의  key로 question에 담긴 것이 들어가고, value에는 아무것도 안담기는 형태

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요: ")
    total_dictionary[i] = answer
print(total_dictionary)