class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The solution I think I am going for here is this
        make a dictionary where it stores list
        sort the letters and store em in the dictionary
        """
        anagram_dict = dict()
        for i in strs:
            key = tuple(sorted(i))
            if key in anagram_dict:
                anagram_dict[key].append(i)
            else:
                anagram_dict[key] = [i]
        answer = []
        for k in anagram_dict:
            answer.append(anagram_dict[k])
        return answer