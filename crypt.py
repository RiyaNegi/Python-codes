import sys

# Use Caesar's cipher, offset by +3

def secret(message):
    new_msg=""
    for i in message:
        fill = ord(i)+3
        new_msg += (chr(fill))
    return new_msg

def decode(msg):
    decode = ""
    for i in msg:
        code = ord(i)-3
        decode += (chr(code))
    return decode

message = "Naruto is going to use Shadow clone jutsu against Orochimaru and kabuto"
print("the encoded msg is :" + (secret(message)))
print("the decoded msg is :" + decode(secret(message)))
