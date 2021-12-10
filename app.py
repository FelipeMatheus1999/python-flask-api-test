from flask import Flask, request, jsonify
import json

app = Flask(__name__)

persons = [
    {
    "id": 1,
    "name": "Felipe Matheus",
    "age": 21,
    "programming_languages": ["Java Script", "Python"]
    },
    {
    "id": 2,
    "name": "Marcos Augusto",
    "age": 27,
    "programming_languages": ["Java Script", "Python", "PHP", "Java"]
    },
    {
    "id": 3,
    "name": "Lucas Arruda",
    "age": 17,
    "programming_languages": ["Java Script"]
    }
    ]

#devolve um desenvolvedor pelo ID, também é possível alterar e deletar.
@app.route("/dev/<int:id>", methods=["GET", "PUT", "DELETE"])
def person(id):
    try:
        for person in persons:
            if person.get("id") == id:
                person_find = person

        person_find

        if request.method == "GET":
            return person_find
        
        elif request.method == "PUT":
            data = json.loads(request.data)

            for index, person in enumerate(persons):
                if person.get("id") == id:
                    persons[index] = data
            
            return data

        elif request.method == "DELETE":
            message = f"Deleper Id {id} deleted"
            response = {"state": "ok", "message": message}

            for index, person in enumerate(persons):
                if person.get("id") == id:
                    persons.pop(index)
            
            return response

    except IndexError:
        message = f"Id developer {id} does not exist"
        response = {"state": "error", "message": message}
        return response

    except Exception:
        message = f"Unknown error look for API admin"
        response = {"state": "error", "message": message}
        return response

#Lista todos os desenvolvedores e permite register um desenvolvedor.
@app.route("/dev/", methods=["GET", "POST"])  
def persons__list__and__join():
    if request.method == "POST":
        data = json.loads(request.data)

        for index, person in enumerate(persons):
            last_id = person.get("id")

            if person.get("id") - last_id != 1:
                data["id"] = index + 1
            
            else:
                data["id"] = len(persons) + 1
        
        persons.append(data)
        return data
    
    elif request.method == "GET":
        return jsonify(persons)

if __name__ == "__main__":
    app.run(debug=True)
