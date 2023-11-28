import json

# 1 string para dicionário
person = '{"nome": "Rodrigo", "Linguagens": ["Python", "Javascript"]}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['Linguagens'])

# 2 Convertendo dict para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))

# 3 - Formatando json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando json em txt
with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)

# 5 - Lendo json externo
with open('person.txt', 'r') as f:
    data = json.load(f)
print(data)
