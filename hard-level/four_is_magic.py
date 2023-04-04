# Write a function that takes an integer number and returns an English text sequence starting with the
# English cardinal representation of that integer, the word 'is' and then the English cardinal representation of the
# count of characters that made up the first word, followed by a comma. Continue the sequence by using the previous
# count word as the first word of the next phrase, append 'is' and the cardinal count of the letters in that word.
# Continue until you reach four. Since four has four characters, finish by adding the words 'four is magic'
# and a period. All integers will eventually wind up at four. Input number is not greater than 20.

# Examples:
# "Zero is four, four is magic."  == solution(0)
# "Three is five, five is four, four is magic."  == solution(3)
# "Four is magic."  == solution(4)
# "Five is four, four is magic."  == solution(5)
# "Ten is three, three is five, five is four, four is magic."  == solution(10)
# "Fifteen is seven, seven is five, five is four, four is magic."  == solution(15)


def solution(num: int) -> str:
    numbers = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
        18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    }

    result = ''
    while num != 4:
        word_num = numbers[num]
        num = len(word_num)
        result += f'{word_num} is {numbers[num]}, '

    result += 'four is magic.'
    return result.capitalize()
