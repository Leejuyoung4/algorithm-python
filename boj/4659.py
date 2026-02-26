vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()
    if word == 'end':
        break
    
    status = True

    # 1. 모음 포함 여부 확인
    has_vowel = False
    for w in word:
        if w in vowels:
            has_vowel = True
            break
    
    if has_vowel == False:
        status = False

    # 2. 모음 3개 연속 or 자음 3개 연속 확인
    for i in range(len(word) - 2):
        if (word[i] in vowels and word[i + 1] in vowels and word[i + 2] in vowels) or (word[i] not in vowels and word[i + 1] not in vowels and word[i + 2] not in vowels):
            status = False

    # 3. 같은 글자 연속 확인   
    for i in range(len(word) - 1):
        if word[i] != 'o' and word[i] != 'e':
            if word[i] == word[i + 1]:
                status = False

    if status == True:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")