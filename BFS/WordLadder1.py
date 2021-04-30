import functools
from typing import List
from collections import deque
from collections import defaultdict


class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_keys = defaultdict(lambda: [])

        # Should preprocess all words in the world list
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                word_keys[key].append(word)

        queue = deque([(1, beginWord, None)])
        max_distance = None
        visited = set()
        while queue:
            distance, word, prev_word = queue.popleft()
            visited.add(word)

            for i in range(len(word)):
                wildcard = word[:i] + "*" + word[i + 1:]
                words = word_keys[wildcard]
                for possible_word in words:
                    if possible_word == endWord:
                        if max_distance is None:
                            max_distance = distance + 1
                        elif distance + 1 == max_distance:
                            pass

                    if possible_word not in visited and (max_distance is None or distance + 1 <= max_distance):
                        queue.append((distance + 1, possible_word, word))

        return 0 if max_distance is None else max_distance


solution = Solution()

result = solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(result)
