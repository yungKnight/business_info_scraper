# business_info_scraper
This project is a portfolio project that extracts information for each registered business on the website 'christianlist.gdirect.com',<br>
cleans it up removing businesses that do not have the needed information filled. <br>
Since this is a portfolio project and not legally protected hence the need for me to hide certain info in my scrape code.
<br>
<br>
This code aims to emulate a search result for a specified state
but since all states share the same database, there is no need <br>
for a dynamic or parrallel run for all states in this code.

## Project Dependencies Version

- Python >= 3.12.1
- Scrapy >= 2.1.0
- Playwright >= 1.43.0

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repository_url>

2. **Navigate to your project directory**
   ```sh
   cd path/to/business_info_scraper
   
3. **Create a virtual environment:**
	```sh
	python -m venv venv
	```

4. **Activate virtual environment: (On windows)**
	```sh
	source venv\Scripts\activate
	```

5. **Install the required dependencies:**
	```sh
	pip install -r requirements.txt
	```
## Usage
1. **Navigate to your project directory**
   ```sh
   cd path/to/business_info_scraper

2. **Execute the scraper:**
   ```sh
   python info_scraper.py
