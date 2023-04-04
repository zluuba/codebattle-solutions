# Write a function that accepts a positive integer between 0 and 2000 inclusive and returns a string representation
# of that integer written in English.
#
# Examples:
# "Zero"  == solution(0)
# "Eleven"  == solution(11)
# "Fifty-nine"  == solution(59)
# "One hundred twenty-nine"  == solution(129)
# "One thousand, nine hundred twenty-three"  == solution(1923)


def solution(num: int) -> str:
    numbers = {
        0: 'zero',
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteenth', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
        90: 'ninety', 100: ' hundred ', 1000: ' thousand',
    }

    if num < 20:
        return numbers[num].capitalize()
    if num < 100:
        if num % 10 == 0:
            return numbers[num].capitalize()
        else:
            return (numbers[num - num % 10] + '-' + numbers[num % 10]).capitalize()
    if num < 1000:
        if num % 100 == 0:
            return (numbers[num // 100] + numbers[100]).capitalize().strip()
        else:
            return (numbers[num // 100] + numbers[100] + solution(num % 100)).capitalize()
    if num % 1000 == 0:
        return (numbers[num // 1000] + numbers[1000] + ' ').capitalize().strip()
    return (numbers[num // 1000] + numbers[1000] + ', ' + solution(num % 1000)).capitalize()


# Alternative solution
def solution2(num: int) -> str:
    ones = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
        14: 'fourteen', 15: 'fifteenth', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    }

    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety',
    }

    def num_to_words(number, keyword):
        res = ""
        if number > 19:
            if number % 10 != 0:
                res += f"{tens[number // 10]}-{ones[number % 10]} "
            else:
                res += tens[number // 10]
        else:
            res += ones[number] + " "
        return res + keyword

    result = ""
    if 0 <= num <= 19:
        return ones[num].capitalize()
    elif 100 <= num <= 999:
        result += num_to_words(((num // 100) % 10), "hundred ")
    elif 1000 <= num <= 2000:
        result += num_to_words(((num // 1000) % 100), "thousand, ")
        result += num_to_words(((num // 100) % 10), "hundred ")

    if num % 100 != 0:
        result += num_to_words((num % 100), "")

    return result.strip().capitalize()
