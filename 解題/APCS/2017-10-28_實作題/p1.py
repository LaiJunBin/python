while True:
    a,b,c = list(map(lambda x: bool(int(x)),input().split(' ')))
    answer = []
    if (a and b) == c:
        answer.append('AND')
    if (a or b) == c:
        answer.append("OR")
    if (a ^ b) == c:
        answer.append("XOR")
    print("IMPOSSIBLE") if len(answer)==0 else print('\n'.join(answer))
