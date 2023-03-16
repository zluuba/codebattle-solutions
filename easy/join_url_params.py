# Return a query string (URL) generated from the given address and a hash map of parameters.
# The parameters in your result string should be arranged in alphabetical order.
#
# Examples:
# "http://www.foobar.com?first_param=test&second_param=some&third_param=clj" == solution(
#       "http://www.foobar.com", {"first_param":"test","second_param":"some","third_param":"clj"}
# )
# "http://www.example.com/search?q=findme&useragent=chrome" == solution(
#       "http://www.example.com/search", {"q":"findme","useragent":"chrome"}
# )
# "http://authority.com?smile=weight&steam=metal&surprise=connection" == solution(
#       "http://authority.com", {"smile":"weight","surprise":"connection","steam":"metal"}
# )

from typing import Dict


def solution(url: str, params: Dict[str, str]) -> str:
    result = url + '?'
    sorted_params = sorted(params.items())

    for param, val in sorted_params:
        result += f"{param}={val}&"

    return result.strip('&')
