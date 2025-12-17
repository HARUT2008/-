from collections import Counter  # Ներմուծում ենք Counter-ը՝ տարրերի հաճախականությունը հաշվելու համար


# Ֆունկցիա, որը վերադարձնում է նախադասության ամենաերկար բառը
def amenashat_nish_bare(sentence):
    
    # Նախադասությունը բաժանում ենք բառերի
    words = sentence.split()

    # Գտնում ենք ամենաերկար բառը ըստ երկարության
    max_word = max(words, key=len)

    # Վերադարձնում ենք ամենաերկար բառը
    return max_word


# Փորձնական նախադասություն
sentence = "Ծիրանենիի ծաղկունքը հրաշալ"

# Տպում ենք ամենաերկար բառը
print(amenashat_nish_bare(sentence))




# Ֆունկցիա, որը գտնում է նախադասության ամենաշատ օգտագործված տառը
def amenashat_ogtagorcvox_tar(nakhad):

    # Թողնում ենք միայն տառերը և դարձնում փոքրատառ
    only_letters = [char.lower() for char in nakhad if char.isalpha()]

    # Եթե տառ չկա, վերադարձնում ենք None
    if not only_letters:
        return None

    # Հաշվում ենք յուրաքանչյուր տառի քանակը
    count = Counter(only_letters)

    # Գտնում ենք ամենահաճախ հանդիպող տառը
    most_common = count.most_common(1)[0]

    # Վերադարձնում ենք (տառ, քանակ) զույգը
    return most_common


# Փորձնական նախադասություն
nakhad = "Ծիրանենի ծաղկունքը հրաշալի տեսարան է"

# Կանչում ենք ֆունկցիան
result = amenashat_ogtagorcvox_tar(nakhad)


# Ստուգում ենք արդյունքը և տպում
if result:
    tar, qanak = result
    print("Ամենաշատ օգտագործված տառն է՝ '{}', որը հանդիպել է {} անգամ։".format(tar, qanak))
else:
    print("Տառեր չեն գտնվել։")




# Ֆունկցիա, որը գտնում է ամենաերկար բառի մեջ ամենաշատ օգտագործված տառը
def erkar_bari_amenashat_tar(nakhad):

    # Նախադասությունը բաժանում ենք բառերի
    words = nakhad.split()

    # Եթե բառեր չկան, վերադարձնում ենք None
    if not words:
        return None

    # Գտնում ենք ամենաերկար բառը
    longest_word = max(words, key=len)

    # Մաքրում ենք բառը՝ թողնելով միայն տառերը
    cleaned_word = ''.join([ch.lower() for ch in longest_word if ch.isalpha()])

    # Եթե բառը դատարկ է, վերադարձնում ենք None
    if not cleaned_word:
        return None

    # Հաշվում ենք տառերի հաճախականությունը
    count = Counter(cleaned_word)

    # Գտնում ենք ամենահաճախ հանդիպող տառը
    most_common = count.most_common(1)[0]

    # Վերադարձնում ենք միայն տառը
    return most_common[0]


# Փորձնական նախադասություն
sentence = "Ծիրանենի ծաղկունքը հրաշալի տեսարան է"

# Կանչում ենք ֆունկցիան
result = erkar_bari_amenashat_tar(sentence)

# Տպում ենք արդյունքը
print("Ամենաշատ օգտագործված տառը ամենաերկար բառում՝", result)




# Ֆունկցիա, որը վերադարձնում է տողի n-րդ սկզբի և n-րդ վերջի սիմվոլները
def edge_elements(s: str, n: int):

    # Եթե n-ը սխալ է, վերադարձնում ենք None
    if n <= 0 or n > len(s):
        return None

    # Վերադարձնում ենք համապատասխան սիմվոլները
    return s[n - 1], s[-n]


# Փորձարկումներ
print(edge_elements("HelloWorld", 1))  # ('H', 'd')
print(edge_elements("HelloWorld", 3))  # ('l', 'r')




# Ֆունկցիա, որը ստուգում է՝ թիվը պալինդրոմ է, թե ոչ
def is_palindrome(num: int) -> bool:

    # Թիվը դարձնում ենք տող
    s = str(num)

    # Համեմատում ենք ուղիղ և հակադարձ տողերը
    return s == s[::-1]


# Փորձարկումներ
print(is_palindrome(121))    # True
print(is_palindrome(12321))  # True
print(is_palindrome(123))    # False




# Ֆունկցիա, որը գտնում է ամենամոտ պալինդրոմ թիվը
def nearest_palindrome(num: int) -> int:

    # Եթե թիվն արդեն պալինդրոմ է, վերադարձնում ենք այն
    if is_palindrome(num):
        return num

    # Սկսում ենք որոնումը երկու կողմերով
    lower = num - 1
    upper = num + 1

    # Անվերջ ցիկլ մինչև գտնենք պալինդրոմ
    while True:
        if lower >= 0 and is_palindrome(lower):
            return lower
        if is_palindrome(upper):
            return upper
        lower -= 1
        upper += 1


# Փորձարկումներ
print(nearest_palindrome(121))   # 121
print(nearest_palindrome(123))   # 121
print(nearest_palindrome(99))    # 99
print(nearest_palindrome(10))    # 9
print(nearest_palindrome(88))    # 88




# Ֆունկցիա, որը վերադարձնում է թվի առաջին և վերջին թվանշանների արտադրյալը
def product_first_last(num: int) -> int:

    # Վերցնում ենք թվի բացարձակ արժեքը և դարձնում տող
    s = str(abs(num))

    # Եթե թիվը մեկանիշ է
    if len(s) == 1:
        d = int(s[0])
        return d * d

    # Առաջին և վերջին թվանշանները
    first = int(s[0])
    last = int(s[-1])

    # Վերադարձնում ենք արտադրյալը
    return first * last


# Փորձարկումներ
print(product_first_last(1234))   # 4
print(product_first_last(5069))   # 45
print(product_first_last(7))      # 49
print(product_first_last(-987))   # 63




# Ֆունկցիա, որը հաշվում է ցուցակում եղած տողերի քանակը
def count_strings(lst: list) -> int:

    # Հաշվում ենք միայն str տիպի տարրերը
    return sum(1 for item in lst if isinstance(item, str))


# Փորձարկումներ
print(count_strings([1, "hello", 3, "world", True]))   # 2
print(count_strings(["a", "b", "c"]))                  # 3
print(count_strings([10, 20, 30]))                     # 0



from typing import Union  # Տիպերի միավորման համար


# Ֆունկցիա, որը վերադարձնում է ցուցակի առավելագույն թիվը
def max_number(lst: list) -> Union[int, float, None]:

    # Եթե ցուցակը դատարկ է
    if not lst:
        return None

    # Վերադարձնում ենք առավելագույն արժեքը
    return max(lst)


# Փորձնական տվյալներ
numbers = [3, 5.7, 2, 9, 4.2]

# Կանչում ենք ֆունկցիան
result = max_number(numbers)

# Տպում ենք արդյունքը
print("Max number is:", result)

