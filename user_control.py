import requests, json

if __name__ == '__main__':
    print("Read the Readme file on instructionas to run flask server")
    user_in = input("Choose option:\n\t1. Conenct to server\n\t2. Make a prediction\n\tUser Input:")
    while user_in:
        if user_in == '2':
            news = input("Copy paste the  article here")
            print('making a call to API')
            data = {'news': news}
            response = requests.post(url="http://127.0.0.1:5001/", data = data)
            print('response', response.json() if str(response) != '<Response [500]>' else response)
        elif user_in == '1':
            print("Connecting to  server...")
            response = requests.get("http://127.0.0.1:5001/")
            print('response', response.json() if str(response) == '<Response [200]>' else response)
        elif user_in == 'quit':
            break
        else:
            print('invalid input')
        print("\n\n\n")
        user_in = input("Choose option:\n\t1. Conenct to server\n\t2. Make a prediction\n\tUser Input:")
