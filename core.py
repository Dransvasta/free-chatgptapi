from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
driver=0
list_answers=[]
def launch():
        global driver
        global list_answers
        driver=Driver(uc=True)
        list_answers=[]
def opengpt(username="animelover132003",password="8870480win"):
        global driver
        global list_answers
        driver.default_get("https://chat.openai.com")
        login_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"__next\"]/div[1]/div[2]/div[1]/div/div/button[1]")))
        login_field.click()
        click2=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".c2694b5b5.cf417db7d.c385f7bb4")))
        click2.click()
        email_field=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#identifierId")))
        email_field.send_keys(username)
        email_field.send_keys(Keys.RETURN)
        
        #pass_field=driver.find_element('//*[@id="password"]/div[1]/div/div[1]/input')
        pass_field=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'Passwd')))
        pass_field.send_keys(password)
        pass_field.send_keys(Keys.RETURN)
        ##__next > div.relative.z-0.flex.h-full.w-full.overflow-hidden > div.relative.flex.h-full.max-w-full.flex-1.flex-col.overflow-hidden > main > div.flex.h-full.flex-col > div.flex-1.overflow-hidden > div > div > div > div:nth-child(9) > div > div > div.relative.flex.w-full.flex-col.lg\:w-\[calc\(100\%-115px\)\].agent-turn > div.flex-col.gap-1.md\:gap-3 > div.flex.flex-grow.flex-col.max-w-full > div > div
        #list_answer=[]
def generate_promt(prompt):
        global driver
        global list_answers
        query_field=driver.find_element("#prompt-textarea")
        query_field.send_keys(prompt)
        query_field.send_keys(Keys.RETURN)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        len1=len(self.list_answers)
        self.list_answers=soup.find_all(class_="markdown prose w-full break-words dark:prose-invert dark")
        while(len(self.list_answers)<len1+1):
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            self.list_answers=soup.find_all(class_="markdown prose w-full break-words dark:prose-invert dark")
        return self.list_answers[-1].text
def closegpt(self):
        global driver
        global list_answers
        driver.close()

launch()
opengpt()
