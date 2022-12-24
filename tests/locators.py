from selenium.webdriver.common.by import By


class GoogleSearchLocators:
    GOOGLE_SEARCH_FIELD = (By.NAME, 'q')
    GOOGLE_SEARCH_RESULTS = (By.XPATH, '//*[@data-sokoban-container]/div/div/a[1]')  # selects only main links,
    # without google_translate and etc.


class ScoresLocators:
    MAIN_TITLE_LOGO = (By.CLASS_NAME, 'logo-container')
    ALL_SCORES_WIDGET = (By.XPATH, '//*[starts-with(@class,"competitor-container_container")]')
    GAME_CARD_LINKS = (By.XPATH, '//*[starts-with(@class,"game-card_game_card_link")]')

