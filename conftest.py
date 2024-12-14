import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.webdriver import Options
from utils.config import load_config
import datetime

def get_driver():
    """
    Initialize and return a WebDriver instance based on the browser specified in the config.
    """
    config = load_config()

    # Determine the browser to use
    browser = config.get("browser", "chrome").lower()

    # Initialize the driver based on the selected browser
    if browser == "chrome":
        driver_path = os.path.abspath(config["chrome_driver_path"])
        service = ChromeService(executable_path=driver_path)
        options = Options()
        # options.add_argument("--headless")  # Optional: Run in headless mode
        # options.add_argument("--disable-gpu")  # Optional: Disable GPU
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver_path = os.path.abspath(config["gecko_driver_path"])
        service = FirefoxService(executable_path=driver_path)
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError("Unsupported browser specified in the config!")

    driver.maximize_window()
    return driver

@pytest.fixture
def setup(request):
    """
    Pytest fixture to initialize the WebDriver using the get_driver function.
    Ensures the WebDriver is properly closed after the test.
    Captures screenshots on test failure.
    """
    driver = get_driver()  # Use the get_driver function to initialize the driver
    yield driver  # Provide the driver instance to the test

    # Capture screenshot on failure
    if request.node.rep_call.failed:
        # Create a screenshots directory if it doesn't exist
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        # Generate a unique screenshot name
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{request.node.name}_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)

        # Save the screenshot
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    driver.quit()  # Ensure the driver is closed after the test

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook for capturing the test result status.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
