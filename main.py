from fastapi import FastAPI
from blic_data import blic_dict
from mondo_data import mondo_dict
app = FastAPI()

# root endpoint
@app.get("/")
def root():
    return{"Welcome":"to my Novak Djokovic 10 latest news API"}

# main endpoint
@app.get("/api")
def news_api():
    
    return {"Blic":blic_dict,"Mondo":mondo_dict}

