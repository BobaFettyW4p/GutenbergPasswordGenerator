import gutenbergpy.textget, string, random


#this function accepts one parameter, the BOOK_ID variable, and gets the full text.
def get_book(BOOK_ID) -> bytes:
    book = gutenbergpy.textget.get_text_by_id(BOOK_ID)
    return book

#this function takes the full text of the novel, and turns it into a full list that is a word dictionary used
#to create passwords
def clean_book(book) -> list:
    final_book = []
    clean_book = gutenbergpy.textget.strip_headers(book)
    clean_book = clean_book.decode()
    split = clean_book.split()
    final_book = [x.title() for x in split if len(x)>=4]
    final_book = set(final_book)
    final_book = list(final_book)
    return final_book

#This function uses the output of the above clean_book function, and generates a password with appropriate length
def create_candidates(final_book, PASSWORD_LENGTH) -> list:
    NUMBER_OF_PASSWORDS = 5
    password_candidates = []
    numbers = [*range(1,100)]
    characters = ['!','@','#','$','%','^','&','*','(',')','?','/']
    while len(password_candidates) < NUMBER_OF_PASSWORDS:
        password = ''
        while len(password) < PASSWORD_LENGTH - 3:
            choice = random.choice(final_book)
            valid_word = True
            for character in choice:
                if character in string.ascii_letters:
                    continue
                else:
                    valid_word = False
            if valid_word:
                password+=choice
        #selects a random choice from the numbers variable, if it's a single digit, add a leading 0
        digit_choice = random.choice(numbers)
        if digit_choice < 10:
            digit_choice=f'0{digit_choice}'
        password+=str(digit_choice)
        #adding a random special character to round out the password
        password+=random.choice(characters)
        password_candidates.append(password)
    return password_candidates
#BOOK_ID is keyed to Edward Gibbon's Decline and Fall of the Roman Empire, PASSWORD_LENGTH was chosen after some testing to determine what a good password looked like         
def generate_passwords(BOOK_ID=890,PASSWORD_LENGTH=20) -> list:
    book = get_book(BOOK_ID)
    final_book = clean_book(book)
    return create_candidates(final_book, PASSWORD_LENGTH)

