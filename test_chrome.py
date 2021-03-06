from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import TakeScreenshotConditionType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Ran's Project
    Package: TestProject.Generated.Tests.RansProject
    Test: Python Test Check
    Generated by: Ran Tzur (ran.tzur@testproject.io)
    Generated on 04/07/2021, 08:05:57
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="kJCeheoppFyo8uaZ17k0JQyBck1qLIf5ZrynbI6t7Fk1",
                              project_name="Ran's Project",
                              job_name="Python Test Check")
    step_settings = StepSettings(timeout=15000, screenshot_condition=TakeScreenshotConditionType.Failure)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://www.airbnb.com"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'query'
    query = driver.find_element(By.CSS_SELECTOR,
                                "#bigsearch-query-detached-query")
    query.click()

    # 3. Type 'Hawaii' in 'query'
    query = driver.find_element(By.CSS_SELECTOR,
                                "#bigsearch-query-detached-query")
    query.send_keys("Hawaii")

    # 4. Click 'DIV'
    div = driver.find_element(By.XPATH,
                              "//form/div/div/div[3]/div[1]/div/div")
    div.click()

    # 5. Click '20'
    _20 = driver.find_element(By.XPATH,
                              "//td[3]/div/div[. = '20']")
    _20.click()

    # 6. Click '23'
    _23 = driver.find_element(By.XPATH,
                              "//td[6]/div/div[. = '23']")
    _23.click()

    # 7. Click 'DIV1'
    div1 = driver.find_element(By.XPATH,
                               "//form/div/div/div[5]/div/div")
    div1.click()

    # 8. Click 'svg'
    svg = driver.find_element(By.XPATH,
                              "//div[1]/div[2]/button[2]//*[name()='svg']")
    svg.click()

    # 9. Click 'svg1'
    svg1 = driver.find_element(By.XPATH,
                               "//div[1]/div[2]/button[2]//*[name()='svg']")
    svg1.click()

    # 10. Click 'SPAN'
    span = driver.find_element(By.XPATH,
                               "//button/span/span")
    span.click()

    # 11. Get text from 'Stays in Hawaii'
    stays_in_hawaii = driver.find_element(By.XPATH,
                                          "//h1[. = 'Stays in Hawaii']")
    step_output = stays_in_hawaii.text
    assert "Hawaii" in step_output
