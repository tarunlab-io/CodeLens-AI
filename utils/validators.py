def validate_code_input(code: str) -> tuple[bool, str]:
    """
    Validates the user code input.
    Returns a tuple: (is_valid, error_message)
    """
    if not code or not code.strip():
        return False, "Please enter some code to analyze."
    
    if len(code) > 50000:
        return False, "The code is too large. Please limit your input to around 50,000 characters."
    
    return True, ""
