total_list = []

while True:
    question = input("질문을 입력하세요: ")
    if question == "q":
        break
    else:
        total_list.append({"질문": question, "답변":""})
for i in total_list:
    print(i["질문"])  #질문을 key로 해서 접근하기
    answer = input("답변을 입력해주세요: ")
    i["답변"] = answer    #답변을 Key로 해서 접근해서 answer에 input된 값 넣어주기
print(total_list)