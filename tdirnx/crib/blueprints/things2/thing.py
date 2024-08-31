import nanoid
import uuid
import os
import json
from json import JSONEncoder
import requests
from bs4 import BeautifulSoup as bs

class Thing():
    def __init__(self,description=None,name=None,status="New",typeName="Thing",*args,**kwargs):
        self.uuid = uuid.uuid4().hex
        self.nid = nanoid.generate()
        self.status = "New"
        
        if name == None:
            self.name = "NoName"
        else:
            self.name = str(name)
        self.description = description
        self.typeName = typeName
        self.status = [status]
        self.file = None
        self.filename = "/workspaces/codespaces-flask/newprojects/Things/" + self.name + "_" + self.typeName + "_" + self.nid
        self.path = str(self.filename)
        self.things = []
        
    
    def __repr__(self):
        return "Thing(" + self.typeName + ":" + self.name + ":" + self.uuid + ")"

    def __str__(self):
        return "Thing(" + self.typeName + ":" + self.name + ")"

    def ensurePath(self):
        if not os.path.exists(self.path):
            os.makedirs(path)
    
    def write(self):
        print("writing " + str(self.name) + ":" + str(self.uuid))
        self.open_file()
        self.file.write(json.dumps(self,cls=ThingEncoder))
        self.close_file()
        return self

    def get_stats(self):
        return str(self.description) + " " + (" ".join(self.status))

    def get_filename(self):
        return self.filename

    def open_file(self):
        # if path != None:
        #     if not os.path.exists(path):
        #         os.makedirs(path)
        #     if os.path.exists(path + self.get_filename(with_path=False)):
        #          return open(path + self.get_filename(with_path=False), 'r+')
        #     else 
        #          return open(path + self.get_filename(with_path=False), 'w')
        # else
        #     if not os.path.exists(self.path):
        #         raise Exception("No path supplied and Thing:" + self.getNid() + " has bad internal path " + self.path)
        #     else 
        #         if os.path.exists(self.get_filename(with_path=True)):
        #             return open(self.get_filename(with_path=True),'r+')
        #         else return open(self.get_filename(with_path=True), 'w')
        if self.file == None:
            self.file = open(self.filename, 'w')
            return "Opened first time"
        elif self.file.closed:
            self.file = open(self.filename, 'w')
            return "Old file was closed. Opened new file overwriting old one"
        else:
            return "Old file was still opened. Doing nothing"
        
    def close_file(self):
        if self.file == None:
            return "No file yet."
        else:
            self.file.close()
        
    def get_file_closed_status(self):
        return self.file.closed

    def use(self,newStatus="Used"):
        print("Used " + self.name + ".")
        self.status.append(newStatus)
        return self

    def use(self, adverb, exclaim=False):
        print("Used " + adverb + ("." if not exclaim else "!"))
        self.status.append("Used " + adverb + ("." if not exclaim else "!"))
        return self

    def refresh(self):
        print(self.typeName + " " + self.realname + " is refreshed.")
        self.status = ['Renewed']
        
    def realname(self):
        return (self.typeName + ":" + self.name + ":" + self.nid)

    def getStatus(self):
        return self.status

    def getUuid(self):
        return self.uuid
    
    def getNid(self):
        return self.nid
    
    def getType(self):
        return self.typeName
    
    def say_name(self):
        print(self.typeName + " says, \"" + self.name + "\"")
    
    def retrieve(self):
        try:
            return json.load(open(self.filename, 'r'))
        
        except FileNotFoundError:
            print('no file on disk')

# subclass JSONEncoder
class ThingEncoder(JSONEncoder):
        def decode(self, s):
            di = json.loads(s)
            return Thing(**di)
        def default(self, o):
            return o.__dict__