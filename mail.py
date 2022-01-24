# 메일링 사전준비
'''
1. 구글 IMAP 설정하기(https://likelion.notion.site/Google-93ee4cffb5b7481584be4de44ce5bf5e)
2. 구글 보안 수준 변경하기(https://likelion.notion.site/Google-IMAP-ca417541e62b4f958ff695b8db8c0feb)
'''
# SMTP : Simple Main Transfer Protocol
# SMTP 서버를 이용해서 우리가 원하는 곳으로 이메일을 보낼 수 있다! SMTP 서버에는 이메일이 저장되는 공간 정도의 개념!!

'''
1. SMTP 메일 서버를 연결한다
2. SMTP 메일 서버에 로그인 한다
3. SMTP 메일 서버로 메일을 보낸다
'''

'''
MIME 사용하기
from email.message import EmailMessage
1. 이메일을 만든다.
 message = EmailMessage()
2. 이메일에 내용을 담는다.
 message.set_content("이메일 내용입니다.")
3. 발신자, 수신자를 설정한다.
'''

import smtplib
from email.message import EmailMessage
import imghdr   #이미지 확장자 자동 인식 기능
import re   # 유효성 검사 위한 모듈

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    # 유효성 검사를 위한 정규표현식 만들기
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        # 메일 전송하기
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

    

message = EmailMessage()
message.set_content("이메일 내용입니다.")

message["Subject"] = "이것은 사진이 담긴 메일의 제목입니다."
message["From"] = "mndnyn@gmail.com"
message["To"] = "mndnyn@likelion.org"

# smtplib.SMTP(서버주소, 포트번호)
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

# smtp.login(gmail계정, 계정비밀번호)
smtp.login("mndnyn@gmail.com", "BeLLa5813G!")

# 메일에 사진 첨부하기
# 파일 열고, open() & 읽어서 출력하기 read()
'''
image = open("minions.png", "rb")
print(image.read())
'''
# close 문 없이 파일 이용하고 닫기
with open("minions.png", "rb") as image:
    image_file = image.read()
    
# 메일에 무언가를 첨부하기 필요한 요소 "add_attachment() 함수 사용하기 ": image / maintype / subtype
image_type = imghdr.what('minions', image_file)
message.add_attachment(image_file, maintype ='image', subtype = image_type)

# 이메일 유효성 검사하기
# 1.형식
# ^[a-zA-Z0-9.+_-]+ @ [a-zA-Z0-9]+ \. [a-zA-Z]{2-3}$
# ^: 시작, $: 끝
# [a-zA-Z0-9.+_-]+ : 소문자, 대문자, 0부터 9, + _ - 다 올 수 있고, 이 조건들이 + : 반복될 수 있음
# \. : .을 의미
# [a-zA-Z]{2-3} : []안의 조건들 최소 2회, 최대 3회 반복 가능

# sendEmail 함수 이용해서 메일 보내기
sendEmail("mndnyn@likelion.org")
smtp.quit()