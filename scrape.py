import selenium.webdriver as webdriver  # controlling web browsers programmatically
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup


def scrape_website(website):
    print("launching chrome browser")

    # path to the chrome driver
    chrome_driver_path = "./chromedriver"

    # options to configure the chrome browser, must be initialized!
    options = webdriver.ChromeOptions()

    # create a new chrome browser instance
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # open the website
        driver.get(website)  # open the website
        print(f"Page loaded - {driver.title}")  # print the page title
        html = driver.page_source
        # wait for 10 seconds
        time.sleep(3)
        # get the html of the page
        return html
    finally:
        driver.quit()  # close the browser


# Extract html body content and stringify them.
def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body

    # If body content exists, return stringified body content
    if body_content:
        return str(body_content)
    return ""


# Clean the body content by removing scripts, styles, and extra whitespace
def clean_body_content(body_content):
    # Parse html body
    soup = BeautifulSoup(body_content, "html.parser")

    # Extract each script or style from the soup
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Each content on new line
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


# Batch/Split them in chunks with a certain max lengh. Example: if "Hello Saugat" and max length is 2, the result is ["He", "ll", "o ", "Sa", "ug", "at"]
def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
