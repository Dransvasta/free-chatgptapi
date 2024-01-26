import requests
import json
server=" https://0ddc-122-164-85-202.ngrok-free.app"
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
