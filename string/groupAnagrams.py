class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        table = defaultdict(lambda : [])
        for st in strs:
            table["".join(sorted(st))] += [st]
        return [table[x] for x in table]