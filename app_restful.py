from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills, SkillsAddAndRemove
import json

persons = [
    {
    "name": "Felipe Matheus",
    "age": 21,
    "programming_languages": ["Java Script", "Python"],
    "id": 1
    },
    {
    "name": "Marcos Augusto",
    "age": 27,
    "programming_languages": ["Java Script", "Python", "PHP", "Java"],
    "id": 2
    },
    {
    "name": "Lucas Arruda",
    "age": 17,
    "programming_languages": ["Java Script"],
    "id": 3
    }
]

app = Flask(__name__)
api = Api(app)

class Person(Resource):
    def get(self, id):
        try:
            for person in persons:
                if person.get("id") == id:
                    person_find = person
            return person_find

        except IndexError:
            message = f"Id developer {id} does not exist"
            response = {"state": "error", "message": message}
            return response

        except Exception:
            message = f"Unknown error look for API admin"
            response = {"state": "error", "message": message}
            return response

    def put(self, id):
        data = json.loads(request.data)
        for index, person in enumerate(persons):
            if person.get("id") == id:
                persons[index] = data
                return data
    
    def delete(self, id):
        message = f"Developer {id} deleted"
        response = {"status": "ok", "message": message}
        for index, person in enumerate(persons):
            if person.get("id") == id:
                persons.pop(index)
                return response
class ListAllPersonsAndAddNewPerson(Resource):
    def get(self):
        persons.sort(key=lambda person: person.get("id"))
        return persons
    
    def post(self):
        data = json.loads(request.data)
        for index, person in enumerate(persons):
            
            if index == 0:
                last_id = 0
            
            if person.get("id") - last_id != 1 and index != 0:
                data["id"] = index + 1
                persons.append(data)
                return data
            
            else:
                data["id"] = len(persons) + 1
            last_id = person.get("id")

        persons.append(data)
        return data

api.add_resource(Person, "/dev/<int:id>")
api.add_resource(ListAllPersonsAndAddNewPerson, "/dev")
api.add_resource(Skills, "/skills")
api.add_resource(SkillsAddAndRemove, "/skills/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
