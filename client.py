import requests

response = requests.post('http://127.0.0.1:5000/advertisements/',
                        json={'title': 'python', 'description': 'back language', 'owner': 'nikolay'}                      
                        )

response = requests.patch('http://127.0.0.1:5000/advertisements/1',
                        json={'title': 'java', 'description': 'front language', 'owner': 'olesya'}  
                        )

response = requests.get('http://127.0.0.1:5000/advertisements/1')                                      

response = requests.delete('http://127.0.0.1:5000/advertisements/1')                                      
                        


print(response.status_code)
print(response.json())
