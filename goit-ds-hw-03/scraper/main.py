import json
from typing import List, Dict
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://quotes.toscrape.com'


def get_soup(url: str) -> BeautifulSoup:
    """Fetches the page and returns a BeautifulSoup object."""
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def scrape_quotes_and_authors() -> None:
    """Scrapes quotes and authors from paginated pages."""
    quotes_data: List[Dict] = []
    authors_data: Dict[str, Dict] = {}

    page = 1
    while True:
        url = f"{BASE_URL}/page/{page}/"
        soup = get_soup(url)

        quotes = soup.find_all("div", class_="quote")
        if not quotes:
            break

        for quote in quotes:
            text = quote.find("span", class_="text").get_text(strip=True)
            author_name = quote.find("small", class_="author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
            author_link = quote.find("a")["href"]
            quotes_data.append({"quote": text, "author": author_name, "tags": tags})
            # If author is new, fetch additional details
            if author_name not in authors_data:
                author_details = get_author_details(BASE_URL + author_link)
                authors_data[author_name] = author_details

        print(f"Page {page} scraped successfully.")
        page += 1

    # Save data to JSON files
    save_to_json("authors.json", list(authors_data.values()))
    save_to_json("quotes.json", quotes_data)
    print("Data successfully saved to authors.json and quotes.json.")


def get_author_details(url: str) -> Dict:
    """Fetches author details from their page."""
    soup = get_soup(url)
    return {
        "fullname": soup.find("h3", class_="author-title").get_text(strip=True),
        "born_date": soup.find("span", class_="author-born-date").get_text(strip=True),
        "born_location": soup.find("span", class_="author-born-location").get_text(strip=True),
        "description": soup.find("div", class_="author-description").get_text(strip=True)
    }


def save_to_json(filename: str, data) -> None:
    """Saves data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    scrape_quotes_and_authors()
