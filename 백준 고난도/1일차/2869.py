A, B, V = map(int,input().split())#


result = (V-A)//(A-B) + 1

print(result)
# V-A / A-B : 도착하면 더해지면 안되니깐 V-A 그리고 A-B 하루에 올라가는 값에 최종으로 올라가야하는 값을 나누면 일수가 나옴.