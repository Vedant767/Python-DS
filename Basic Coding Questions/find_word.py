def count(str1):
    # print("Hello")
    dict = {}
    for key in str1:
        if key in dict:
            dict[key] +=1
        else:
            dict[key] = 1
    return dict


def find(str1, str2):
    if len(str2) != len(str1):
        return False
    
    return count(str1) == count(str2)

print(find("abca","aaaa"))