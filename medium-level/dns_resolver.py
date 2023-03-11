# Create a function, thats pick up an IP from domains by domain name.
# If there is no record, then return "DNS_PROBE_FINISHED_NXDOMAIN".
#
# Examples:
# "103.95.84.1"  == solution({"rubyonrails.org":"211.116.107.5","clojure.org":"103.95.84.1",
#                             "phoenixframework.org":"234.214.199.63","reactjs.org":"20.199.101.214"}, "clojure.org")
# "234.214.199.63"  == solution({"rhythm.ru":"201.116.147.4","building.ru":"103.176.11.27","hexlet.io":"234.214.199.63",
#                                "brass.ru":"201.116.147.4"}, "hexlet.io")
# "DNS_PROBE_FINISHED_NXDOMAIN"  == solution({"some.com":"127.0.0.1"}, "test.net")

from typing import Dict


def solution(domains: Dict[str, str], domain: str) -> str:
    return domains.get(domain, 'DNS_PROBE_FINISHED_NXDOMAIN')
