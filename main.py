from os import curdir
from fastapi import FastAPI,Path
from scrape import blic_funct,mondo_funct
app = FastAPI()

# root endpoint
@app.get("/")
def root():
    return{"Welcome":"to my Novak Djokovic 10 latest articles API"}

# main endpoint
@app.get("/api")
def news_api():
    blic_json = blic_funct(5)
    mondo_json = mondo_funct(5)
    return {"Blic":blic_json,"Mondo":mondo_json}

# custom endpoint
@app.get("/api/{custom_num}")
def custom_news_api(custom_num:int=Path(5,
    description="Please enter number of articles between 1 and 10",
    gt=0, 
    lt=11
)):
    blic_json = blic_funct(custom_num)
    mondo_json = mondo_funct(custom_num)
    return {"Blic":blic_json,"Mondo":mondo_json}
