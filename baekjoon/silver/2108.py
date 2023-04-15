import sys
input = sys.stdin.readline


n = int(input())
li = []

for i in range(n):
    li.append(int(input()))

li = sorted(li)

# get frequency of elements in list
freq = {}
for item in li:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

# get the most frequent element
max_freq = max(freq.values())

# get all elements with max frequency
max_freq_el = [k for k, v in freq.items() if v == max_freq]

# if there is more than one element with max frequency, get the second smallest
if len(max_freq_el) > 1:
    max_freq_el = sorted(max_freq_el)[1]
else:
    max_freq_el = max_freq_el[0]


av = int(round(sum(li)/n, 0))
mid = li[int(n/2)]
ran = max(li) - min(li)

print(av)
print(mid)
print(max_freq_el)
print(ran)
