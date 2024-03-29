from .driver import Driver
import pandas as pd
from selenium.webdriver.common.by import By

class Scraper:
    def __init__(self, link):
        self.driver = Driver()
        self.all_links, self.row, self.images  = [], [], []
        self.link = link
        self.textual_discription = ''
        self.index = 0
        self.true_elements = []
        self.df = pd.DataFrame(columns=['Discription', 'Name', 'Age', 'Date', 'Sex', 'Size', 'Color', 'Education', 'Breed', 'Adjusted to'])

    def get(self):
        self.driver.get(self.link)

    def detemine_number_of_pages(self):
        # Find the last page element
        self.driver.get(self.link)
        last_page_element = self.driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/ul/li[11]/a')
        link = last_page_element .get_attribute('href')
        num_of_pages = int(link[-2:])
        return num_of_pages

    def find_all_links(self):
        # Find all elements with class 'post_content col-sm-6'
        all_elements = self.driver.find_elements(By.CLASS_NAME, 'post_content.col-sm-6')

        # Iterate through the 'post_content col-sm-6' elements
        for element in all_elements:
            # Find all 'a' elements within each 'post_content col-sm-6' element
            a_elements = element.find_elements(By.TAG_NAME, 'a')
            image_element = element.find_element(By.TAG_NAME, 'img')
            # Iterate through the 'a' elements and print their href attribute
            for a_element in a_elements:
                href = a_element.get_attribute('href')
                if href != None:
                    self.all_links.append(href)
                    self.images.append(image_element.get_attribute('src'))

    def fix_textual_discription(self, text: str):
        for paragraph in text:
            for sen in paragraph.split('.'):
                sen = sen
                self.textual_discription += sen + '.'
        self.row.append(self.textual_discription)
        self.textual_discription = ''

    def fix_details(self, details_list: list):
        details_list = [sen for sen in details_list[self.index:]]
        for index, detail in enumerate(details_list):
            if index % 2 == 1:
                self.row.append(detail)


    def catch_name_index(self, details_list: list):
        for index, detail in enumerate(details_list):
            if detail == 'שם':
                self.index = index

  
    def get_info(self):
        # Find the element with class 'entry-content'
        for indexx, link in enumerate(self.all_links):
            self.driver.get(link)
            details = self.driver.find_elements(By.CLASS_NAME, 'all-details')
            for details_element in details:
            # Get the text content of each 'all-details' element
                details_text = details_element.text
                self.arrange_info_in_df(details_text, indexx)
        self.df['Image'] = [self.images[i] for i in self.true_elements]
        self.df['Link'] = [self.all_links[i] for i in self.true_elements]

    
    def arrange_info_in_df(self, details_text: str, indexx: int):
        details_list = details_text.split('\n')
        self.catch_name_index(details_list)
        self.fix_textual_discription(details_list[:self.index])
        self.fix_details(details_list)
        if len(self.row) == 10:
            self.true_elements.append(indexx)
            self.df.loc[len(self.df.index)] = self.row
        self.row = []

                
    def run(self):
        self.get()
        self.find_all_links()
        self.get_info()
        self.driver.quit()
        return self.df

# scraper = Scraper('https://www.dog.org.il/adoptions/')