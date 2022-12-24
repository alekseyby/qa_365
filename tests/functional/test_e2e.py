import pytest
import allure
from tests.pages.page import GoogleSearchPage
from tests.locators import ScoresLocators


@allure.title("Test: search site on google, navigate exist links and verify site title")
@allure.description(""" Test checks how many site links found by the search phrase on the first google page 
                    then navigates by links and check title logo and sport results exists on page """)
@pytest.mark.e2e_test
@pytest.mark.parametrize(('search_phrase', 'site_link_matcher'), [('365 Livescore in israel', '365score')])
def test_search_phrase_and_check_site_by_links(browser, search_phrase, site_link_matcher):
    user_page = GoogleSearchPage(browser)
    with allure.step('User navigates to google.com'):
        user_page.go_to_site()
    with allure.step(f'User search phrase: {search_phrase}'):
        user_page.perform_search(search_phrase)
    links = user_page.get_links_from_search_results()
    with allure.step(f'Check search result contains sites matches with {site_link_matcher}'):
        related_links = [link for link in links if site_link_matcher in link]
    with allure.step('Check found links count'):
        assert len(related_links) >= 2
    for link in related_links:
        with allure.step(f'Navigate to {link}'):
            user_page.go_to_site(link)
            with allure.step(f'Verify main logo, scores results visible on page'):
                user_page.check_element_is_displayed(ScoresLocators.MAIN_TITLE_LOGO)
                user_page.check_element_is_displayed(ScoresLocators.ALL_SCORES_WIDGET)
                score_results = user_page.find_elements(ScoresLocators.GAME_CARD_LINKS)
                assert len(score_results) > 0
