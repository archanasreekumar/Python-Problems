def count_char(input_string: str) -> str:
    seen = {}
    for ch in input_string:
        seen[ch] = seen.get(ch, 0)+1
    return "".join(f"{i}{seen[i]}" for i in seen)

print(count_char("AAABBC"))