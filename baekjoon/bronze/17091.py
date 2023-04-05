h = ["one", "two", "three", "four", "five", "six", "seven",
     "eight", "nine", "ten", "eleven", "twelve"]
m = ["one minute", "two minutes", "three minutes", "four minutes", "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes", "ten minutes", "eleven minutes", "twelve minutes", "thirteen minutes", "fourteen minutes", "quarter",
     "sixteen minutes", "seventeen minutes", "eighteen minutes", "nineteen minutes", "twenty minutes", "twenty one minutes", "twenty two minutes", "twenty three minutes", "twenty four minutes", "twenty five minutes", "twenty six minutes", "twenty seven minutes",
     "twenty eight minutes", "twenty nine minutes", "half"]

hour = int(input())
hour = hour % 12  # 12시간제로 바꿔줌

minute = int(input())

if minute == 0:
    ans = h[hour-1] + " o' clock"
elif minute >= 1 and minute <= 30:
    ans = m[minute-1] + " past " + h[hour-1]
elif minute == 60:  # 60분일 경우 0분으로 바꿔줌
    ans = h[hour] + " o' clock"
else:
    minute = 60 - minute
    ans = m[minute-1] + " to " + h[hour]

print(ans)
