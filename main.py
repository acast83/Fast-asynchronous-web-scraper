"""Main module"""
import concurrent.futures
from fastapi import FastAPI, Path
from scrape import blic_funct, mondo_funct


app = FastAPI()


@app.get("/")
def root():
    """
    root endpoint
    """
    return {"Welcome": "to my Novak Djokovic 10 latest articles API"}


# main endpoint
@app.get("/api")
def news_api():
    """multiprocessing """
    with concurrent.futures.ProcessPoolExecutor() as executor:

        blic_json = executor.submit(blic_funct, 5)
        mondo_json = executor.submit(mondo_funct, 5)
        return {"Blic": blic_json.result(), "Mondo": mondo_json.result()}


# custom endpoint
@app.get("/api/{custom_num}")
def custom_news_api(
    custom_num: int = Path(
        5, description="Please enter number of articles between 1 and 10", gt=0, lt=11
    )
):
    """multiprocessing"""
    with concurrent.futures.ProcessPoolExecutor() as executor:

        blic_json = executor.submit(blic_funct, custom_num)
        mondo_json = executor.submit(mondo_funct, custom_num)
        return {"Blic": blic_json.result(), "Mondo": mondo_json.result()}
