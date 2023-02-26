# Сonvert Celsius temperature to Kelvin. Consider using 273 for conversion.
#
# Examples:
# 308  == solution(35)
# 261  == solution(-12)
# 273  == solution(0)
# -227  == solution(-500)


def solution(temperature: int) -> int:
    celsius_kelvin_diff = 273
    kelvin_temperature = temperature + celsius_kelvin_diff
    return kelvin_temperature
