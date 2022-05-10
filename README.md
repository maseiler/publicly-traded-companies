# Publicly Traded Companies

Do you want to know early on if the company you are following is finally listed on a stock exchange? This script checks whether a company is traded publicly or privately by scraping [MarketWatch](https://www.marketwatch.com/).

## Installation
Install the required python packages
```bash
pip install beautifulsoup4 lxml selenium
```
Install your version of the [WebDriver for Chrome](https://chromedriver.chromium.org/downloads) and make sure it is in your `PATH` (e.g. place it in `/usr/bin` or `/usr/local/bin`).

## Run It!
Provide a space-delimited list with company names (use quotation marks if company name contains spaces).
```bash
python3 main.py Apple "Microsoft Research"
```
The results are written to a JSON file.
