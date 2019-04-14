import requests, time, random

sent = 0

try:
    while True:
        s = int(time.time())

        message = chr(random.randint(60,127))
        result = requests.get('http://127.0.0.1:8080/?data='+message).text

        if result != message:
            print(result)
            print(message)
            print('ERROR!')
            break

        sent += 1
except Exception as e:
    print(e)
    print('sent ', sent)
