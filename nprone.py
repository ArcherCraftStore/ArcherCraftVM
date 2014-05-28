import cmd,sys
from urllib import request
from json import loads

class NPRClient(cmd.Cmd):
  def __init__(self):
   cmd.Cmd.__init__(self)
   self.prompt="NPRC 1.0.0.1"
   self.doc_header="Available Support Topic"
   self.undoc_header="Unavailable Topics"
   self.intro="ACOSF ArcherCraft VM NPRC v1.0.0.0 copyright 2014"
   self.file = None
  def do_nprlist(self, line):
   url =  "http://api.npr.org/query"
   url = url + "?apiKey="
   key = "MDE0MzQ3NDAyMDE0MDEyMDQ0NzAzYTBlYw001"
   url = url + key
   url += '&numResults=3&format=json'
   url += '&id='
   npr_id = input("Which NPR ID do you want to query?")
   url += str(npr_id)
   print(url)
   response = request.urlopen(url)
   json_obj = loads(response)
   for story in json_obj['list']['story']:
       print(story['title']['text'])
   
   
   
  
if __name__  == "__main__":
  nprc = NPRClient()
  nprc.cmdloop()
