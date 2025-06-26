# 📰 BBC India News Headlines Scraper

This Python script scrapes the latest headlines from the [BBC India News](https://www.bbc.com/news/world/asia/india) page using `requests` and `BeautifulSoup`, and saves them to a `.txt` file with a timestamp.


## ✅ Features

- Scrapes headlines from HTML tags like `<h2>` and `<h3>`
- Automatically filters duplicates
- Saves headlines to a `.txt` file with the current timestamp
- Gracefully handles connection and parsing errors


## 📦 Requirements

- Python 3.x  
- Dependencies:
  - `requests`
  - `beautifulsoup4`

### Install dependencies:

```bash
pip install requests beautifulsoup4
