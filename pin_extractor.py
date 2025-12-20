def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        secret_code += str(len(words[line_index]))
        


poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)
