from playwright.sync_api import Page, expect
import pytest


def test_text_check(page: Page):
    page.goto("https://www.hhs.gov/")
    pull_right = page.locator('[class="site-name pull-right"]')
    assert pull_right.inner_text() == 'U.S. Department of Health & Human Services'

    search_box = page.locator('[class="global-search"]')
    expect(search_box).to_be_visible()
    search_box.fill("aa2222")
    page.click('[type="submit"]')

    expect(page.locator('[class="max-width-css noResults"]')).to_be_visible()

    search_box_btn = page.locator("[title='Search Text']")
    expect(search_box_btn).to_be_visible()
    login_btn = page.locator('[class="footer-email-signup-btn"]')
    expect(login_btn).to_be_visible()

    login_btn.click()




    page.close();





   #pytest --headed