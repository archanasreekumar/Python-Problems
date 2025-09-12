def count_char(input_string: str) -> str:
    input_items = sorted(set(input_string))
    return "".join(f"{i}{input_string.count(i)}" for i in input_items)

print(count_char("AAABBC"))