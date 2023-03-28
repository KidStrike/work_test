from robot.libraries.BuiltIn import BuiltIn
from playwright.sync_api import sync_playwright


def test_open_page():
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(headless=False)
            browser_type = "chromium"
        except:
            try:
                browser = playwright.firefox.launch(headless=False)
                browser_type = "firefox"
            except:
                browser = playwright.webkit.launch(headless=False)
                browser_type = "webkit"
        with browser.new_context() as context:
            page = context.new_page()
            response = page.goto("https://www.multitude.com/")
            status = response.status
            # Check if HTTP status is equal to 200
            assert status == 200
            page.wait_for_selector("body")
            text = page.inner_text("body")
            # Check for present text
            assert "Multitude" in text
            page.close()
        browser.close()

    print(f"Test executed in {browser_type} browser.")


if __name__ == "__main__":
    robot = BuiltIn()
    robot.run_keyword("test_open_page")
