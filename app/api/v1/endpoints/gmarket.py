from fastapi import APIRouter
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

router = APIRouter()

@router.get("/item")
def read_users():
    return [{"id": 1, "name": "apple", "original_price" : 20000, "sales_price" : 18000}, 
            {"id": 2, "name": "banana", "original_price" : 10000, "sales_price" : 7000}]

@router.post("/item/{group_name}")
async def clawling_item(group_name: str):

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox') # linux 환경 권한 문제
    driver = webdriver.Chrome(options=options)
    with open('app/api/v1/endpoints/gmarket.yaml') as f:
            file = yaml.full_load(f)

    if group_name == 'best':
        driver.get('https://www.gmarket.co.kr/n/best')
    else:
        if group_name in file['Gmarket']: # fresh, frozen, daily_necessities, kitchen
            group_catecogry = file['Gmarket'][f'{group_name}']
            group_code = group_catecogry['groupCode']
            driver.get(f'https://www.gmarket.co.kr/n/best?groupCode={group_code}')
    data = []
    for i in range(1, 201):
            try:
                item_selector = f"//div[@id='container']/div[2]/ul/li[{i}]"
                item_element = driver.find_element(By.XPATH, item_selector)

                rank = item_element.find_element(By.XPATH, ".//a/div[1]/span").text
                name = item_element.find_element(By.XPATH, ".//a/div[2]/p").text
                
                try:
                    original_price = item_element.find_element(By.CSS_SELECTOR, "div.box__price-original > span.text.text__value").text
                except:
                    original_price = 'N/A'
                try:    
                    sale_price = item_element.find_element(By.CSS_SELECTOR, "div.box__price-seller > span.text.text__value").text
                except:
                    sale_price = 'N/A'

                data.append((rank, name, original_price, sale_price))
            except Exception as e:
                f"Error occurred: {e}"
    
    driver.quit()
    
    return data