class TikTokInterview:

    # Return the first mismatched character in the two lists.
    # The lists are not sorted.
    # There is only one mismatch.
    # The lists might be of equal length, or one of them might be 1 character longer.
    # Lists might contain duplicates.
    #
    # Example input: arr1 = ['a', 'b', 'c', 'd'], arr2 = ['a', 'b', 'c', 'e']
    # Example output: 'e'
    #
    # Example input: arr1 = ['a', 'b', 'c'], arr2 = ['a', 'b', 'c', 'c']
    # Example output: 'c'
    #
    # Example input: arr1 = ['a', 'b', 'c', 'c'], arr2 = ['a', 'c', 'b']
    # Example output: 'c'

    def find_mismatch(self, arr1: [str], arr2: [str]) -> str:
        dict_arr1 = {}
        for letter in arr1:
            dict_arr1[letter] = 1 + dict_arr1.get(letter, 0)

        for letter in arr2:
            if letter in dict_arr1 and dict_arr1[letter] > 1:
                dict_arr1[letter] -= 1
            elif letter in dict_arr1 and dict_arr1[letter] == 1:
                dict_arr1.pop(letter)
            elif letter not in dict_arr1:
                return letter
        return list(dict_arr1.keys())[0]
