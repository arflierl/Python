def letters_advanced_3(x: str) -> str:

    import string

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    increase = 3
    answer = ""

    for ch in x:
        if not ch.isalpha():
            answer += ch
        elif ch in lowercase:
            answer += lowercase[(lowercase.index(ch) + increase) % 26]
        elif ch in uppercase:
            answer += uppercase[(uppercase.index(ch) + increase) % 26]

    print(answer)
    return answer

letters_advanced_3(str(input("Please enter a word or phrase: ")))
