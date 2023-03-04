"""
Write a function that takes in a string and returns it's run length encoding.
"""


def run_length_encoding(string: str) -> str:
    if not string:
        return None
    result = []
    count = 1
    last_char = string[0]
    for char in string[1:]:
        if char == last_char and count < 9:
            count += 1
        else:
            result.append(str(count) + last_char)
            last_char = char
            count = 1
    result.append(str(count) + last_char)
    return "".join(result)


if __name__ == "__main__":
    print(run_length_encoding(""))
    print(run_length_encoding("AAAAAAAAAAAABBBBBBBBBBCCCCCCCCDDDDDDDDDDD"))  # 9A3A9B1B8C9D2D

