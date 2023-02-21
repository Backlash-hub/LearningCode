str = "X-DSPAM-Confidence:    0.8475"

space = str.find(':')

data = str[space+2:]

value = float(data)

print(value)