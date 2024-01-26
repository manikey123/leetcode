# Check if a given IP address is valid.
# A valid IP address must be in the form of xxx.xxx.xxx.xxx,
# where xxx is a number from 0-255

# For example:
#           - 256.1.2.3 is not a valid IP address because the
#             first octet number is greater than 255
#           - 245.1.2 is not a valid IP address because
#             it has only 3 octets

# Note: We recommend you do NOT use regex to solve this question
# as it can be difficult and time consuming to debug. You may however, do
# so if you wish.

# def is_valid_IP(check_ip):
#     # Your code here

def is_valid_IP(address):
    parts = address.split(".")

    if len(parts) != 4:
        print("IP address invalid!")
        return False


    for part in parts:
        if not part.isdigit():
            print('IP address invalid!')
            return False

        if int(part) < 0 or int(part) > 255:
            print('IP address invalid!')
            return False
    print('IP address valid!')
    return True

assert is_valid_IP('') == False
assert is_valid_IP('127.0.0.1') == True
assert is_valid_IP('127.0.0.100') == True
assert is_valid_IP('192.34.0.0.1') == False
assert is_valid_IP('192.3.0.1') == True
assert is_valid_IP('192.289.25.10') == False
assert is_valid_IP('192.289.25') == False
assert is_valid_IP('a12.A.29.5') == False
print('passed')
