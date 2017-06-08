#!/usr/bin/python

import urllib, urllib2
import cookielib
import json

url     = 'https://chile.rutificador.com'
url_api = url + '/get_generic_ajax/'

def getToken():
    cookie_jar = cookielib.CookieJar()
    opener     = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))

    urllib2.install_opener(opener)

    req = urllib2.Request(url)
    urllib2.urlopen(req)

    data = dict((cookie.name, cookie.value) for cookie in cookie_jar)

    token = data['csrftoken']

    return token

def rutificador(nombre):

    token = getToken()

    #Seteamos los valores que se enviaran por POST
    values  = {'entrada': nombre, 'csrfmiddlewaretoken': token}

    data = urllib.urlencode(values)
    req  = urllib2.Request(url_api, data)

    #req.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
    #req.add_header("Content-Length", str(len(data)))
    req.add_header("Cookie", "csrftoken=" + token)
    req.add_header('referer', url)

    response = urllib2.urlopen(req)

    # x='{"status": "success", "value": [{"dv": "0", "name": "ITURRA VALDES SEBASTIAN ANDRES", "rut": 18765525, "wname": "iturra-valdes-sebastian-andres"}]}'
    x = response.read()
    
    # Convierte la respuesta a objetos json
    y = json.loads(x)  

    #print "result status: " + y['status']  # imprime la respuesta de la web (success, error)

    if y['status'] == "success":
        print x
    else:
        print y


def main():
    rutificador('sebastian andres iturra valdes')

if __name__ == '__main__':
    main()
