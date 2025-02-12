# CheetahType - Auto Typing Bot

CheetahType is a Python script that automates typing on typing speed test websites like [monkeytype.com](https://monkeytype.com). It bypasses cookie popups and simulates keystrokes to achieve a user-specified words-per-minute (WPM) speed. Built using Selenium, this script provides an easy way to test high-speed typing.

## Features
- **Bypasses Cookie Popups:** Automatically handles cookie consent dialogs to allow uninterrupted typing.
- **Customizable Typing Speed:** Adjust the WPM setting to simulate different typing speeds.
- **Realistic Typing Simulation:** Adds slight random variations to keystroke delays to mimic human typing.
- **Auto-Focus on Typing Area:** Ensures the cursor is placed in the correct input field before starting.
- **Error Handling:** Gracefully handles errors and interruptions.

## Requirements
Ensure you have the following installed before running the script:
- Python 3.x
- Google Chrome (latest version)
- Chrome WebDriver (compatible with your Chrome version)
- Selenium library

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/shay-ff/CheetahType.git
   cd CheetahType
   ```
2. Install dependencies:
   ```bash
   pip install selenium
   ```
3. Download and set up Chrome WebDriver:
   - Get the correct version of ChromeDriver from [here](https://chromedriver.chromium.org/downloads).
   - Place it in a directory and update the `setup_driver()` function in `main.py` to include its path.

## Usage
Run the script with:
```bash
python main.py
```

By default, the script starts typing at **200 WPM**. You can modify this by editing the `wpm` argument in `type_words_continuously()` inside `main.py`.

### Adjusting WPM
To change the typing speed, update the function call:
```python
type_words_continuously(driver, wpm=100)  # Adjust speed as needed
```

## Build Methods
The script includes the following key methods:
- **setup_driver()** → Initializes and configures the Selenium WebDriver.
- **get_active_words(driver)** → Retrieves the list of words that need to be typed.
- **type_words_continuously(driver, wpm)** → Simulates keystrokes at the specified WPM.
- **by_pass_cookies(driver)** → Handles and dismisses cookie popups.
- **main()** → Orchestrates the entire automation process.

## Future Enhancements
- Add support for **time-based** and **word-count-based** typing tests.
- Implement support for more websites.
- Improve the keystroke simulation for more human-like typing.

## Disclaimer
This script is created for **educational and fun purposes**. Use it responsibly and ensure it complies with the terms of use of the websites you run it on.

## License
This project is open-source and licensed under the MIT License.

