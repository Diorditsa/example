



class CalculationPage():
    def __init__(self):
        pass
    goals_card = {
        "selector": "//mat-card[contains(.,'Совмещение целей')]",
        "type_selector": "by_xpath"
    }

    add_goal = {
        "selector": ".btn-plus",
        "type_selector": "by_css"
    }
    name_new_goal = {
        "selector": "//input[@id='mat-input-6']",
        "type_selector": "by_xpath"
    }

    save_goal = {
        "selector": "//button[contains(.,'Сохранить')]",
        "type_selector": "by_xpath"
    }

    goals_row_instance = {
        "selector": "//table[@class='mat-table cdk-table goal-main-table']/tbody[@role='rowgroup']/tr[@class='mat-row cdk-row ng-star-inserted']",
        "type_selector": "by_xpath"
    }
    name_instance_row =  {
        "selector": "//tbody[@role='rowgroup']//tr[@class='mat-row cdk-row ng-star-inserted']//td[1]",
        "type_selector": "by_xpath"
    }
    goals_row_instance2 = {
        "selector": "//tbody[@role='rowgroup']/tr[@class='mat-row cdk-row ng-star-inserted']",
        "type_selector": "by_xpath"
    }
    name_instance_row2 = {
        "selector": "//tr[@class='mat-row cdk-row ng-star-inserted']/td[1]",
        "type_selector": "by_xpath"
    }
    every_mounts_investments = {
        "selector": "//p[contains(.,'Ежемесячные инвестиции')]",
        "type_selector": "by_xpath"
    }
    goals_row_instance_on_mounts_invest = {
        "selector": "//table[@class='table table-bordered']/tbody[@class='bg-white']/tr[@class='ng-star-inserted']",
        "type_selector": "by_xpath"
    }
    name_instance_row_on_mount_invest = {
        "selector": "//table[@class='table table-bordered']/tbody[@class='bg-white']/tr[@class='ng-star-inserted']/td[@class='text-left td-goals']",
        "type_selector": "by_xpath"
    }
