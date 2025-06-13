import requests
from bs4 import BeautifulSoup
import json
import re

class WikipediaScraper():
    def __init__(self):
        #,root_url, country_endpoint, leaders_endpoint, cookies_endpoint
        self.root_url: str = "https://country-leaders.onrender.com"
        self.country_endpoint: str = "/countries"
        self.leaders_endpoint: str = "/leaders"
        self.cookies_endpoint: str = "/cookie"
        self.leaders_data={}
        #cookie=Refresh_cookies()


    def refresh_cookies(self):
        self.cookie_url=self.root_url+"/cookie"
        r=requests.get(cookie_url)
        self.cookie=r.cookies
        return (self.cookie)
    
    
    
    def get_countries():
        self.countries=requests.get(self.root_url+self.country_endpoint, cookies=cookies).json()
        print(self.countries)
        
        
    def get_leaders(country: str) -> None
        self.country=[country for country in self.countries]
        
        self.leaders_url= self.root_url+self.leaders_endpoint

        #print(countries, len(countries))
        self.leaders_per_country={}
        self.wikipedia_url=[]
        for country in self.countries:
            params = {"country": c}
            selfleaders=requests.get(leaders_url, cookies=cookie, params=params).json()
            self.leaders_per_country[country]=self.leaders
        #print(leaders_per_country.keys())
        for leader in self.leaders_per_country.keys():
            self.l=self.leaders_per_country[leader]
            #print(type(l), len(l))
            for leader1 in selfleaders_per_country[leader]:
                #print(leader1)
                url=leader1["wikipedia_url"]
                leader1["leaders_intro"]=str(get_first_paragraph(url))
                        #print(leader1)
            return(leaders_per_country)
    def get_first_paragraph(wikipedia_url: str) -> str 
        #def get_first_paragraph(wikipedia_url):
       #print(wikipedia_url) # keep this for the rest of the notebook

        a=requests.get(wikipedia_url)
        content=a.content
        soup=BeautifulSoup(content, "html")

        paragraph= soup.find_all("p")
        first_paragraph_raw=[]
        for p in paragraph:
            if p.find("b") != None:
                p_index=paragraph.index(p)
                first_paragraph_raw.append(paragraph[p_index].get_text())
                pattern = re.compile(r"\[|\]|//|/xa0|\b\w+\s*ⓘ")
                first_paragraph = re.sub(pattern, "", str(first_paragraph_raw))
                return (first_paragraph)
                break
    def to_json_file(filepath: str) -> None 
        
        try:
            with open(filepath, "w") as leaders_file:
                json.dump(self.leaders_per_country, leaders_file)
            print("done")
        except Exception as e:
            print(f"file cant be saved: {e}")
    