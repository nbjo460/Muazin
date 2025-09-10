keywords = ["abc", "abc edf", "12 34", "12 34", "abcedf", "1234"]
text = "abc edf"
sum_commons = {}

for word in keywords:
    sum_commons[word] = text.count(word)

print(sum_commons)