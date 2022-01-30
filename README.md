# Novak Djokovic latest news REST API
This is my second Fast Api project. Main purpose of of this Api project is to scrape information 
about articles on subject Novak Djokovic from two Serbian websites, blic.rs, and mondo.rs, and also to provide an endpoint with information about specific number of latest articles from each website. It features multiprocessing, so it should provide fast response.

This REST API project is live on Heroku: https://novak-djokovic-latest-news-res.herokuapp.com

Main endpoint, provides information about 5 latest articles from each website: https://novak-djokovic-latest-news-res.herokuapp.com/api

Custom endpoint, client can choose between 1 and 10 latest articles: https://novak-djokovic-latest-news-res.herokuapp.com/api/{number_of_articles}

Interactive documentation automatically created by Fast Api: https://novak-djokovic-latest-news-res.herokuapp.com/docs

