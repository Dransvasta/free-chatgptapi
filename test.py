import requests
import json
server="http://127.0.0.1:5000"
def startgpt(username,password):
    global server
    html = requests.get(server+'/launch?username='+username+'&pass='+password,headers={"ngrok-skip-browser-warning":"40"})
    d=json.loads(html.text)
    if d['status']=="Success":
        return d['driverid']
    else:
        print("opening gpt failed miserably")
def generate(driverid,prompt):
    global server
    html = requests.get(server+'/promt/'+str(driverid)+'?prompt='+prompt,headers={"ngrok-skip-browser-warning":"40"})
    d=json.loads(html.text)
    return d['result']
def stop(driverid):
    global server
    requests.get(server+'/stop/'+str(driverid),headers={"ngrok-skip-browser-warning":"40"})
    return "closed"


tc=startgpt('animelover132003','8870480win')
print(tc)
ch="NO"
while ch!='YES':
    promt=input("enter your promt:")
    print(generate(tc,promt))
    ch = input("do u want to stop say 'YES'")