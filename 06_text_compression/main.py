def compress_text(text):
    if text == "":
        return ""
    result = ""
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            result += current + str(count)
            current = ch
            count = 1
    result += current + str(count)
    return result

print("RUN-LENGTH TEXT COMPRESSION")
message = input("Enter text to compress: ")
if not message:
    print("Input text is empty.")
else:
    encoded = compress_text(message)
    print("Original text:", message)
    print("Compressed text:", encoded)
    print("Original length:", len(message))
    print("Compressed length:", len(encoded))
    if len(encoded) < len(message):
        print("Compression is beneficial.")
    else:
        print("Compression is not beneficial; keep the original text.")
