a,b = map(int, raw_input().split())
answer = 0

while True:
    if a == b:
        answer = a
        break

    if a < b:
        a,b = b,a

    a = a % b
    if a == 0:
        answer = b
        break

print answer
    
