from playwright.sync_api import sync_playwright

def extract_full_body_html(from_url, wait_for=None):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(from_url)

        # page.wait_for_selector('div.some_class')
        page.wait_for_load_state('networkidle')
        page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
        page.wait_for_load_state('domcontentloaded')
        if wait_for:
            page.wait_for_selector(wait_for)

        # page.screenshot(path='steam3.png', full_page=True)

        html = page.inner_html('body')
        return html
