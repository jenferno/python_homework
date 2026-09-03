# Task 6: Scraping Structured Data

import os
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Anchor the output path to this script's own directory (assignment8),
# so owasp_top_10.csv is always written there regardless of the
# directory the script is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "owasp_top_10.csv")


# --- Step 1/2: Use Selenium to read the target page ---
# NOTE: The original assignment page,
# https://owasp.org/www-project-top-ten/, no longer lists the ten
# vulnerabilities directly. It now links out to the current OWASP
# Top 10 edition page instead. We navigate straight to that current
# page, https://owasp.org/Top10/2025/, since that is where the
# ordered list of the ten vulnerabilities actually lives.
# (See challenges.txt for more detail on this page-structure change.)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("https://owasp.org/Top10/2025/")

# --- Step 3: Find each of the top 10 vulnerabilities ---
# Locate the "Top 10:2025" heading element by its id, then use XPath
# to move from that heading to the ordered list (<ol>) that
# immediately follows it and contains the ten vulnerability links.
top_ten_heading = driver.find_element(
    By.CSS_SELECTOR,
    '[id="top-102025-list"]'
)

top_ten_list = top_ten_heading.find_element(
    By.XPATH,
    "following-sibling::ol[1]"
)

# Each vulnerability is an <a> link inside a top-level <li> of the
# ordered list. For each one, keep the title and href link in a
# dict, and accumulate these dicts in a list.
vulnerability_links = top_ten_list.find_elements(
    By.XPATH,
    "./li/a"
)

vulnerabilities = []

for link in vulnerability_links:
    title = link.text
    href = link.get_attribute("href")

    vulnerability = {
        "Title": title,
        "Link": href
    }

    vulnerabilities.append(vulnerability)

# --- Step 4: Print the list, then write it to a CSV file ---
print(vulnerabilities)

driver.quit()

with open(
    OUTPUT_PATH,
    "w",
    newline=""
) as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["Title", "Link"])

    for vulnerability in vulnerabilities:
        writer.writerow([
            vulnerability["Title"],
            vulnerability["Link"]
        ])

print(f"\nowasp_top_10.csv created successfully at: {OUTPUT_PATH}")