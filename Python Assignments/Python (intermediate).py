'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if ord(letter)==32:
        return " "
    elif ord(letter)+shift>90:
        while ord(letter)+shift>90:
           shift=shift-26
        return chr(ord(letter)+shift)
    elif ord(letter)+shift<=90:
        return chr(ord(letter)+shift)

    
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shiftedstring=''
    value=shift
    
    for i in message:
        
        if ord(i)==32:
            shiftedstring=shiftedstring+' '
        elif ord(i)+shift>90:
            while ord(i)+value>90:
               value=value-26
            shiftedstring=shiftedstring+chr(ord(i)+value)
        elif ord(i)+shift<=90:
            shiftedstring=shiftedstring+chr(ord(i)+shift)
            
    return shiftedstring


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if ord(letter)==32:
        return " "
    elif ord(letter)-65 + ord(letter_shift)-65>25:
        return chr(ord(letter)-65 + ord(letter_shift)-26)
    elif ord(letter)-65 + ord(letter_shift)-65<=25:
        return chr(ord(letter)-65 + ord(letter_shift))

    
def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    keycode=[]
    messagecode=[]
    combinedcode=[]
    answer=''
    key_letters=(len(message)//len(key))*key + key[0:len(message)%len(key)]
    
    for y in range(0,len(message)):
        messagecode.append(ord(message[y])-65)
    for x in range(0,len(key_letters)):
        keycode.append(ord(key_letters[x])-65)
    for z in range (0,len(messagecode)):
        if messagecode[z]==-33:
            combinedcode.append(messagecode[z])
        elif messagecode[z]+keycode[z]>25:
            combinedcode.append(messagecode[z]+keycode[z]-26)
        elif messagecode[z]+keycode[z]<=25:
            combinedcode.append(messagecode[z]+keycode[z])
            
    for a in range(0,len(combinedcode)):
        answer=answer+chr(combinedcode[a]+65)
        
    return answer
