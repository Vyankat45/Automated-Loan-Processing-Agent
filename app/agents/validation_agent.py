import re


PAN_REGEX = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"


def validate_pan(text: str):

    match = re.search(PAN_REGEX, text)

    if match:
        return {
            "valid": True,
            "pan_number": match.group()
        }

    return {
        "valid": False,
        "message": "PAN not found"
    }