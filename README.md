# cars2click-test

This app was written during the cars2click recruitment process.

Its purpose is to scrape the car dealership data from [this](https://www.auto-concession.fr/) website. The output format is a JSON file containing a list of data points with the following format:
```json
  {
    "brand": "Car Brand",
    "dealer": "Car Dealership",
    "address": "The address",
    "tel": "0123465789"
  }
```

#### Installation

You need Python 3.6+ and the Scrapy Python library. I recommend using a virtual environment.

To create a virtual environment run `python3 -m venv venv`. Then you need to activate it by running `source venv/bin/activate`.

Install all the required components (_in the activated virtual environment_) by running `python -m pip install -r requirements.txt` from the root of the project.

For more information check the following links:

 - [Virtual Environments](https://docs.python.org/3/tutorial/venv.html#tut-venv)
 - [Scrapy Installation Guide](https://docs.scrapy.org/en/latest/intro/install.html)

#### Run the scraper

To run the scraper you have to run the following command from the _concession_ directory:
```bash
scrapy crawl concession -O results.json
```
This command will create a JSON file called _results.json_ in the _concession_ directory which contains the scraped data. From my testing the crawler manages to scrape 4882 data points.