def lpad(input_value, length):
    input_string = str(input_value)
    padding = '0' * length
    result = padding + input_string
    return result[-(len(result) - len(input_string)):]
