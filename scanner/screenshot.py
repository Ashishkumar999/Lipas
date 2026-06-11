import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def take_screenshot(target):

    print("\n[+] Capturing Screenshot...")

    if not target.startswith("http"):
        target = "https://" + target

    os.makedirs(
        "reports/screenshots",
        exist_ok=True
    )

    filename = (
        target.replace("https://", "")
              .replace("http://", "")
              .replace("/", "_")
    )

    screenshot_file = (
        f"reports/screenshots/{filename}.png"
    )

    options = Options()

    options.add_argument("--headless")

    driver = webdriver.Firefox(
        options=options
    )

    driver.set_window_size(
        1920,
        1080
    )

    driver.get(target)

    driver.save_screenshot(
        screenshot_file
    )

    driver.quit()

    print(
        f"[+] Screenshot Saved: {screenshot_file}"
    )
