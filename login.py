import json
import re

class Register:
    details = {}
    @staticmethod 
    def login( name, password):
        with open("passworda.json", "r") as f:
            file = json.load(f)
        if name in file.keys():
            if file[name] == password:
                print("Logged in ")
                return True
        else:
            return False

    def __init__(self, name, password):
        # Check if the password is valid using the re.search function
        if re.search(r'^(\w+)@[0-9]+\.[a-zA-Z]{2,3}$', password):
            Register.details[name] = password
            with open("passworda.json", "w") as f:
                json.dump(Register.details, f)
        else:
            print("Invalid password .")


# register_instance= Register("moni", "password@123.com")
# Register.login("moni", "password@123.com")
