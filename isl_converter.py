def convert_to_isl(text: str) -> str:
    words = text.lower().split()

    # Remove unnecessary words
    remove_words = {"is", "am", "are", "the", "a", "an", "to"}

    filtered = [word for word in words if word not in remove_words]

    return " ".join(filtered)

