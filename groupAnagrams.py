class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a HashMap for return list
        groups_dict = {}

        # Loop thru words
        for word in strs:
            # key - serves as a sorted word in alphabet order
            key = "".join(sorted(word))
            if key in groups_dict:
                # if found the key, add the word
                groups_dict[key].append(word)
            else:
                # unless, create a list for it
                groups_dict[key] = [word]
        # return group_dict with entirety as a list
        return list(groups_dict.values())
