def chunks(string, size = 1):
    """Splits `string` in chunks of size `size`

    Returns a generator.
    Raises `ValueError` if `size == 0`.
    """
    # Create a generator
    for i in range(0, len(string), size):
        yield string[i : i+size]
