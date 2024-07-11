# 请实现一个wordcount函数，统计英文字符串中每个单词出现的次数。返回一个字典，key为单词，value为对应单词出现的次数。

def wordcount(text):
    # 先将字符串转换为小写，然后用空格分隔单词
    words = text.lower().split()
    # 定义一个字典，用于存储单词出现的次数
    count = {}
    # 遍历单词列表，统计每个单词出现的次数
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count    

text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

result = wordcount(text)
print(result)     


