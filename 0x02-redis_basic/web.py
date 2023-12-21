#!/usr/bin/env python3
"""
web.py - Module for handling web page retrieval and caching.
This module provides functionality to retrieve HTML content from a URL using
the requests module, cache the content in Redis with an expiration time of
10 seconds, and track the number of times a particular URL was accessed.
"""

import requests
import redis


def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a URL and cache the result with an expiration
    time of 10 seconds.

    Args:
    - url: The URL to retrieve the HTML content from.

    Returns:
    - The HTML content of the URL.
    """
    # Initialize Redis client
    r = redis.Redis()

    # Increment count for the URL
    r.incr(f"count:{url}")

    # Check if content is cached
    cached_content = r.get(f"content:{url}")
    if cached_content:
        return cached_content.decode('utf-8')

    # Get the HTML content using requests
    response = requests.get(url)
    html_content = response.text

    # Cache the content with a 10-second expiration
    r.setex(f"content:{url}", 10, html_content)

    return html_content


if __name__ == "__main__":
    # Example usage:
    url = "http://slowwly.robertomurray.co.uk/delay/10000/url/"
    url += "http://www.example.com"
    html = get_page(url)
    print(html)  # This will print the HTML content fetched from the URL
