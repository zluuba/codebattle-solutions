# If a number is divisible by 3, return "Fizz". If a number is divisible by 5, return "Buzz".
# If a number is divisible by 3 and 5, return "FizzBuzz". Otherwise, return an empty string.
#
# Examples:
# "Fizz"  == solution(3)
# "Buzz"  == solution(50)
# "FizzBuzz"  == solution(150)
# "FizzBuzz"  == solution(5175)


def solution(n: int) -> str:
    fizz, buzz = 'Fizz', 'Buzz'

    if n % 3 == 0 and n % 5 == 0:
        return fizz + buzz
    elif n % 3 == 0:
        return fizz
    elif n % 5 == 0:
        return buzz
    else:
        return ''
