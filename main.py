import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

chrome_driver_path = "/Users/Özkan Selçuk/PycharmProjects/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

headers = {
    "Accept-Language": "tr,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
}

url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.9987815756836%2C%22east%22%3A-122.19540633154297%2C%22south%22%3A37.538007093471194%2C%22north%22%3A37.973395840415876%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A605057%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
response = requests.get(url=url, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
price = soup.find_all(name="div", class_="list-card-price")
prices = [rent.getText() for rent in price]

address = soup.find_all(name="address", class_="list-card-addr")
addresses = [adr.getText() for adr in address]

url = soup.find_all(name="a", href=True, class_="list-card-link list-card-link-top-margin list-card-img", tabindex="-1")
urls = [a["href"] for a in url]

driver.get("https://docs.google.com/forms/d/e/1FAIpQLScebIJjYAe4lwj7zYptNNPVmBuTStrddRe_VqfSbNFCXJfHVQ/viewform?usp=sf_link")

for i in range(len(prices)):
    try:
        time.sleep(1)
        st_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        st_address.send_keys(addresses[i])

        st_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        st_price.send_keys(prices[i])

        st_url = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        st_url.send_keys(urls[i])

        st_send = driver.find_element_by_css_selector(".exportButtonContent")
        st_send.click()

        time.sleep(1)
        st_turnback = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        st_turnback.click()

    except:
        st_send = driver.find_element_by_css_selector(".exportButtonContent")
        st_send.click()

        time.sleep(1)
        st_turnback = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        st_turnback.click()
        driver.quit()
