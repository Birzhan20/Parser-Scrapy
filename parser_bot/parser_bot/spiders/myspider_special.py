import scrapy

class KithSpider(scrapy.Spider):
    name = 'kith_special'
    allowed_domains = ['kith.com']
    start_urls = ['https://kith.com/collections/new-arrivals/products/kht030182-101']

    def parse(self, response):
        products = response.css('div.product__shop')
        for product in products:
            yield {
                'color': self.clean_text(product.css('h2.product__color::text').get()),

                # с элемента <span> берет цену
                'price': self.clean_text(product.css('span[aria-label="current price"]::text').get()),

                # списком собирает <label> с класса product-swatch__label
                'size': [self.clean_text(size) for size in response.css('label.product-swatch__label::text').getall()],

                #  * извлекает текст из все дочерних элементов <span>, <p> и тд.
                'description': self.clean_text(' '.join(
                    product.css('div.product__editors-note__content *::text'
                                ).getall())),

                #  списком собирает все <p> из класса product-description и через генератор списка чистится от пробелов
                'details': [
                    self.clean_text(detail) for detail in response.css('div.product-description p::text').getall()
                ],
            }

    def clean_text(self, text):
        if text:
            return ' '.join(text.split())
        return None
