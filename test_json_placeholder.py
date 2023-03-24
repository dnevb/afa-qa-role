from random import randint

import pytest
from playwright.sync_api import APIRequestContext, Playwright

base_url = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='session')
def req_ctx(playwright: Playwright):
  req_ctx = playwright.request.new_context(base_url=base_url)
  yield req_ctx
  req_ctx.dispose()

@pytest.fixture(scope='session')
def user(req_ctx: APIRequestContext):
  user_id = randint(1,10)
  item = req_ctx.get(f'/users/{user_id}').json()
  print('User email: ', item['email'])
  return item

def test_valid_user_posts(req_ctx: APIRequestContext, user):
  userid = user['id']
  res = req_ctx.get(f'/posts?userId={userid}')
  items = res.json()

  for post in items:
    assert post['id'] >= 1 and post['id'] <= 100

def test_valid_post_creation(req_ctx: APIRequestContext, user):
  userid = user['id']
  payload = {
    'userId': userid,
    'title': 'lorem title',
    'body': 'lorem body'
  }
  res = req_ctx.post('/posts', data=payload)
  assert res.status == 201