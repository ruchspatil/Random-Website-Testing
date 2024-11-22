import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class TestRandomOrg(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = False 
        self.driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)
        self.driver.maximize_window()
    
    def test_page_load(self):
        driver = self.driver
        driver.get("https://www.random.org/")
        
        # Check if the page title is correct
        self.assertIn("Random.org", driver.title)
        print("Page loaded successfully.")
    
    def test_generate_random_number(self):
        driver = self.driver
        driver.get("https://www.random.org/integers/")
        
        time.sleep(2)
        
        # Locate the input fields for 'min' and 'max' values, and 'count'
        min_value = driver.find_element(By.ID, "min")
        max_value = driver.find_element(By.ID, "max")
        count_value = driver.find_element(By.ID, "num")
        
        # Input valid values into the form (for example: generating a random number between 1 and 100)
        min_value.clear()
        min_value.send_keys("1")
        max_value.clear()
        max_value.send_keys("100")
        count_value.clear()
        count_value.send_keys("1")
        
        # Submit the form
        count_value.send_keys(Keys.RETURN)
        
        time.sleep(3)
        
        # Check that a random number is displayed on the page
        result_text = driver.find_element(By.CLASS_NAME, "result").text
        self.assertIsNotNone(result_text)
        print("Random number generated:", result_text)

    def tearDown(self):
        # Clean up and close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
