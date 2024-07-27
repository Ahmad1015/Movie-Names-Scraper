# Movie Names Scraper
This Python script scrapes movie names from an archived webpage of Empire Online and saves them to a text file.

## Requirements
- Python 3.x
- requests
- beautifulsoup4
## Install dependencies:
```bash
pip install requests beautifulsoup4
```
## How to Run
1. Clone/download the script.
2. Run the script:
```bash
   python movie_names_scraper.py
```
## Script Details
- Fetches webpage content from an archived Empire Online page.
- Parses HTML to extract movie names.
- Reverses the list of movie names.
- Writes the names to Movies Names.txt.
- Prints the list of names.
## Output
Creates Movies Names.txt with movie names in reverse order.

