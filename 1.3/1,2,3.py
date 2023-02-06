#-1:

#Para el punto 1, podemos crear una función que realice una petición POST para crear un usuario, 
#y luego otra función que realice una petición GET para recuperar sus datos:

import requests
 #1.2

# Crea un usuario
url = "https://petstore.swagger.io/v2/user/R"
payload = {"username": "example_user", "firstName": "John", "lastName": "Doe", "email": "example@gmail.com", "password": "password123"}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=payload, headers=headers)

# Recupera los datos del usuario
url = "https://petstore.swagger.io/v2/user/example_user"

response = requests.get(url)
data = response.json()
print(data)

# Obtiene la lista de mascotas vendidas
url = "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"

response = requests.get(url)
data = response.json()

# Lista los nombres de las mascotas vendidas
pet_list = []
for pet in data:
    pet_list.append({"id": pet["id"], "name": pet["name"]})

print(pet_list)



#3
class PetList:
    def __init__(self, pet_list):
        self.pet_list = pet_list

    def count_pets_by_name(self):
        pet_count = {}
        for pet in self.pet_list:
            if pet["name"] in pet_count:
                pet_count[pet["name"]] += 1
            else:
                pet_count[pet["name"]] = 1
        return pet_count

pet_list = PetList(pet_list)
print(pet_list.count_pets_by_name())