# 교점에 별 만들기

# 시도 1: 시간 초과
def solution(line):
    pos, answer = [], [] # pos: 교점의 좌표, answer: 출력할 결과
    n = len(line) # 선의 개수

    x_min = y_min = 1000000000 # 최대값으로 초기화
    x_max = y_max = -1000000000 # 최소값으로 초기화

    for i in range(n):
        a, b, e = line[i]
        for j in range(i + 1, n): # i+1부터 n까지 (중복 제거)
            c, d, f = line[j]
            if a * d - b * c == 0: continue
            x = (b * f - e * d) / (a * d - b * c) # 교점의 x좌표
            y = (e * c - a * f) / (a * d - b * c) # 교점의 y좌표

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x, y])

                if x_min > x: x_min = x # 최소값 갱신
                if x_max < x: x_max = x # 최대값 갱신

                if y_min > y: y_min = y # 최소값 갱신 
                if y_max < y: y_max = y # 최대값 갱신

    x_len = x_max - x_min + 1 # x좌표의 길이 (최대값 - 최소값 + 1 = 길이)
    y_len = y_max - y_min + 1 # y좌표의 길이 (최대값 - 최소값 + 1 = 길이)
    coord = [['.'] * x_len for _ in range(y_len)] # 좌표평면

    for star_x, star_y in pos: 
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min # x좌표의 최소값이 0보다 작으면 절대값을 더해줌 (좌표평면의 x좌표는 0부터 시작하기 때문)
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min # y좌표의 최소값이 0보다 작으면 절대값을 더해줌 (좌표평면의 y좌표는 0부터 시작하기 때문)
        coord[ny][nx] = '*'

    for result in coord: answer.append(''.join(result)) # 출력할 결과에 좌표평면을 문자열로 변환하여 추가

    return answer[::-1] # 좌표평면을 뒤집어서 반환 (문제에서는 y좌표가 아래에서부터 시작하기 때문)

# 시도 2: 간소화
def solution(line):
    pos = []  

    for i in range(len(line)): # 불필요한 변수 n 제거
        a, b, e = line[i]
        for j in range(i + 1, len(line)):
            c, d, f = line[j]
            if a * d - b * c == 0: continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            if x.is_integer() and y.is_integer(): # is_integer() 대체
                pos.append((int(x), int(y))) # 넣을때에만 type 변환

    x_min = min(pos, key=lambda p: p[0])[0]  # min(), max() 대체, lambda는 x좌표를 기준으로 최소값, 최대값을 찾음
    x_max = max(pos, key=lambda p: p[0])[0]  
    y_min = min(pos, key=lambda p: p[1])[1]  
    y_max = max(pos, key=lambda p: p[1])[1]  

    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for _ in range(y_len)]

    for star_x, star_y in pos:
        nx = star_x - x_min # 절대값을 더해주는 과정을 제거 (star_x - x_min는 0 이상이기 때문)
        ny = star_y - y_min
        coord[ny][nx] = '*' 

    return [''.join(result) for result in coord[::-1]] # join 사용함 (answer 변수 제거)
