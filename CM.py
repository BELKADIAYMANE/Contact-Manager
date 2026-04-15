from fastapi import FastAPI
import json

app=FastAPI()
class ContactManager:
    
    def __init__(self):
        self.contacts = {}
        self.load()


    def save(self):
        with open("contacts.json","w") as file:
            json.dump(self.contacts,file)

    def load(self):
        try:
             with open("contacts.json","r") as file:
                self.contacts=json.load(file)
        except:
            self.contacts={}


manager = ContactManager()
@app.get("/contacts")
def get_contacts():
    return manager.contacts


@app.post("/contacts")

def add_contact(name:str,phone:str):
    name=name.lower()
    if name in manager.contacts:
         return {"error": "Contact exists"}
    else:
        manager.contacts[name]=phone
    manager.save()
    return{"message":"contact added"}

@app.get("/contacts/{name}")

def search_contact(name:str):
    name=name.lower()
    if name in manager.contacts:
        return{name:manager.contacts[name]}
    else:
        return{"error":"not found"}

@app.delete("/contacts/{name}")

def delete_contact(name:str):
    name=name.lower()
    if name in manager.contacts:
        del manager.contacts[name]
        return{"message":"deleted"}
    
    else:
        return{"error":"not found"}

@app.put("/contacts/^{name}")

def update_contact(name:str,phone:str):
    name=name.lower()
    if name in manager.contacts:
        manager.contacts[name]=phone
        return{"message":"updated"}
    else:
        return{"error":"not found"}
    





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  

    
    



