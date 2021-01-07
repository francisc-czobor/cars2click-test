import scrapy


class BrandSpider(scrapy.Spider):
    name = 'concession'
    start_urls = ['https://www.auto-concession.fr/']

    def parse(self, response):
        for link in response.css('.constructeur'):
            yield response.follow(link.css('a::attr(href)').get(), self.parse_item)

    def parse_item(self, response):
        for dealer in response.css('.conteneur li'):
            yield {
                'brand': response.css('h1.hidden-phone::text').get().split(' ', 1)[1].strip(),
                'dealer': dealer.css('h2::text').get(),
                'address': dealer.css('.legende').get().split('</div>')[1].replace('\n', '').replace('\t', '').replace('<br>', ' ').strip(),
                'tel': dealer.css('.buttons a::attr(href)').get().split(':')[1],
            }
