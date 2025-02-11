from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def setup_driver():
    service = Service()  # Replace with actual path
    driver = webdriver.Chrome(service=service)
    return driver


def get_active_words(driver):
    """Get currently visible words that haven't been typed yet"""
    try:
        # Find all word elements
        word_elements = driver.find_elements(By.CLASS_NAME, "word")

        # Filter for active (upcoming) words
        active_words = []
        for element in word_elements:
            # Skip words that have already been typed
            if "typed" not in element.get_attribute("class"):
                active_words.append(element.text)

        return active_words
    except Exception as e:
        print("Error getting words:", e)
        return []


def type_words_continuously(driver, wpm=60):
    # Calculate base delay between keystrokes
    delay = 60 / (wpm * 5)
    # Wait for the page to be fully loaded and ready
    time.sleep(2)

    # Create ActionChains object
    actions = ActionChains(driver)

    # Click on the typing area to focus it
    actions.click().perform()

    # Keep track of typed words to avoid duplicates
    typed_word_count = 0

    flag = False

    try:
        while True:  # Continue until test ends or interrupted
            # Get current batch of words
            active_words = get_active_words(driver)

            if not flag:
                flag = True
                actions.send_keys(active_words[0][0])
                actions.perform()

            # If we have words to type
            if active_words:
                for word in active_words:
                    # Type each character in the word
                    for char in word:
                        actions.send_keys(char)
                        actions.perform()
                        # Add slight random variation to typing speed
                        time.sleep(delay * random.uniform(0.8, 1.2))

                    # Add space after word
                    actions.send_keys(Keys.SPACE)
                    actions.perform()
                    time.sleep(delay * random.uniform(1.0, 1.5))

                    typed_word_count += 1

            # Brief pause to allow new words to load
            time.sleep(delay)

    except KeyboardInterrupt:
        print(f"\nStopped typing. Typed {typed_word_count} words.")
    except Exception as e:
        print(f"Error during typing: {e}")


def by_pass_cookies(driver):
    try:
        # Wait for cookie consent popup using a more generic approach
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "acceptAll"))
        )

        # Find the accept button - trying multiple possible selectors
        accept_button = None
        possible_selectors = [
            (By.ID, "accept"),
            (By.CLASS_NAME, "acceptAll"),
            (By.XPATH, "//button[contains(text(), 'Accept')]"),
            (By.XPATH, "//div[contains(@class, 'active acceptAll')]//button"),
            (By.XPATH, "//*[contains(text(), 'Accept') or contains(text(), 'accept')]")
        ]

        for by, selector in possible_selectors:
            try:
                accept_button = driver.find_element(by, selector)
                if accept_button and accept_button.is_displayed():
                    break
            except:
                continue

        if accept_button:
            # Use JavaScript click as a fallback if regular click doesn't work
            try:
                accept_button.click()
            except:
                driver.execute_script("arguments[0].click();", accept_button)
            print("Cookie popup handled successfully")
        else:
            print("Could not find cookie accept button")

    except Exception as e:
        print(f"Error handling cookie popup: {e}")
        # Print the page source to debug
        print("\nPage source:")
        print(driver.page_source[:1000])  # Print first 1000 chars of page source


def main():
    driver = setup_driver()
    try:
        driver.get("https://monkeytype.com")
        print("Starting typing test... Press Ctrl+C to stop.")
        # Wait for the words container to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "words"))
        )
        by_pass_cookies(driver)
        type_words_continuously(driver, wpm=100)  # Adjust WPM as needed
    finally:
        driver.quit()


if __name__ == "__main__":
    main()