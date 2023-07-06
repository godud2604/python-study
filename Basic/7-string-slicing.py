# slicing
# => a 라는 연속적인 객체들의 자료구조(ex: 리스트, 튜플, 문자열)가 있다고 가정
# => a[start: end: step]
# => start: 슬라이싱을 시작할 시작 위치
# => end: 슬라이싱을 끝낼 위치로 end는 포함하지 않음,
# => step: stride(보폭)라고도 하며 몇 개씩 끊어서 가져올지와 방향을 정한다.

name = "Bro Code"
first_name = name[:3]
last_name = name[4:]
funky_name = name[0:8:3]
reserved_name = name[::-1] 

print(first_name)
print(last_name)
print(funky_name) # B d
print(reserved_name) # edoC orB

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])