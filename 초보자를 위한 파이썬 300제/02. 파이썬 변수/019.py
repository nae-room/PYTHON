# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다.
# 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.

# year = "2020"

year = "2020"
int_year = int(year)
print(int_year-3)
print(int_year-2)
print(int_year-1)

''' 답안
print(int(year)-3)  # 2017
print(int(year)-2)  # 2018
print(int(year)-1)  # 2019
'''