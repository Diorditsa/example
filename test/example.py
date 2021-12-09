import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import allure
from allure import severity, severity_level
from page_objects import login_page
from page_objects import main
from page_objects import calculations_tab


@severity(severity_level.NORMAL)
@allure.feature("User can add new goal")
@allure.description("When user add new goal, then he can see them in schedule")
def test_example(selenium_facade):
    act = selenium_facade
    page_login = login_page.LoginPage()
    page_main = main.MainPage()
    page_calculations = calculations_tab.CalculationPage()
    # user data
    user_email = 'stuffy.user.0101@gmail.com'
    user_password = 'TUnke3RW4gm4YM8'
    new_goal_name = "Бэт мобиль"
    with allure.step("Open url (website)"):
        act.go_to_url('https://dev.invest-ra.ru')
    with allure.step("Enter user data and login"):
        act.tap_element(page_login.log_in_button)
        act.send_keys(page_login.email_field, user_email)
        act.send_keys(page_login.password_field, user_password)
        act.tap_element(page_login.entrance_next_button)
    with allure.step("open tab 'Калькуляторы'"):
        act.tap_element(page_main.calculations)
        act.tap_element(page_main.goals_card)
    with allure.step("Set goals number before add new goal"):
        goals_number = len(act.get_elements(page_calculations.goals_row_instance))
        allure.attach(act.get_screen_shot())
        allure.attach(act.get_element_image(page_calculations.goals_row_instance))
    with allure.step(f"Add new goal and gave them name:{new_goal_name}, then tap 'save' button"):
        act.tap_element(page_calculations.add_goal)
        act.clear_input(page_calculations.name_new_goal)
        act.send_keys(page_calculations.name_new_goal, new_goal_name)
        act.tap_element(page_calculations.save_goal)
        allure.attach(act.get_screen_shot())
    with allure.step(f"Chek what new goal wad added to schedule and her name:{new_goal_name}"):
        act.key_down(7)
        allure.attach(act.get_screen_shot())
    with allure.step("Set goals number after add new goal, and check conditions what new goal add and have our name"):
        new_goals_number = len(act.get_elements(page_calculations.goals_row_instance))
        allure.attach(act.get_element_image(page_calculations.goals_row_instance))
        allure.attach(act.get_screen_shot())
        print(f"{goals_number}, {new_goals_number}")
        if new_goals_number != goals_number + 1:
            raise AssertionError("Seems like new goal doesn't add to schedule")
        name_created_goal = act.get_elements(page_calculations.name_instance_row)[-1].text
        allure.attach(act.get_elements(page_calculations.name_instance_row)[-1].screenshot_as_png)
        if name_created_goal != new_goal_name:
            allure.attach(f"entered name:{name_created_goal}, current goal name:{new_goal_name}")
            raise AssertionError("Goal name doesn't mach with entered name")
    with allure.step("Check every month invest tab, what them too have new goal in schedule"):
        act.tap_element(page_calculations.every_mounts_investments)
        act.wait_visible_of_element(page_calculations.goals_row_instance_on_mounts_invest)
        # print(act.get_elements(page_calculations.name_instance_row_on_mount_invest)[-1].text)
        if name_created_goal != act.get_elements(page_calculations.name_instance_row_on_mount_invest)[-1].text:
            allure.attach(act.get_screen_shot())
            raise AssertionError("I can't find new goal in goals page")