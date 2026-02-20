from playwright.sync_api import sync_playwright
import time

def get_stockx_price(url:str, size:str, region:str="en.US"):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
            
        context = browser.new_context( locale=region)

        page = context.new_page()
        
        page.goto(url, timeout=60000)

        page.evaluate("document.body.style.zoom = '0.7'")

        page.locator("#onetrust-accept-btn-handler").click(timeout=5000)
        
        page.locator("#menu-button-pdp-size-selector").click(timeout=5000)

        row = page.get_by_role("menuitemradio", name=f"EU {size} €")
        
        price = row.locator('[data-testid="selector-secondary-label"]').inner_text()
        labels = page.locator('[data-testid="selector-secondary-label"]').all_inner_texts()
        
        browser.close()

        return price

