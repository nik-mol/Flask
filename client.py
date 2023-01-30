import requests

response = requests.post('http://127.0.0.1:5000/users/',
                        json={'email': 'nikolay@yandex.ru', 'password': '310585'}                      
                        )

response = requests.patch('http://127.0.0.1:5000/users/1',
                        json={'email': 'new_nikolay@yandex.ru', 'password': '31058511'}                      
                        )

response = requests.get('http://127.0.0.1:5000/users/1')                                      

response = requests.delete('http://127.0.0.1:5000/users/1')                                      
                        


print(response.status_code)
print(response.json())
