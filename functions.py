
t = "testcase"


def dollarizer(word):
    # Replace every 's' with '$'
    result = word.replace('s','$')
    return result

def eurizer(word):
    # Replace every 'e' with '3'
    result = word.replace('e','3')
    return result

def replacer(word, char_to_replace, replacement_char):
    """
    Replace every occurrence of char_to_replace in word with replacement_char.
    
    Parameters:
    - word (str): The input word in which replacements are to be made.
    - char_to_replace (str): The character to replace.
    - replacement_char (str): The character to replace with.
    
    Returns:
    - str: The word with the replacements made.
    """
    # Ensure char_to_replace and replacement_char are single characters
    # if len(char_to_replace) != 1 or len(replacement_char) != 1:
    #     raise ValueError("Both char_to_replace and replacement_char must be single characters.")
    
    # Perform the replacement
    result = word.replace(char_to_replace, replacement_char)
    return result

# Example usage
input_word = t
char_to_replace = 's'
replacement_char = '$'
output_word = replacer(input_word, char_to_replace, replacement_char)
print(output_word)  # Output: te$tca$e

# Another example with 'e' replaced by the Euro sign
input_word_eur = t
char_to_replace_eur = 'e'
replacement_char_eur = '€'
output_word_eur = replacer(input_word_eur, char_to_replace_eur, replacement_char_eur)
print(output_word_eur)  # Output: t€stcas€

def wonky_text(word):
    word = dollarizer(t)
    word = eurizer(t)
    return word

# example
input_word_wonky = t
output_word_wonky = wonky_text(input_word_wonky)
print(output_word_wonky)



print(f"Dollarizer: {dollarizer(t)}")
print(f"Eurizer: {eurizer(t)}")
print(f"replacer: {replacer(t)}")
print(f"Wonky Text: {wonky_text(t)}")