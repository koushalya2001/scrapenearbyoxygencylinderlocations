from flask import Flask,jsonify,request
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time
def getReviewstwo(zone):

    return shops
app = Flask(__name__)
@app.route("/damagedetails/<string:zone>")
def get(zone):
    assert zone==request.view_args['zone']
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    search = "hospitals with oxygen cylinder in{}".format(zone)
    url =f"https://www.google.com/search?q={search}"
    names,addresses,phones,openstatuses=["Raj Gas Agency",Triveni Oxygen Company"],["DM Rd, near sneak garden","160, Jeevan Jyoti"],["094114 77488","099356 63423"],["open","open"]
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    menu_bt = wait.until(EC.element_to_be_clickable( (By.XPATH, '//div[@class="hdtb-mitem"]//a')) )
    menu_bt.click()
    response = BeautifulSoup(driver.page_source, 'html.parser')
    name=driver.find_elements_by_xpath('//div[@class="CUwbzc-content gm2-body-2"]//div[@class="qBF1Pd-haAclf"]//span')
    address=driver.find_elements_by_xpath('//div[@class="CUwbzc-content gm2-body-2"]//div[@class="ZY2y6b-RWgCYc"]//div[@class="ZY2y6b-RWgCYc"]//span[@jsinstance="*1"]//jsl//span[2]')
    phone=driver.find_elements_by_xpath('//div[@jsinstance="*1"]//span[@jsinstance="*0"]//jsl//span[2]')
    for e in address:
        if(not(bool(re.search("[Opens]\w+",e.text)) or bool(re.search("[Clos]\w+",e.text)))):
          print(e.text)
          addresses.append(e.text)
    for f in name:
        print("name")
        print(f.text)
        names.append(f.text)
    for g in phone:
        if(bool(re.search(r'\d',g.text))):
            print(g.text)
            phones.append(g.text)
        elif(g.text!=''):
            openstatuses.append(g.text)
        else:
            phones.append('')
            openstatuses.append('')
    print(phones)
    print(names)
    print(addresses)
    print(openstatuses)

    score_titles = [{"name": t, "address": s,"phone":u,"status":w} for t,s,u,w in zip(names,addresses,phones,openstatuses)]
    shops=json.dumps(score_titles)
    driver.quit()
    return jsonify({"area":score_titles})


if __name__== "__main__":
    app.run(host='0.0.0.0',port=8080)