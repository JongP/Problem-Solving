class Solution:
    #failed to implement completely
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        
        conversion_mappings = dict()
        unique_characters_in_str2 = set()
        
        # Make sure that no character in str1 is mapped to multiple characters in str2.
        for letter1, letter2 in zip(str1, str2):
            if letter1 not in conversion_mappings:
                conversion_mappings[letter1] = letter2
                unique_characters_in_str2.add(letter2)
            elif conversion_mappings[letter1] != letter2:
                # letter1 maps to 2 different characters, so str1 cannot transform into str2.
                return False
        
        
        if len(unique_characters_in_str2) < 26:
            # No character in str1 maps to 2 or more different characters in str2 and there
            # is at least one temporary character that can be used to break any loops.
            return True
        
        # The conversion mapping forms one or more cycles and there are no temporary 
        # characters that we can use to break the loops, so str1 cannot transform into str2.
        return False