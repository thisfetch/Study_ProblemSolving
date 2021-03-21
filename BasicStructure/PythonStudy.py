# abs = 절대값, pow(n, m) = n의 m 승, round = 반올림
# from math import * => math 라이브러리 사용 가능
# floor = 내림, ceil = 올림, sqrt = 제곱근
# from random import * => 난수 생성, print(random()) => 0.0 ~ 1.0 미만의 임의의 값, * 10 하면 0.0 ~ 10.0 임의의 값
# print(int(random())) => integer값 생성
# print(int(random() * 10) + 1) => 소수점 제거
# print(randrage(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1, 45))

# 슬라이싱 => print("성별 : " + jumin[7]) => 한글자
# jumin[0:2] => 0부터 2 직전까지 (0,1), jumin[:6] -> 처음부터 6직전까지, jumin[7:] => 7부터 끝까지
# jumin[-7:] => 맨뒤에서 7번째부터 끝까지
# python = "Python is Amazing", python.lower() => 소문자 출력, python.upper() 대문자 출력
# python[0].isupper() => 1번째 글자가 대문자인가 아닌가 , len(python) => 문자열 길이
# python.replace("Python", "Java") => Python 찾아서 java로 바꿔줌 , index = python.index("n") => 인덱스 찾아주기 
# python.index("n", index + 1) => 이면 맨 앞 n 말고 두번째 n
# python.find("n") => n 위치 알려줌 , 없으면 -1 return... index는 없으면 Error

# print("나는 %d살입니다." % 20), print("나는 %s를 좋아해요" % "파이썬") print("Apple은 %c로 시작해요." % "A")
# %s만 쓰면 문자열 만능이다... print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# print("나는 {}살입니다.".format(20)), print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
# v3.6 이상 가능 => age = 20 color = "빨간" print(f"나는 {age}살이며, {color}색을 좋아해요.")
# \n => 줄바꿈 , \" => 큰따옴표 \' => 작은따옴표 \\ -> 문장 내 \.. \r => 커서를 맨 앞으로 이동 \b => 백스페이스 
# \t => 탭, 

# subway = [10, 20, 30], subway.index(20) => 1; subway.append(40) => 뒤에 배열 요소 추가 
# subway.insert(1, 15) => 1번째 자리에 요소 추가 나머지 요소 밀림
# subway.pop() => 맨 마지막 요소 POP, subway.count(10) => 같은 값이 몇 명 나오는지
# num_list = [5, 2, 4, 3, 1] => num_list.sort() => 오름차순 정렬, num_list.reverse() => 배열 뒤집기 
# num_list.clear() => 배열 모두 지우기, mix_list = ["조세호", 20, true] => 다양한 자료형 함께 사용
# num_list.extend(mix_list) => 배열 합치기.. ㄷㄷ 

# dictionary => key 중복 허용x
# cabinet = {key : value, key: value} => 이런 식으로 구성, print(cabinet[key]) => dict 출력
# print(cabinet.get(key))도 가능, cabinet[ne_key] => 없는 키는 예외처리 후 프로그램 종료, get은 None 문자만 return
# cabinet.get(ne_key, "사용 가능") => 없으면 사용 가능 출력, key in cabinet => key 유무에 따라 t or f return
# key 값은 string도 가능 , key에 value 바꾸기도 가능, key value 추가도 가능 del cabinet[key] => key와 value 모두 삭제
# key 들만 출력 => cabinet.keys(), value들만 출력 => cabinet.values() 쌍으로 출력 => cabinet.items()
# cabinet.clear() => 모든 key, value 삭제

# tuple => list 와는 다르게 변경 수정 x but 속도 빠르다
# menu = ("돈까스", "치즈까스") => 여기서 추가 변경 불가능 (name, age, hobby) = ("김종국", 20, "코딩") 가능

# set 중복 안되고 순서 없음
# my_set = {1, 2, 3, 3, 3} => dict와 달리 값만 나열할 수 있삼 1, 2, 3 출력, 중복 허용이 안되기 때문에
# java = {"유재석", "김태호", "양세형"} , python = set(["유재석", "박명수"]) java & python => 교집합
# java.intersection(python) => 교집합, java. | python or java.union(python) => 합집합
# java - python, java.difference(python) => 차집합 , python.add("김태호") => set에 값 추가 
# java.remove("김태호") => 김태호 제거
# menu = {"커피", "우유", "주스"}, menu = list(menu) => 타입의 형 변환, tuple(menu), set(menu)도 가능...

# 입력 temp  = input("기온은 어떄요?") => 항상 문자열인데 int(intput())은 integer로 바꿔준다.

# for waiting_no in [0, 1, 2, 3, 4]: print("대기번호 : {0}".format(waiting_no))
# for waiting_no in range(5) => 0, 1, 2, 3, 4 for waiting_no in range(1, 6) => 1, 2, 3, 4, 5
# for customer in starbucks: => foreach문

# while index >= 1:

# stuents = [1,2,3,4,5] print(students) students = [i + 100 for i in students] 이런식으로 한 줄 for 가능
# students = ["Iron man", "Thor", "I am groot"] students = [len(list) for list in students]
# studnets = [i.upper() for i in students]

# def open_account(): => 함수 선언
# def deposit(balance, money): print("입금 되었고 잔액은 {0}원 입니다.".format(balance + money)) return balance + money;

# 표준 입출력
# print("Python", "Java", "JavaScript", sep=" vs ") => Python vs Java vs JavaScript
# print("Python", "Java", sep="," , end ="?") => Python vs Java?
# import sys
# print("Python", "Java", file=sys.stdout) => 표준출력 stderr => 표준에러?
# scores = {"수학": 0, "영어":50, "코딩":100} for subject, score in scores.items(): 
# print(subject.ljust(8), str(score)rjust(4), sep=":") 

# for num in range(1, 21): print("대기번호 : " + str(num).zfill(3)) => 001 002,003..
# answer = input("아무 값이나 입력하세요 : ") print("입력하신 값은 " + answer) => 출력은 모두 문자열

# 예외처리는 try except 문으로 ... excpet ~~ as err : print(err) ,, raise를 써서 err 발생 가능
# try : 
#     num = int(input())
# except ValueError as err : print(err)
    