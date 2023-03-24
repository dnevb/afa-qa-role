from random import randint

import pytest
from playwright.sync_api import ElementHandle, Page, Playwright


@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
  page.goto('https://google.com')
  page.wait_for_load_state('domcontentloaded')

  input = page.query_selector('input[name="q"]')
  page.wait_for_timeout(100)
  input.fill('Aid for Aids')

  btn = page.query_selector('input[name="btnK"]')
  btn.click()

  page.wait_for_load_state('domcontentloaded')


@pytest.fixture
def afa_nodes(page:Page):
  return page.query_selector_all('a[href^="https://aidforaids.org"]')

def test_validate_results_number(afa_nodes):
  assert len(afa_nodes) > 0

def test_validate_links(
  afa_nodes: list[ElementHandle], 
  playwright: Playwright
):
  browser = playwright.chromium.launch()
  for node in afa_nodes:
    url = node.get_attribute('href')
    assert url != None

    ctx = browser.new_context()
    ctx.set_default_timeout(60000)

    page = ctx.new_page()
    page.goto(url)
    page.wait_for_load_state('networkidle', timeout=None)

    assert page.title() != None

    menu_items = page.query_selector_all('#primary-menu > li > a[href^=https]')
    item = menu_items[randint(0, len(menu_items) - 1)]

    item_link = item.get_attribute('href')
    assert item_link != None

    res = page.goto(item_link)
    page.wait_for_load_state('networkidle')

    assert res.status < 300

    page.screenshot(path=f'tmp/{page.title()}.png')

    ctx.close()
  browser.close()