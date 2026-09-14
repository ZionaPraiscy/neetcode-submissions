class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}

        for i in strs :

            key = tuple(sorted(Counter(i).items()))

            if key not in group :
                group[key] = []
            group[key].append(i)
        return list(group.values())