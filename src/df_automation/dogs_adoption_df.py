from .scraping import Scraper
import pandas as pd

class Adoption_Dogs_df:
    LINK: str = 'https://www.letlive.org.il/?post_type=pet&pet-cat=pc-dog&gad_source=1&gclid=Cj0KCQiAz8GuBhCxARIsAOpzk8yQPS1FUcsf_698EN4NCo6qyC1-mPr_5bdS1eVt7g3J6uZIvTOUOGIaAqwnEALw_wcB&paged='
    
    def __init__(self):
        self.page  = 0
        self.result_df = pd.DataFrame()
        self.link = ''

    def edit_link(self):
        self.link = self.LINK + str(self.page)

    def create_df(self):
        number_of_pages = Scraper(self.LINK + '2').detemine_number_of_pages()
        for page in range(1, number_of_pages + 1):
            print(f'Page {page}')
            self.page = page
            self.edit_link()
            Scraper(self.link).get()
            df = Scraper(self.link).run()
            self.result_df = pd.concat([self.result_df, df], ignore_index=True)
        self.result_df.reset_index()
        self.result_df.to_csv('dogs.csv', encoding='utf-8-sig')
        return self.result_df
    