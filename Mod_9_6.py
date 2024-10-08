def all_variants(text):
    for possible_length in range(1, len(text) + 1):
        for start_position in range(len(text) - possible_length + 1):
            yield text[start_position:start_position + possible_length]


a = all_variants("abc")
for i in a:
    print(i)
