#quick script to refresh your search appearence on dice.com
#input fields email and password to be modified for correct run

from playwright.sync_api import Page, expect
import pytest


def test_Dice_update(page: Page):
    page.goto("https://www.dice.com/")


    login_dropdown = page.locator('#navbarDropdown-10').click()
    login_button = page.locator('//a[@href="/dashboard/login"]').click()


    email =  page.locator('#email').fill('ur_email')
    password = page.locator('#password').fill('ur_password')


    sign_in_btn = page.locator('//div[@class="col-sm-8 col-md-8 col-lg-8"]//button[@class="btn btn-primary btn-lg btn-block"]')

    expect(sign_in_btn).to_be_visible()
    sign_in_btn.click()

    profile_toggle = page.locator('#dice-login-customer-name').click()

    profile_btn = page.locator('//ul[@class="dropdown-menu dropdown-smartMenu slideUp"]//a[@href="/dashboard"]').click()


    page.close()
    
    
