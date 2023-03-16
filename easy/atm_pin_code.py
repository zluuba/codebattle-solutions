# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits
# or exactly 6 digits. Create a function that takes a string and check if the PIN is valid.
#
# Examples:
# true  == solution("1234")
# true  == solution("123456")
# false  == solution("12345")
# false  == solution("some pin code")
# false  == solution("m8te")


def solution(pin: str) -> bool:
    if pin.isdigit() and (len(pin) == 4 or len(pin) == 6):
        return True
    return False
