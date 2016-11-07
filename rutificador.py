#!/usr/bin/python3

import urllib, urllib2
import json

def rutificador(nombre):
   url    = 'http://chile.rutificador.com/get_generic_ajax/'
   values = {'entrada':nombre,'csrfmiddlewaretoken':'ioAfP80sm4cafdC8qgT9OoeCFb53KXGh' }
   
   data   = urllib.urlencode(values)
   req    = urllib2.Request(url,data)

   req.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
   req.add_header("Content-Length", str(len(data)))
   req.add_header("Cookie", "csrftoken=ioAfP80sm4cafdC8qgT9OoeCFb53KXGh; _ga=GA1.2.947659569.1478526923")

   response = urllib2.urlopen(req)

   #x='{"status": "success", "value": [{"dv": "0", "name": "ITURRA VALDES SEBASTIAN ANDRES", "rut": 18765525, "wname": "iturra-valdes-sebastian-andres"}]}'
   x = response.read()    
   y = json.loads(x) #convierte la respuesta a objetos json
   
   print "result status: " + y['status'] #imprime la respuesta de la web (success, error)
  
   if y['status'] == "success":
      print x
   else:
      print("status error.")
    

def main():   
   rutificador('sebastian andres iturra valdes')
   #rutificador('18765525-0')
   
   print 'Fin.'

if __name__ == '__main__':
	main()
