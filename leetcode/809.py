from typing import List


# 数据结构
# [('s',3),('a',2),('s',5)]

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s_w = self.func(s)
        c = 0
        for word in words:
            s_word = self.func(word)
            if len(s_word) != len(s_w):
                continue

            for a, b in zip(s_w, s_word):
                if a[0] != b[0]:
                    break
                if a[1] < b[1]:
                    break
                elif a[1] == b[1]:
                    pass
                else:
                    if a[1] >= 3:
                        pass
                    else:
                        break
            else:
                c += 1
        return c

    def func(self, word):
        data = []
        char = None
        for i in word:
            if i != char:
                char = i
                data.append([i, 1])
            else:
                data[-1][1] += 1
        return data


if __name__ == '__main__':
    print(Solution().expressiveWords(s="heeellooo",
                                     words=["hello", "hi", "helo"]))
