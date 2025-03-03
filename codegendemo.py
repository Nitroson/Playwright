from playwright.sync_api import Page, expect

def test_inventory_site(page: Page):
    # Go to the login page
    page.goto("https://www.saucedemo.com/")

    # Fill in login details
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")

    # Click the login button
    page.locator('[data-test="login-button"]').click()

    # Verify that the user is redirected to the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
