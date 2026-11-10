"""A side-effect-free function, adapted from the original cap example."""


def capitalize_text(text):
    """Capitalize the first character and lowercase the remaining characters.

    This is str.capitalize(), not title case. Reject non-text input explicitly.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return text.capitalize()
