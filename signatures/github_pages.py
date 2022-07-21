from domain import Domain
from . import generic
import detection_enums

github_pages_ipv4 = [
    "185.199.108.153",
    "185.199.109.153",
    "185.199.110.153",
    "185.199.111.153",
]
github_pages_ipv6 = [
    "2606:50c0:8000::153",
    "2606:50c0:8001::153",
    "2606:50c0:8002::153",
    "2606:50c0:8003::153",
]


def potential(domain: Domain, **kwargs) -> bool:
    return generic.COMBINED.matching_ipv4_or_ipv6(
        domain, github_pages_ipv4, github_pages_ipv6
    )


domain_not_configured_message = "There isn't a GitHub Pages site here"


def check(domain: Domain, **kwargs) -> bool:
    return generic.WEB.string_in_body_http(domain, domain_not_configured_message)


INFO = """
The defined domain has A/AAAA records configured for Github pages but Github pages returns a 404. \
An attacker can register this domain on Github pages.
    """

CONFIDENCE = detection_enums.CONFIDENCE.CONFIRMED
