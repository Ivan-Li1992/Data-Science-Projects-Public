import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep

class ZoocasaSpider(scrapy.Spider):
    name = 'zoocasa'
    allowed_domains = ['www.zoocasa.com']
    #start_urls = ['zoocasa.com']


    def start_requests(self):
        
        self.driver = webdriver.Chrome('/Users/ivan/Downloads/chromedriver')
        
        self.driver.maximize_window()                                                                                                                                                                                              
        sleep(0.5) 

        self.driver.get("https://www.zoocasa.com/real-estate")
        sleep(3)

        self.driver.find_element_by_xpath("(//a[text() = 'Sign in'])[1]").click()
        sleep(2)
       
        user_input = self.driver.find_element_by_xpath("//input[@type='email']")  
        #//input[@placeholder='Email Address']
        user_input.send_keys('lixianji55@gmail.com') 
        sleep(2)
 
        password_input = self.driver.find_element_by_xpath("//input[@type='password']")
        password_input.send_keys('Summer2020')  
        sleep(3)
 
        self.driver.find_element_by_xpath("//button[text() ='Sign in']").click() 
        sleep(5)

        #Active listing 
        self.driver.find_element_by_xpath("(//span[@class='label'])[2]").click() 
        sleep(2)

        #Sold Listings radio button
        self.driver.find_element_by_xpath("//radio-buttons/div/span[@role='button'][2]").click() 
        sleep(2)

        #Hometype
        self.driver.find_element_by_xpath("(//span[@class='label'])[3]").click() 
        sleep(2)

        #Hometype House button
        self.driver.find_element_by_xpath("(//div/section/div/div/checkbox-input/span[@role = 'button'])[1]").click() 
        sleep(2)

        #Hometype Townhouse button
        self.driver.find_element_by_xpath("(//div/section/div/div/checkbox-input/span[@role = 'button'])[2]").click() 
        sleep(2)

         #Hometype apply button
        self.driver.find_element_by_xpath("(//button[@class='apply'])[1]").click() 
        sleep(2)

        for i in range(482):
            sel = Selector(text=self.driver.page_source)

            links = sel.xpath("//div[@class='card-wrapper']/listing-card/div/a/@href").extract()
            

            for link in links:
                url = 'https://www.zoocasa.com' + link
                yield Request(url, callback=self.parse, meta={'URL':url})

            sleep(3)
            self.driver.find_element_by_xpath('(//pagination-nav/a)[2]').click()
            sleep(12)


    def parse(self, response):
        URL = response.meta.get('URL')   
        status = response.xpath('(//listing-status)[1]/text()[1]').extract()
        Type = response.xpath('(((//details-table)[1]/section/div)[2]/span)[2]/text()').extract()
        level= response.xpath('(((//details-table)[1]/section/div)[3]/span)[2]/text()').extract()
        mgmt_fee = response.xpath('(((//details-table)[1]/section/div)[5]/span)[2]/text()').extract()
        property_tax = response.xpath('(((//details-table)[1]/section/div)[6]/span)[2]/text()').extract()
        Locker = response.xpath('(((//details-table)[1]/section/div)[7]/span)[2]/text()').extract()
        Ensuite_Laundry = response.xpath('(((//details-table)[2]/section/div)[1]/span)[2]/text()').extract()
        Balcony = response.xpath('(((//details-table)[2]/section/div)[2]/span)[2]/text()').extract()
        Laundry_Level = response.xpath('(((//details-table)[2]/section/div)[4]/span)[2]/text()').extract()
        Exposure = response.xpath('(((//details-table)[2]/section/div)[5]/span)[2]/text()').extract()
        Exterior = response.xpath('(((//details-table)[3]/section/div)[1]/span)[2]/text()').extract()
        Garage = response.xpath('(((//details-table)[3]/section/div)[2]/span)[2]/text()').extract()
        Approx_Age = response.xpath('(((//details-table)[3]/section/div)[3]/span)[2]/text()').extract()
        Stories = response.xpath('(((//details-table)[3]/section/div)[4]/span)[2]/text()').extract()
        pets = response.xpath('(((//details-table)[3]/section/div)[5]/span)[2]/text()').extract()
        Elevator = response.xpath('(((//details-table)[3]/section/div)[7]/span)[2]/text()').extract()
        city = response.xpath('(//address[@class="region-wrapper"]/span)[1]/text()[1]').extract()
        Province = response.xpath('(//address[@class="region-wrapper"]/span)[2]/text()').extract()
        Address = response.xpath("//span[@class='street']/text()").extract()
        num_bed = response.xpath("//div[@class='beds-baths']/span[1]/text()[1]").extract()
        num_bath = response.xpath("//div[@class='beds-baths']/span[2]/text()[1]").extract()
        num_parking = response.xpath("//div[@class='beds-baths']/span[4]/text()").extract()
        sf_range = response.xpath("//div[@class='beds-baths']/span[3]/text()").extract()
        list_price = response.xpath("((//div[@class='list-price'])[1]/span)[1]/text()").extract()
        sold_price = response.xpath("((//div[@class='sold-price'])[1]/span)[1]/text()").extract()

        yield {
        'URL': URL,
        'status': status,
        'Type': Type,
        'level': level,
        'mgmt_fee': mgmt_fee,
        'property_tax': property_tax,
        'Locker': Locker,
        'Ensuite_Laundry': Ensuite_Laundry,
        'Balcony': Balcony,
        'Laundry_Level': Laundry_Level,
        'Exposure': Exposure,
        'Exterior': Exterior,
        'Garage': Garage,
        'Approx_Age': Approx_Age,
        'Stories': Stories,
        'pets': pets,
        'Elevator': Elevator,
        'city': city,
        'Province': Province,
        'Address':Address,
        'num_bed':num_bed,
        'num_bath': num_bath,
        'num_parking': num_parking,
        'sf_range': sf_range,
        'list_price': list_price,
        'sold_price': sold_price
        }




