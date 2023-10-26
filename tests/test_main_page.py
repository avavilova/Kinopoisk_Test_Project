import pytest

from pages import *

@pytest.fixture(scope='module')
def main_page(kinopoisk_main_page):
    kinopoisk_main_page: MainPage
    kinopoisk_main_page.go_to_site()
    yield kinopoisk_main_page

def test_search_default_suggestion_list_is_not_empty(main_page):
    assert main_page.get_default_suggested_search_results()

def test_search_default_suggestion_has_top10_label(main_page):
    assert main_page.is_default_suggested_search_top10_label_exist()

def test_search_returns_results(main_page):
    assert main_page.get_search_results("мой")


