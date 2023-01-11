import string
import pytest
import gutenbergpy.textget
import gutenbergPasswordGenerator


@pytest.fixture
def sample_text():
    book = gutenbergpy.textget.get_text_by_id(890)
    return book


@pytest.fixture
def sample_dictionary():
    book = gutenbergPasswordGenerator.get_book(890)
    final_book = gutenbergPasswordGenerator.clean_book(book)
    return final_book


def test_get_book(sample_text):
    assert type(gutenbergPasswordGenerator.get_book(890)) is bytes


def test_clean_book_type(sample_text):
    assert type(gutenbergPasswordGenerator.clean_book(sample_text)) is list


def test_clean_book_word_length(sample_text):
    book = gutenbergPasswordGenerator.clean_book(sample_text)
    valid = True
    for page in book:
        if len(page) < 4:
            valid = False
            break
    assert valid


def test_capitalizaton_clean_book(sample_text):
    book = gutenbergPasswordGenerator.clean_book(sample_text)
    valid = True
    for page in book:
        if page[0] in string.ascii_lowercase:
            valid = False
            break
    assert valid


def test_clean_book_uniqueness(sample_text):
    book = gutenbergPasswordGenerator.clean_book(sample_text)
    valid = True
    for word in book:
        if book.count(word) != 1:
            valid = False
            break
    assert valid


def test_create_candidates_number(sample_dictionary):
    PASSWORD_LENGTH = 20
    candidates = gutenbergPasswordGenerator.create_candidates(
        sample_dictionary, PASSWORD_LENGTH
    )
    assert len(candidates) == 5


def test_create_candidates_two_digits(sample_dictionary):
    PASSWORD_LENGTH = 20
    candidates = gutenbergPasswordGenerator.create_candidates(
        sample_dictionary, PASSWORD_LENGTH
    )
    valid = True
    for candidate in candidates:
        digits = [x for x in candidate if x.isdigit()]
        if len(digits) != 2:
            valid = False
    assert valid


def test_create_candidates_password_length(sample_dictionary):
    PASSWORD_LENGTH = 20
    candidates = gutenbergPasswordGenerator.create_candidates(
        sample_dictionary, PASSWORD_LENGTH
    )
    valid = True
    for candidate in candidates:
        if len(candidate) < PASSWORD_LENGTH:
            valid = False
    assert valid


def test_create_candidates_contains_special_character(sample_dictionary):
    PASSWORD_LENGTH = 20
    candidates = gutenbergPasswordGenerator.create_candidates(
        sample_dictionary, PASSWORD_LENGTH
    )
    valid = True
    for candidate in candidates:
        valid = False
        for character in candidate:
            if character not in string.ascii_letters or not character.isdigit():
                valid = True
                break
        if not valid:
            assert valid
    assert valid
