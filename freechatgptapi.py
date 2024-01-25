import requests
import json
server="https://4710-122-164-85-202.ngrok-free.app"
def startgpt(username,password):
    global server
    html = requests.get(server+'/launch?username='+username+'&pass='+password,headers={"ngrok-skip-browser-warning":"40"})
    d=json.loads(html.text)
    return d['status']
def generate(prompt):
    global server
    html = requests.get(server+'/promt?prompt='+prompt,headers={"ngrok-skip-browser-warning":"40"})
    d=json.loads(html.text)
    return d['result']
def stop():
    global server
    requests.get(server+'/stop',headers={"ngrok-skip-browser-warning":"40"})
    return "closed"
