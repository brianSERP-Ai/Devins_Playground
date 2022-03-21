# Import the beautifulsoup
# and request libraries of python.
import requests
import time
from collections import Counter
from nltk.util import ngrams 
import bs4
from collections import Counter
import csv
from time import sleep
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome()
chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)
with open('PAGELEVELserp.csv', 'w',newline='' , encoding="utf-8") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(["ID","TERM","CONTEXT"])

# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them

import pandas as pd
url = 'PAGE LEVEL serp.co content - about 1500 posts.csv'
df1 = pd.read_csv(url ,encoding="utf-8" ,engine="python",warn_bad_lines=True, error_bad_lines=False)
df1 =df1

# Dataset is now stored in a Pandas Dataframe
for ID, TERM in zip(df1['ID'],df1['TERM']):
    ID = str(ID)
    TERM =str(TERM)
    text= f"{TERM} for sale Amazon"
    url = 'https://google.com/search?q=' + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
    MAX_RETRY = 100
    retries = 0
    
    try:
        driver.get(url)
        
        request_result=requests.get( url )
        # Creating soup from the fetched request
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        
        
    except Exception as exception:
        if retries <= MAX_RETRY:
            print("ERROR=Method failed. Retrying ... #%s", retries)
            time.sleep(1) 
            continue
        else:
            raise Exception(exception)
    
#print(soup)
# soup.find.all( h3 ) to grab 
# all major headings of our search result,
    try:
        heading_object1=soup.find_all("h1")
        time.sleep(0.1)
        heading_object2=soup.find_all("h2")
        time.sleep(0.1)
        heading_object3=soup.find_all("h3")
        time.sleep(0.1)
        heading_object4=soup.find_all("p")
        time.sleep(0.1)
    except:
        continue
    
# Iterate through the object 
# and print it as a string.
    all_words = ""
    for info in heading_object1:
        all_words += info.getText()
    for info in heading_object2:
        all_words += info.getText()
    for info in heading_object3:
        all_words += info.getText()
    for info in heading_object4:
        all_words += info.getText()
        
        
    
    all_words = all_words.replace("-"," ").replace("|"," ").replace(","," ").replace("["," ").replace("]"," ").replace(":"," ").lower()  
    BLACKLIST = [
        "area","made","for","web","india", "snippet","accurate", "history", "accurate", "sales",'still','ultimate','definition','premium','choice','behind','risks','help','google','askgoogle','web','ask','that', 'out', 'haven', 'your', 'once', 'again', 'off', 'with', 'under', 'aren', 'were', "needn't", 'this', 'each', 'while', "you'll", 'they', 'll', 'shouldn', 'won', 'my', 'own', 'don', 'both', 'a', 'or', 've', 'so', 'at', 's', 'have', 'those', 'ours', 'where', 'its', 'wasn', "you're", 'these', 'yourself', 'having', 'most', 'from', 'any', 'below', 'their', 'between', "should've", 'of', 'm', "shan't", 'for', 'them', 'no', 'in', 'her', 'yourselves', "couldn't", 'nor', 'now', 'his', 'didn', 'being', "wouldn't", 'further', 'he', 'against', 'by', 'if', 'before', 'me', 'because', 'hasn', 'be', 'whom', 'we', 'and', 'until', 'doing', 'mightn', 'why', 'about', 'herself', 'itself', 'the', "weren't", 'our', 'you', 'above', 'can', 'up', 'what', 'theirs', 'than', 'only', 'just', "shouldn't", "hasn't", 'do', 'myself', "that'll", 'who', 'couldn', 'other', 'to', "won't", 'an', 'but', 'here', 'needn', 'does', 'when', 'yours', 'did', 'same', 'himself', 'isn', 'ourselves', "mustn't", 'such', 'during', "doesn't", 'too', 'over', 'ain', "you'd", "don't", 'some', "haven't", 're', "wasn't", 'weren', 'been', 'through', 'has', 'as', 'are', 'few', 'will', 'ma', 'there', 'themselves', 'how', 'is', 'which', 'on', 'i', 'very', 'was', 'more', "it's", 'y', 'him', 'hadn', "didn't", 'then', 'd', 'down', 'all', 'o', "isn't", 'after', 'she', "she's", "hadn't", 'should', "mightn't", 'had', "aren't", "you've", 'hers', 'shan', 'it', 'into', 'not', 'doesn', 'mustn', 'wouldn', 'am', 't',"free","shipping","offers","helpline","support","customer","costco","ebay",")","(","?", "online","previous","guide","best","updated","...",".com",".html","wikipedia","amazon","discount","homepage","preowned","youtube","configurable","products",'2020',"brands",'2021','2022','review',"[buyer's","manufacturers","manufacturers","choose","every","results","this","dozen)","clearance","(utility","width","with","men's",'show','product','prices','models','primeblue','sale','wonderful','excellent','great','your','piece','new','pick','specs','preloved','used','of','that','these','should','everything','you','need',"about",'right','choosing','know','are','what', 'what','type','between','for','best','and','which','the','put','review','&','ivory','olive','the','blue','orange',"red","pink","green","yellow","white","black","turquoise", "blue-violet", "red-violet", "yellow-green", "red-orange", "yellow-orange", "blue-green","Violet","Aqua","Cyan","Brown",'also']
    all_words_list = all_words.split()
    
    deleteAsk = []
    for i in all_words_list:
        
        if i[0:3] == "ask":
            del i
        elif i[0:3] == "web":
            del i
        else:
            deleteAsk.append(i)
            
        
        

    newray = []
    
    for i in deleteAsk:
        if len(i)>3:
            newray.append(i)
    
    cleanlist = [word for word in newray if word not in BLACKLIST]
    
    BLACKLIST2 = ["seller","what", "insider", "snippet","india", "snippet","accurate", "history", "accurate", "sales","investopedia","benefits","askthe","people","people",'actually','results',"modesquick","modesquick","modesquick","footer","navigation","resultspage","search","accessibility","settingssearch","link","research","consulting","free","shipping","offers","helpline","support","customer","costco","ebay",")","(","?", "online","previous","guide","best","updated","...",".com",".html","wikipedia","amazon","discount","homepage","preowned","youtube","configurable","products",'2020',"brands",'2021','2022','review','details']
    
    cleanlist = [word for word in cleanlist if not any(
        bad in word for bad in BLACKLIST2)]  
    

        
        
    
    counts = Counter(cleanlist)
    context = counts.most_common(5)
    #context = str(context).replace("('","").replace(")","").replace("(","").replace('"',"").replace("'","").replace("1","").replace("2","").replace("3","").replace("0","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("10","").replace(" , ","").replace(", ","").replace(",",", ")
    
    forngrams = " ".join(cleanlist)
    
    print(TERM)
    n_gram = 2
    
    counts2 = Counter(ngrams(forngrams.split(), n_gram))
    context2 = counts2.most_common(3)
    
    try:
        context = context2[0][0][0]+" "+context2[0][0][1]+", "+ context2[1][0][0]+" "+ context2[1][0][1]+", "+ context2[2][0][0]+" "+ context2[2][0][1]
    except:
        context = context2
    
    print(context)
    print("\n")
    
    

    
 
    #print(selected_items)
    
    
        
    with open('PAGELEVELserp.csv', 'a+', newline='', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([ID, TERM, context])