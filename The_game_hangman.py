old_letters_guessed = []
MAX_TRIES = 6
num_of_tries = 0
HANGMAN_PHOTOS = {
0:'x-------x',
1:"""x-------x
|
|
|
|
|""",
2:"""x-------x
|       |
|       0
|
|
|""",
3:"""x-------x
|       |
|       0
|       |
|
|""",
4:"""x-------x
|       |
|       0
|      /|\\
|
|""",
5:"""x-------x
|       |
|       0
|      /|\\
|      /
|""",
6:"""x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}

def welcome_screen():
    """
    This function show hangman welcome screen.
    :return: the welcome screen with the max tries the user can try
    :rtype: str
    """
    HANGMAN_IMAGE = """ _    _                                         
| |  | |                                        
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/
%d""" %(MAX_TRIES)
 
    return HANGMAN_IMAGE

def show_hidden_word(secret_word, old_letters_guessed):
    """
    This function gets a word, gets letters from the user and checks if the letters show in the word.
    :param secret_word: the word the user need to guess
    :param old_letters_guessed: the letters the user guess
    :type secret_word: str
    :type old_letters_guessed: list
    :return: the word the user need to guess only with the letters he right
    :rtype: str
    """
    show_word = ""
    
    for i in secret_word:
        if i in old_letters_guessed:
            show_word += i + " "
        else:
            show_word += "_ "
    
    return show_word
    
def check_win(secret_word, old_letters_guessed):
    """
    This function check if the user guessed the secret word.
    :param secret_word: the word the user need to guess
    :param old_letters_guessed: the letters the user input
    :type secret_word: str
    :type old_letters_guessed: list
    :return: if the user succeed to guess the word    
    :rtype: bool
    """
    return "".join(show_hidden_word(secret_word, old_letters_guessed).split()) == secret_word  

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function checks if the letter the user guessed is valid.
    :param letter_guessed: the letter the user enter
    :param old_letters_guessed: a list of all the letters the user guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: if the letter is not valid False, else True
    :rtype: bool
    """
    if (len(letter_guessed) > 1) or (not(letter_guessed.isalpha())) or (letter_guessed in old_letters_guessed):
        return False
    else:
        old_letters_guessed += [letter_guessed]
        return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function checks if the letter the user enter is valid.
    :param letter_guessed: the letter the user guessed
    :param old_letters_guessed: the letters the user guessed before
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: None (the function is print)
    :rtype: None
    """
    if (len(letter_guessed) > 1) or (not(letter_guessed.isalpha())) or (letter_guessed in old_letters_guessed):
        print("X")
        print(" -> ".join(sorted(old_letters_guessed))) if len(old_letters_guessed) > 0 else None
    else:
        old_letters_guessed += [letter_guessed]

def choose_word(file_path, index):
    """
    This function gets a index that point to a word from the text file, if the index is bigger then the amount of the words the function counts from the beginning again.
    :param file_path: a text file includes words that separated by spaces
    :param index: The index the user enter to choose a word from the text file
    :type file_path: str
    :type index: int
    :return: the word the index the user enter point
    :rtype: str
    """
    global secret_word
    file_path_read = file_path.read()
    file_path_read = file_path_read.split(' ')
    
    while (index >= len(file_path_read)):
        index %= len(file_path_read)
    secret_word = file_path_read[index - 1]
    
    return secret_word
    file_path.close()

def wrong_letter():
        """
        This function shows to the user that the user wrong and shows the hangman one level up and how much he guessed the secret word.
        :return: None(the function is print)
        :rtype: None
        """
        print(':(\n')
        print(HANGMAN_PHOTOS[num_of_tries + 1], '\n')
        print(show_hidden_word(secret_word, old_letters_guessed))

def main():
    global num_of_tries
    global show_word
    
    print(welcome_screen(), '\n')
    file_path = open(input(r"Please enter a txt file path: "), "r")
    index = int(input("Please enter the index for the word: "))
    choose_word(file_path, index)
    print("\nLet's start!\n")
    print(HANGMAN_PHOTOS[0], '\n')
    print('_ ' * len(secret_word), '\n')
    
    while num_of_tries < MAX_TRIES:
        letter_guessed = input("Guess a letter: ").lower()
        if check_valid_input(letter_guessed, old_letters_guessed):
            if letter_guessed in secret_word:
                print(show_hidden_word(secret_word, old_letters_guessed))
                if check_win(secret_word, old_letters_guessed):
                    print('WIN!!!')
                    break
            else:
                if num_of_tries == 5:
                    wrong_letter()
                    print('LOSE')
                    break
                else:
                    wrong_letter()
                    num_of_tries += 1                
        else:
            try_update_letter_guessed(letter_guessed, old_letters_guessed)

if __name__ == '__main__':
    main()