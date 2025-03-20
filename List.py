import json

class List:
    def __init__(self, file_name):
        self.fileName = f'{file_name}.txt'
        self.list = self.load_list_from_file() 
    
    def load_list_from_file(self):
        try:
            file = open(self.fileName, "r")
            list = json.load(file)
            return list
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_list(self):
        file = open(self.fileName, "w")
        json.dump(self.list, file, indent=4)

    def add_list(self, title):
        if len(self.list) == 0:
            list_id = 1
        else:
            list_id = self.list[-1]["id"] + 1

        list = {
            "id": list_id,
            "title": title
        }
        
        self.list.append(list)
        self.save_list()

    def remove_list(self, list_id):
        for list in self.list:
            if list["id"] == list_id:
                self.list.remove(list)
                self.save_list()
                break
        else:
            print("list does not exist!")
