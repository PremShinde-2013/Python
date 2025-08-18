import json

# Python object → JSON file
person = {"name": "Prem", "age": 25, "skills": ["python", "ml"]}
with open("person.json", "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=2)

# JSON file → Python object
with open("person.json", "r", encoding="utf-8") as f:
    obj = json.load(f)
print(obj["skills"])

# Strings also work:
s = json.dumps(person, ensure_ascii=False)   # to string
obj2 = json.loads(s)                          # from string
