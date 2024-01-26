from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from flask import Flask,render_template,url_for,request,jsonify,redirect
import secrets

def generate_unique_id(length=12):
    # Using hex encoding to create a random string
    unique_id = secrets.token_hex(length // 2)
    return unique_id
app = Flask(__name__)
drivers={}
list_answers={}
def launchgpt():
        global drivers
        global c
        global list_answers
        c=generate_unique_id()
        driver=Driver(uc=True)
        drivers[c]=driver
        list_answers[c]=[]
        print(c)
        return c
def opengpt(driverid,username="animelover132003",password="8870480win"):
        global drivers
        global list_answers
        drivers[driverid].default_get("https://chat.openai.com")
        login_field = WebDriverWait(drivers[driverid], 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div[1]/div/div/button[1]")))
        login_field.click()
        click2=WebDriverWait(drivers[driverid], 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-provider='google']")))
        click2.click()
        email_field=WebDriverWait(drivers[driverid], 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#identifierId")))
        email_field.send_keys(username)
        email_field.send_keys(Keys.RETURN)
        
        #pass_field=driver.find_element('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_field=WebDriverWait(drivers[driverid], 10).until(EC.visibility_of_element_located((By.NAME, 'Passwd')))
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)
        ##__next > div.relative.z-0.flex.h-full.w-full.overflow-hidden > div.relative.flex.h-full.max-w-full.flex-1.flex-col.overflow-hidden > main > div.flex.h-full.flex-col > div.flex-1.overflow-hidden > div > div > div > div:nth-child(9) > div > div > div.relative.flex.w-full.flex-col.lg\:w-\[calc\(100\%-115px\)\].agent-turn > div.flex-col.gap-1.md\:gap-3 > div.flex.flex-grow.flex-col.max-w-full > div > div
        #list_answer=[]
def generate_promt(driverid,prompt):
        global drivers
        global list_answers
        query_field=drivers[driverid].find_element("#prompt-textarea")
        query_field.send_keys(prompt)
        query_field.send_keys(Keys.RETURN)
        html_content = drivers[driverid].page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        len1=len(list_answers[driverid])
        list_answers[driverid]=soup.find_all(class_="markdown prose w-full break-words dark:prose-invert dark")
        while(len(list_answers[driverid])<len1+1):
            html_content = drivers[driverid].page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            list_answers[driverid]=soup.find_all(class_="markdown prose w-full break-words dark:prose-invert dark")
        return list_answers[driverid][-1].text
def closegpt(driverid):
        global drivers
        global list_answers
        drivers[driverid].close()
@app.route('/')

def index():
       return 'really'

@app.route('/launch')

def launch():
        re={}
        print("hello--------------------------------------------------------------------")
        username = request.args.get('username') 
        password = request.args.get('pass')
        try:
               tc=launchgpt()
               opengpt(tc,username,password)
               re['status']="Success"
               re['driverid']=tc
        except:
               re['status']='failure'
        print(tc in drivers)
        return jsonify(re)

@app.route('/promt/<string:driverid>')
def promt(driverid):
       promt_answer = {}
       promt_answer['prompt'] = request.args.get('prompt')
       global drivers
       if drivers[driverid]:
              pass
       else:
              promt_answer['result'] = "pls launch the gpt before entering the promt"
       promt_answer['result'] = generate_promt(driverid,promt_answer['prompt'])
       return jsonify(promt_answer)
@app.route('/stop/<string:driverid>')
def stop(driverid):
       closegpt(driverid)
       return "closed succeessfully"
if __name__=='__main__':
       app.run(debug=True,threaded=False)