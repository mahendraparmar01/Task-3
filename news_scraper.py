import requests
from bs4 import BeautifulSoup
import datetime


def scrape_news_headlines(url, output_filename="headlines.txt"):
    """
    Scrapes news headlines from a given URL and saves them to a text file.

    Args:
        url (str): The URL of the news website to scrape.
        output_filename (str): The name of the file to save the headlines to.
    """
    try:
        # 1. Use requests to fetch HTML
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        # 2. Use BeautifulSoup to parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find headline elements. Common tags for headlines are <h2>, <h3>, or <a>
        headlines = []

        # Common strategy 1: Look for <h2> tags (often used for main headlines)
        h2_headlines = soup.find_all("h2")
        for h2 in h2_headlines:
            text = h2.get_text(strip=True)
            if text:
                headlines.append(text)

        # Common strategy 2: Look for <h3> tags (often used for sub-headlines or article titles in lists)
        h3_headlines = soup.find_all("h3")
        for h3 in h3_headlines:
            text = h3.get_text(strip=True)
            if text:
                headlines.append(text)

        # Remove duplicates while preserving order
        unique_headlines = []
        seen = set()
        for headline in headlines:
            if headline not in seen:
                unique_headlines.append(headline)
                seen.add(headline)

        # 3. Save the titles in a .txt file
        with open(output_filename, "w", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"--- News Headlines Scraped on {timestamp} ---\n\n")
            if unique_headlines:
                for i, headline in enumerate(unique_headlines):
                    f.write(f"{i+1}. {headline}\n")
            else:
                f.write(
                    "No headlines found. Please check the URL and HTML structure.\n"
                )

        print(f"Successfully scraped headlines and saved them to '{output_filename}'")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    news_url = "https://www.bbc.com/news/world/asia/india"
    scrape_news_headlines(news_url, "headlines.txt")
