
# Stack Spider

**stack-spider** is a Python web scraper designed for a freelance gig where the client required a program to scrape data from any website, specifically targeting new questions. The scraped data includes the question title and URL. All collected information is then stored in MongoDB. As per the client's specifications, this project is focused on delivering a robust and efficient web scraper.

## File Structure

The project has the following file structure:
├── scrapy.cfg
└── stack
├── init.py
├── items.py
├── pipelines.py
├── settings.py
└── spiders
└── init.py


- **scrapy.cfg:** The configuration file for the Scrapy project.
  
- **stack:** The main directory for the Scrapy project.

    - **__init__.py:** An empty file to indicate that the directory should be considered a Python package.
    
    - **items.py:** Defines the data structure (items) for the scraped data.
    
    - **pipelines.py:** Contains the logic for processing scraped items, such as storing them in MongoDB.
    
    - **settings.py:** Configuration settings for the Scrapy project.
    
    - **spiders:** A directory to contain spider modules.

        - **__init__.py:** An empty file to indicate that the directory should be considered a Python package.
