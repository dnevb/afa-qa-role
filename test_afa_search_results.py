import pytest
from playwright.sync_api import Page


@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
  page.goto('https://google.com')
  page.wait_for_load_state('domcontentloaded')

  input = page.query_selector('input[name="q"]')
  input.fill('Aid for Aids')

  btn = page.query_selector('input[name="btnK"]')
  btn.click()

  page.wait_for_load_state('domcontentloaded')


@pytest.fixture
def afa_nodes(page:Page):
  return page.query_selector_all('a[href*="aidforaids.org"]')

def test_validate_results_number(afa_nodes):
  assert len(afa_nodes) > 0

def test_validate_links(page: Page):
  pass