from flask import request
from flask_restful import Resource
import json

skills = [{"name": "Python", "id": 1}]

class Skills(Resource):
    def get(self):
        skills.sort(key=lambda skill: skill.get("id"))
        return skills

    def post(self): #Está adicionando skill duplicada
        data = json.loads(request.data)
        skills = Skills.get("get")

        for skill in skills:
            if skill.get("name").lower() == data.get("name").lower():
                response = {"message": f"{data.get('name')} already exists in skills"}
                return response
            
            else:
                last_id = 0

                for index, skill in enumerate(skills):
                    if skill.get("id") - last_id != 1 and index != 0:
                        data["id"] = index + 1
                        break
                    
                    else:
                       data["id"] = len(skills) + 1
                    
                    last_id = skill.get("id")

                skills.append(data)
                return data

class SkillsAddAndRemove(Resource):
    def get(self, id): #Não está pegando skill durante o teste da API
        for skill in skills:
            if skill.get("id") == id:
                return skill
            
            else:
                message = f"This id {id} doesn't have a correspoding skill"
                response = {"status": "error", "message": message}
                return response
    
    def put(self, id): #Não está renomeando skill colocadas durante o teste da API
        data = json.loads(request.data)

        for skill in skills:

            if skill.get("id") == id:
                skill["name"] = data
                return skill

            else:
                response = {"status": "error", "message": f"Skill id {id} does not exists"}
                return response

    def delete(self ,id):
        response = {"status": "ok", "message": f"Skill {id} deleted"}
        
        for index, skill in enumerate(skills):
            if skill.get("id") == id:
                skills.pop(index)
                return response
