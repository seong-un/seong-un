T = int(input())
for t in range(T):
    recording = input().split()
    while True:
        cry = list(input().split())[-1]
        if cry == 'say?':
            print(*recording)
            break
        while True:
            try:
                recording.remove(cry)
            except:
                break