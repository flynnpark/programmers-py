def solution(phone_book: list[str]):
    phone_book.sort()
    for index, number in enumerate(phone_book, 0):
        if number.startswith(phone_book[index - 1]):
            return False

    return True
