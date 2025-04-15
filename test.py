# from fundus import PublisherCollection, Crawler
# import json
# # Change to:
# # PublisherCollection.<country_section>.<publisher_specification>
# publisher = PublisherCollection.cz.iRozhlas
# from tqdm import tqdm
# crawler = Crawler(publisher)

# for article in tqdm(crawler.crawl(max_articles=3, only_complete=False,save_to_file="bla.json")):
#     print(article)
#     # with open("bla.json","w") as f:
#     #     json.dump(article.to_json(),f,ensure_ascii=False)

from datetime import datetime

from fundus import CCNewsCrawler, PublisherCollection


crawler = CCNewsCrawler(*PublisherCollection.cz, start=datetime(2022, 1, 1), end=datetime(2022, 3, 1),processes=5)
for article in crawler.crawl(max_articles=100):
    print(article)