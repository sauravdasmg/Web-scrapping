import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(url=absolute_url)
            yield  response.follow(url=link, callback=self.parse_country, meta={'country_name':name})

    def parse_country(self,response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath("//td[2]/strong/text()").get()
            yield{
                'country_name': name,
                'year': year,
                'population': population
            }
name = 'glassesshop'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath('//div[@id="product-lists"]/div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'):
            yield {
                'product url': product.xpath('.//[@id="product-lists"]/div[1]/div[3]/a[1]/@href').get(),
                'product image link': product.xpath('.//[@id="product-lists"]/div[1]/div[3]/a[1]/img[1]/@href').get(),
                'product name': product.xpath('.//div[@class="p-title"]/a/text()').get(),
                'product price': product.xpath('.//div[@class="product-title p-tab p-tab-15396"]/span/text()').get()
            }
# scrapy crawl glassesshop -o dataset.json