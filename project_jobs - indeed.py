#importing libraries
import time
from selenium import webdriver
import pandas as pd
import datetime


#function to take input from the user
def job_in():
    job = input()
    job = job.replace(" ","+")
    return job

strings = job_in()

print('strings=',strings)


#creating chrome driver
driver  = webdriver.Chrome("C://Users//Kshitiz//Downloads//chromedriver")
times=[]

#https://in.indeed.com/jobs?q=data+scientist&start=0
driver.get("https://in.indeed.com/jobs?q={}&start{}".format(strings,"#"))

#fleft grey-text mr-5 fs12

# =============================================================================
# count = int(driver.find_element("css selector",".fleft.grey-text.mr-5.fs12").text[-5:])
# 
# 
# print('count=',count)
# =============================================================================
wait = 5
#data scrapped from the website
jobs = {
        "roles":[],
        "companies":[],
        "locations":[],
        "experience":[],
        "skills":[],
        "salary":[],
        "links":[]
        }

for i in range(1):
    page = i*10
    driver.get("https://in.indeed.com/jobs?q={}&start={}".format(strings,page))
    time.sleep(1)
    # print("i= ",i)
    # print("page= ",page)
    lst=driver.find_elements("css selector",".slider_container.css-g7s71f.eu4oa1w0")
    j=0
    for job in lst:
        driver.implicitly_wait(wait)
        role=job.find_element("css selector",".jcs-JobTitle.css-jspxzf.eu4oa1w0").text
        company=job.find_element("class name","companyName").text
        location=job.find_element("class name","companyLocation").text
        try:
            exp=job.find_element("css selector","div.heading6.tapItem-gutter.metadataContainer.noJEMChips.salaryOnly").text
        except:
            exp = ""
        
        try:
            salaries=job.find_element("css selector","div.metadata.salary-snippet-container").text
        except:
            salaries = ""
            
        print("j=",j)
        links = job.find_element("css selector",".jcs-JobTitle.css-jspxzf.eu4oa1w0").get_attribute("href")
        jobs["roles"].append(role)
        jobs["companies"].append(company)
        jobs["locations"].append(location)
        jobs["experience"].append(exp)
        jobs["links"].append(links)
        jobs["salary"].append(salaries)
        j = j+1
        
# b = datetime.datetime.now()
# c = b-a

# times.append([c,wait])
data = pd.DataFrame(jobs)
data.to_csv("product_analyst_jobs1.csv")

# =============================================================================
#dataset = pd.read_csv("product_analyst_jobs1.csv",index_col = 0)

#dataset.isna().sum()
#dataset  = dataset.dropna()

#dataset=dataset.apply(lambda x: x.astype(str).str.lower())

#dataset.skills = [skill.split("\n") for skill in dataset.skills]
#dataset.locations = [location.split(",") for location in dataset.locations]

# =============================================================================
