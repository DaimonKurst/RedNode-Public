"""
RedNode Public Demo Module

Safe endpoint extractor for synthetic HAR-like structures.
This file is intentionally sanitized for public demonstration.
"""

from urllib.parse import urlparse


def extract_endpoints(entries):
    endpoints = []

    for entry in entries:
        request = entry.get("request", {})
        url = request.get("url")

        if not url:
            continue

        parsed = urlparse(url)

        endpoints.append({
            "method": request.get("method", "GET"),
            "scheme": parsed.scheme,
            "host": parsed.netloc,
            "path": parsed.path,
            "query_present": bool(parsed.query),
        })

    return endpoints


if __name__ == "__main__":
    demo_entries = [
        {"request": {"method": "GET", "url": "https://example.com/api/users"}},
        {"request": {"method": "POST", "url": "https://example.com/api/orders?id=123"}},
    ]

    for endpoint in extract_endpoints(demo_entries):
        print(endpoint)
