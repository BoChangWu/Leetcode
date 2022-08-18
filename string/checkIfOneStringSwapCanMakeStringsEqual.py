class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_indices = []
        for i, (ch1, ch2) in enumerate(zip(s1, s2)):
            if ch1 != ch2:
                diff_indices.append(i)
                if len(diff_indices) > 2:
                    return False
        if len(diff_indices) == 0:
            return True
        if len(diff_indices) == 1:
            return False
        first_idx, second_idx = diff_indices
        return set([s1[first_idx], s1[second_idx]]) == set([s2[first_idx], s2[second_idx]])