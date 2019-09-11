import requests
import time
import scrapy
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
import csv

class Moneda(Item):
    tipo = Field()
    compra = Field()
    venta = Field()
   # fecha = Field()



class ElCronista(Spider):
    name = "Spider"
    start_urls= ['https://www.cronista.com/MercadosOnline/dolar.html']

    def parse(self, response):

        
        sel = Selector(response)
        cotis = sel.xpath('//tr')

        for i, elem in enumerate(cotis[1:2]):
            item = ItemLoader(Moneda(), elem)
           
            item.add_xpath('compra', './/td[@id="dcompra0"]/text()') 
            item.add_xpath('venta', './/td[@id="dventa0"]/text()')
            item.add_xpath('tipo', './/td/a/text()', MapCompose(lambda j: j[15:33]))
            
            yield item.load_item()

        for i, elem in enumerate(cotis[2:3]):
            item = ItemLoader(Moneda(), elem)
           
            item.add_xpath('compra', './/td[@id="dcompra1"]/text()') 
            item.add_xpath('venta', './/td[@id="dventa1"]/text()')
            item.add_xpath('tipo', './/td/a/text()', MapCompose(lambda j: j[15:25]))
           
            yield item.load_item()

        for i, elem in enumerate(cotis[3:]):
            item = ItemLoader(Moneda(), elem)
          
            item.add_xpath('compra', './/td[@id="dcompra2"]/text()')
            item.add_xpath('venta', './/td[@id="dventa2"]/text()')
            item.add_xpath('tipo', './/td/a/text()', MapCompose(lambda j: j[11:28]))
            yield item.load_item()

       
        #  item = scrapy.loader.ItemLoader(Moneda(),response)
       # item.add_xpath('fecha','//span[@class="fecha-cronista"]/text()', MapCompose(lambda j: j[18:28]))
       # yield item.load_item()
      
