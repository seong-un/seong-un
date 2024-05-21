N = int(input())

first_word = input()
similar_word = 0
for n in range(N-1):
    compare_word = list(input())
    error = 0
    for alphabet in first_word:
        try:
            compare_word.remove(alphabet)
        except:
            error += 1

    if len(compare_word) > 1 or error > 1:
        continue

    similar_word += 1

print(similar_word)