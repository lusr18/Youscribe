from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from youtube_transcript import youtube_to_transcript

def parse_query(query):
    print("Parsing query.")
    # Find search bar, input and search for query
    search_bar = driver.find_element(By.NAME, "search_query")
    search_bar.clear()
    search_bar.send_keys(query)
    time.sleep(1)
    search_bar.send_keys(Keys.RETURN)

    # Wait for searched page to load
    time.sleep(2)
    print("Queried search url: ", driver.current_url)

    # Locate the video elements and extract URLs
    video_elements = driver.find_elements(By.ID, "video-title")
    for video in video_elements:
        if video.get_attribute('href') is not None:
            title = video.get_attribute('title')
            url = video.get_attribute('href')
            if "shorts" not in url:
                print("Creating transcript for: " + title + " " + url)
                youtube_to_transcript(title, url)

if __name__ == "__main__":
    # Launch Firefox, open YouTube and wait for page to load
    driver = webdriver.Firefox()
    driver.get("https://www.youtube.com")
    time.sleep(1)

    # While loop to search key word/phrase
    while(1):
        print("\nInput new query:")
        query = input()
        print("Query received, parsing for urls.")
        video_urls = parse_query(query)        

    # Close driver
    driver.close()