class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}

        for word in strs:

            if "".join(sorted(word)) in hash_map:

                hash_map["".join(sorted(word))].append(word)

            else:

                hash_map["".join(sorted(word))] = []
                hash_map["".join(sorted(word))].append(word)

        return list(hash_map.values())
        