import re

# Name regex:
# - Allows capitalized words
# - Allows hyphens and apostrophes inside names (e.g., D'Angelo, Taylor-Joy)
# - Requires at least one capitalized word
name_regex = re.compile(r"^[A-Z][a-z]*(?:[ '\-][A-Z][a-z]*)*$")


# Phone number regex:
# - Supports: 5555555555, 555-555-5555, (555) 555-5555
phone_regex = re.compile(r"^(?:\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$")

# Email regex:
# - Starts with letters (optionally dot-separated), followed by @, domain, and TLD
# - No starting numbers or invalid symbols like `$`
email_regex = re.compile(r"^[a-zA-Z]+(?:\.[a-zA-Z0-9]+)*@[a-zA-Z]+\.[a-zA-Z]{2,}$")
