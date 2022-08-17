def checkInclusion(self, s1: str, s2: str) -> bool:
		# if s1 is smaller then just return False
        if len(s1) > len(s2):
            return False
		# Get the length of s1, so we can find the same length of sub string in s2
        s1_len = len(s1)
        s1_dict = {}
        s2_dict = {}
		# Loop through s1 and make it a dictionary
		# Loop the same size in s2. Also make it a dictionary so we can later add/remove items
        for i in range(0, len(s1)):
            if s1[i] in s1_dict:
                s1_dict[s1[i]] += 1
            else:
                s1_dict[s1[i]] = 1
            if s2[i] in s2_dict:
                s2_dict[s2[i]] += 1
            else:
                s2_dict[s2[i]] = 1
		# If the first substring of s2 equals to s1, just return True
        if s1_dict == s2_dict:
            return True
		# Then we want to loop the rest part of s2, keep adding item in s2_dict and remove the one that is no longer part of the sub-string
        for j in range(len(s1), len(s2)):
            if s2[j] in s2_dict:
                s2_dict[s2[j]] += 1
            else:
                s2_dict[s2[j]] = 1
            old = s2[j-len(s1)]
            s2_dict[old] -= 1
            if s2_dict[old] <= 0:
                del s2_dict[old]
			# For each loop, compare the updated s2_dict with s1
            if s1_dict == s2_dict:
                return True
        return False