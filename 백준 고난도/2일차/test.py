
def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    a=0
    for i in words:
        for j in babbling:
            j = j.replace(i, " ")
            if not j.strip():
                a+=1
                break
    print(a)
solution(["aya", "yee", "u", "maa", "wyeoo"])