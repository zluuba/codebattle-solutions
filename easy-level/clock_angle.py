# Calculate the angle between the hour and the minute hand of a clock at a given time.
#
# Examples:
# 7.5  == solution(3, 15)
# 0.0  == solution(0, 0)
# 82.5  == solution(0, 15)
# 275.0  == solution(0, 50)
# 157.5  == solution(3, 45)


def solution(hour: int, minute: int) -> float:
    h_angle = (hour * 60 + minute) * 0.5
    m_angle = minute * 6
    return abs(h_angle - m_angle)
