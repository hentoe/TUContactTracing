from datetime import date
from time import sleep
import sys
sys.path.extend(['/home/hendrik/PycharmProjects/TUcontact'])

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

from personal_data.data import data_to_submit
from src.log import convert_date, is_registered, write_log

# URL to contact tracing survey
contact_tracing_url = "https://redcap.zih.tu-dresden.de/redcap/surveys/?s=CNRACR4DFH"


def get_date(data=data_to_submit):
    # Get today's date and put it as string in data_to_submit dictionary
    date_string = convert_date(date.today())
    data["tag"] = date_string


def fill_in_data(data=data_to_submit):
    # Find html form elements
    element_classes = browser.find_elements_by_class_name("x-form-text")

    # Fill out form
    browser.find_element_by_class_name("date_dmy").clear()
    for element in element_classes:
        try:
            element_name = element.get_property("name")
            if element_name in data.keys():
                element.send_keys(data[element_name])
        except ElementNotInteractableException:
            # print(f"{element_name} not reachable by keyboard")
            pass

    # Fill out building
    elem_building = browser.find_element_by_id("rc-ac-input_gebaeude")
    elem_building.send_keys(data["gebaeude"])


def select_language(lang="Deutsch"):
    # Select language
    langButtons = browser.find_elements_by_class_name("setLangButtons")
    if len(langButtons) == 2:
        for item in langButtons:
            if item.get_attribute("name") == "Deutsch":
                item.click()


def submit():
    submit_button = browser.find_element_by_class_name("jqbutton")
    submit_button.click()


def close_window():
    while True:
        try:
            close_button = browser.find_element_by_class_name("jqbuttonmed")
            break
        except NoSuchElementException:
            sleep(1)
    close_button.click()
    browser.quit()


if __name__ == "__main__":
    if not is_registered():

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        # Choose your favourite browser by commenting/uncommenting
        browser = webdriver.Firefox(firefox_options=options)
        # browser = webdriver.Chrome()

        # Open browser with survey page
        browser.get(contact_tracing_url)

        get_date()
        fill_in_data()
        submit()
        close_window()

        # Add log
        write_log()
