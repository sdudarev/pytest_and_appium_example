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


@pytest.fixture()
def android_driver():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()
