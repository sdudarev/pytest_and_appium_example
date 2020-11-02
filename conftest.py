import os

import pytest

from appium import webdriver

desired_caps = dict(
    platformName='Android',
    platformVersion='8',
    deviceName='Android Emulator',
    appWaitActivity='ru.europlan.*',
    app=os.path.abspath(os.path.join(__file__, '..', 'ru.europlan.lkk.apk'))
)

desired_win = dict(
    platformName='Android',
    platformVersion='8',
    deviceName='Android Emulator',
    appWaitActivity='ru.internetinvestments.*',
    app=os.path.abspath(os.path.join(__file__, '..', 'Winner.Stage_base.apk'))
)


@pytest.fixture()
def android_driver():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()


@pytest.fixture()
def android_winner():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_win)
    yield driver
    driver.quit()
