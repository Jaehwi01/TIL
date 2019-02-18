
## 1 ##
class Word:
    def __init__(self):
        self.wordbook = {}

    def add(self, en, ko):
        self.wordbook.update({en:ko})
        # self.wordbook[en]=ko
        
    def delete(self, en):
        if en in self.wordbook:
            self.wordbook.pop(en)
            # del self.wordbook[en]
            return True
        else:
            return False

    def print(slef):
        for en, ko in self.workdbook.items():
          print(f'{en}:{ko}')


## 2 ##

class Point:
    def __init__(self):
        self.x=x
        self.y=y

class Rectangle:
    def __init__(self, a, b):
        self.p1 = a
        self.p2 = b
    
    def get_area(slef):
        w = self.p2.x - self.p1.x
        h = self.p1.y - self.p2.y
        return w*h
    def get_perimeter(self):
        w = self.p2.x - self.p1.x
        h = self.p1.y - self.p2.y
        return (w+h)*2
    def is_square(self):
        w = self.p2.x - self.p1.x
        h = self.p1.y - self.p2.y
        if w == h:
            return True
        else:
            return False


## 3 - 1 ##

def alphabaet_count(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

## 3 - 2

def alphabaet_count(word):
    result = {}
    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    max_count = max(result.values())

    for char, count in result.items():
        if max_count == count:
            return char


## 4 ## 

def cipher(word, n):
    result = ''

    # n >= 26인 경우 처리
    n= n % 26 # 26 % 26 == 1  or 26보다크면 -26?

    for char in word:  # 1. a
        w = ord(char) + n  # w= 97(a) + 1 

        # z를 넘어갔을 경우 처리
        if w > 122:  #ord('z')==122
            w = w - 26

        result += chr(w) # chr(98) == 'b'
    return result

# 다른 방법#
result += chr((ord(char)-97+n) % 26 + 97)
#ex) z -> (122-97 +2) % 26 +97 == 98 -> b