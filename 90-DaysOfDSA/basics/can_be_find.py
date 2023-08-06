str1 = "geekforgeeks"
str2 = "geeeek"
def can_find(str1, str2):
    count= {}
    for char in str1:
        count[char] = count.get(char, 0)+1

    for char in str2:
        if char not in count or count[char] == 0:
            return False
        count[char]-=1

    return True

print(can_find(str1, str2))


    