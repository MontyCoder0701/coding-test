import sys
input = sys.stdin.readline

v, e = map(int, input().split())  # v: 정점의 개수, e: 간선의 개수


def find_parent(parent, x):  # 부모 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])  # 경로 압축
    return parent[x]


def union_parent(parent, a, b):  # 두 부모 노드를 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a  # 작은 값으로 합치기
    else:
        parent[a] = b


parent = [0] * (v+1)  # 부모 테이블 초기화
edges = []  # 모든 간선을 담을 리스트
result = 0  # 최종 비용

for i in range(1, v+1):  # 부모 테이블 상에서 부모를 자기 자신으로 초기화
    parent[i] = i

for _ in range(e):  # 모든 간선에 대한 정보를 입력받기
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정

edges.sort()  # 간선을 비용순으로 정렬

for edge in edges:  # 간선을 하나씩 확인하며
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):  # 사이클이 발생하지 않는 경우에만 집합에 포함
        union_parent(parent, a, b)  # 집합에 포함
        result += cost  # 최소 신장 트리에 포함되는 간선의 비용 더하기

print(result)
