# imdb-pybr2022

Web scraping tutorial presented at [Python Brasil 2022](https://pretalx.com/python-brasil-2022/talk/JGXM7G/).
Fetches the IMDB Top 250 list, parses the HTML with BeautifulSoup, and prints a
random title from the ranking.

## Stack

- Python 3.9+ · requests · BeautifulSoup4 · lxml

## Running

```bash
python -m venv .venv && source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate                             # Windows

pip install -r requirements.txt
python imdb.py
```

## What it does

1. Fetches `https://www.imdb.com/chart/top/`
2. Parses the `tbody.lister-list` table with BeautifulSoup + lxml
3. Builds a list of `{"Nome do Filme": ..., "Ano": ...}` dicts
4. Prints one random entry
