from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import smtplib
from email.mime.text import MIMEText

def search_room(driver, start_date, end_date, hotel_name):
    location = driver.find_element_by_id("header-sn-location")
    arrival = driver.find_element_by_id("header-sn-arrival")
    departure = driver.find_element_by_id("header-sn-departure")
    adults = driver.find_element_by_id("header-adults")

    for option in location.find_elements_by_tag_name('option'):
        if option.text == hotel_name:
            option.click()

    arrival.clear()
    arrival.send_keys(start_date)

    departure.clear()
    departure.send_keys(end_date)

    for option in adults.find_elements_by_tag_name('option'):
        if option.text == "2":
            option.click()

    elem = driver.find_element_by_xpath("//input[@value='Search']")
    elem.click()
    time.sleep(1)
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)

    try:
        driver.find_element_by_class_name("btn-md")
        driver.close()
        return True
    except:
        driver.close()
        return False


def main():
    hotels = ['Canyon Lodge',
              'Grant Village',
              'Lake Lodge',
              'Mammoth Hotel and Cabins',
              'Old Faithful Inn',
              'Old Faithful Lodge',
              'Old Faithful Snow Lodge',
              'Roosevelt Lodge']
    dates = ['2017-07-01', '2017-07-02', '2017-07-03', '2017-07-04']
    summary_str = 'Hotel\t\t\t\tDate\t\t\tAvailability\n'

    driver = webdriver.Chrome()
    driver.get("http://www.yellowstonenationalparklodges.com/")
    bookTrip = driver.find_element_by_id("book")
    bookTrip.click()
    time.sleep(2)
    window_before = driver.window_handles[0]
    
    for hotel in hotels:
        for i in range(len(dates)-1):
            summary_str = summary_str + hotel + '\t\t' + dates[i] + '\t\t'
            
            if search_room(driver, dates[i], dates[i+1], hotel):
                summary_str = summary_str + 'Yes\n'
            else:
                summary_str = summary_str + 'No\n'

            driver.switch_to_window(window_before)
            
    driver.quit()
    print(summary_str)

if __name__ == '__main__':
    main()
