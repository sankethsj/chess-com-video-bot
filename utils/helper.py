from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(browser, username:str, password:str):
    """ function to login to chess.com account 
    and close ad-banner (modal) if exists
    browser : instance of chrome browser
    username (str) : accepts chess.com username
    password (str) : accepts chess.com password
    """
    print(f"Logging to chess.com as user : {username}")

    username_input = browser.find_element(By.ID, "username")
    username_input.clear()
    username_input.send_keys(username)

    password_input = browser.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    try:
        modal = browser.find_element(By.XPATH, '//div[contains(@class,"modal")]')
        modal_close_btn = browser.find_element(By.XPATH, '//button[contains(@class,"modal-close")]')
        modal_close_btn.click()
    except Exception as e:
        print("Modal not found.", e)

    return True


def get_game_link(browser):
    """ function to get the latest game link from the games archive
    """
    games = browser.find_elements(By.XPATH, '//a[@class="archived-games-background-link"]')
    game_links = []
    for game in games:
        game_link = game.get_attribute('href')
        game_links.append(game_link)
    game_links = list(set(game_links))

    game_numbers = [game.split("/")[-1] for game in game_links]
    game_numbers = sorted(list(set(game_numbers)), reverse=True)

    game_number = game_numbers[0]
    current_game_link = f"https://www.chess.com/analysis/game/live/{game_number}?tab=analysis"
    return game_number, current_game_link
