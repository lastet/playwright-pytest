from playwright.sync_api import Page, expect
import pytest


def test_text_check(page: Page):
    page.goto("https://www.hhs.gov/")
    pull_right = page.locator('[class="site-name pull-right"]')
    assert pull_right.inner_text() == 'U.S. Department of Health & Human Services'


    find_vaccine_btn = page.locator("//div[@class='field field--name-field-uswds-button field--type-link field--label-hidden field--item']//a[text()='Find a Vaccine']")
    expect(find_vaccine_btn).to_be_visible()

    nav_btn = page.locator("//div[@class='region region-navigation']")
    expect(nav_btn).to_be_visible()

    nav_btn_about = page.locator("//div[@class='region region-navigation']//a[@class='menu-item nav-about-hhs']")
    expect(nav_btn_about).to_be_visible()

    nav_btn_services = page.locator("//div[@class='region region-navigation']//a[@class='menu-item nav-programs-services']")
    expect(nav_btn_services).to_be_visible()

    nav_btn_grants = page.locator("//div[@class='region region-navigation']//a[@class='menu-item nav-grants-contracts']")
    expect(nav_btn_grants).to_be_visible()

    nav_btn_laws = page.locator("//div[@class='region region-navigation']//a[@class='menu-item nav-laws-regulations']")
    expect(nav_btn_laws).to_be_visible()

    main_block = page.locator("//div[@class='field field--name-field-uswds-title field--type-string field--label-hidden field--item']")
    expect(main_block).to_be_visible()

    second_block = page.locator("//div[@class='contextual-links-region homepage-featured-content pane-node panel-pane']")
    expect(second_block).to_be_visible()

    third_block = page.locator("//div[@class='panels-flexible-row clearfix row']//div[@class='homepage-priorities-content']")
    expect(third_block).to_be_visible()

    agencies_block = page.locator("//div[@class='paragraph paragraph--type--uswds-text paragraph--view-mode--default usa-section--background-dark-blue']")
    expect(agencies_block).to_be_visible()

    promo_block = page.locator("//div[@class='paragraph paragraph--type--uswds-text paragraph--view-mode--default']//div[@class='grid']")
    expect(promo_block).to_be_visible()

    bottom_block = page.locator("//div[@class='hhs-global-footer clear-both']")
    expect(bottom_block).to_be_visible()



    search_box = page.locator('[class="global-search"]')
    expect(search_box).to_be_visible()
    search_box.fill("aa2222")
    page.click('[type="submit"]')

    expect(page.locator('[class="max-width-css noResults"]')).to_be_visible()

    search_box_btn = page.locator("[title='Search Text']")
    expect(search_box_btn).to_be_visible()
    login_btn = page.locator('[class="footer-email-signup-btn"]')
    expect(login_btn).to_be_visible()


    page.pause()
    login_btn.click()




    page.close();





   #pytest --headed
