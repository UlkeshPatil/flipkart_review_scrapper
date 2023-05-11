import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from src.logger import logger
class FlipkartScraper:
    '''
    This class contains methods to scrap required data from flipkart website.
    Note: Will only scrap single page.
    '''
    def __init__(self, search_string):
        logger.info("Entered FlipkartScraper class")
        self.search_string = search_string
    
    def _get_search_url(self):
        return f"https://www.flipkart.com/search?q={self.search_string}"
    
    def _get_product_url(self, box):
        return f"https://www.flipkart.com{box.div.div.div.a['href']}"
    
    def _get_product_name(self,box):
        return box.findAll("div" , {"class":"_4rR01T"})[0].text
    
    def _get_comment_boxes(self, product_html):
        return product_html.find_all('div', {'class': '_16PBlm'})
    
    def _get_review_dict(self, commentbox,product):
        try:
            name = commentbox.div.div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
        except:
            name = 'No Name'

        try:
            rating = commentbox.div.div.div.div.text
        except:
            rating = 'No Rating'

        try:
            commentHead = commentbox.div.div.div.p.text
        except:
            commentHead = 'No Comment Heading'
        try:
            comtag = commentbox.div.div.find_all('div', {'class': ''})
            custComment = comtag[0].div.text
        except:
            custComment = 'No Comment'

        return {"Product": product, "Name": name, "Rating": rating,
                "CommentHead": commentHead, "Comment": custComment}

    
    def scrape_reviews(self):
        try:
            search_url = self._get_search_url()
            search_result = requests.get(search_url, timeout=10)
            search_html = BeautifulSoup(search_result.content, "html.parser")
            bigboxes = search_html.find_all("div", {"class": "_1AtVbE col-12-12"})
            del bigboxes[0:2]
            del bigboxes[-3:]
            all_reviews = []  # Accumulate all reviews in this list
            for box in tqdm(bigboxes):
                product_name = self._get_product_name(box)
                product_url = self._get_product_url(box)
                product_result = requests.get(product_url,timeout = 30)
                product_html = BeautifulSoup(product_result.content, "html.parser")
                comment_boxes = self._get_comment_boxes(product_html)

                reviews = []
                for commentbox in tqdm(comment_boxes):
                    review_dict = self._get_review_dict(commentbox,product_name)
                    reviews.append(review_dict)

                all_reviews.extend(reviews)

            return all_reviews 
        
        except Exception as e:
            logger.error(e)

