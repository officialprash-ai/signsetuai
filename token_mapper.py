def map_to_tokens(text: str):
    words = text.split()
    tokens = [f"sign_{word}" for word in words]
    return tokens
