class TestExamples:

    def test_example(self, android_driver):
        android_driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys('123')
        password = android_driver.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('123')
        android_driver.back()
        android_driver.implicitly_wait(5)
        android_driver.find_element_by_class_name('android.widget.Button').click()
        test = android_driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                    '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                    '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                    '/android.widget.LinearLayout[1]/android.widget.LinearLayout'
                                                    '/android.widget.LinearLayout/android.widget.LinearLayout'
                                                    '/android.widget.TextView').text
        assert test == 'Задайте код доступа'

    def test_example_2(self, android_driver):
        android_driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys('test_!')
        password = android_driver.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('123')
        android_driver.back()
        android_driver.implicitly_wait(5)
        android_driver.find_element_by_class_name('android.widget.Button').click()
        toast = android_driver.find_element_by_xpath('//android.widget.Toast[1]').text

        assert toast == '"Неверное имя или пароль"'

    def test_example_3(self, android_driver):
        android_driver.find_element_by_class_name('android.widget.Button').click()
        err_texts = android_driver.find_elements_by_id('ru.europlan.lkk:id/textinput_error')

        assert err_texts[0].text == 'Введите имя пользователя'
        assert err_texts[1].text == 'Введите пароль'

    def test_example_4(self, android_driver):
        android_driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                             '.widget.FrameLayout/android.view.ViewGroup/android.widget'
                                             '.LinearLayout/android.widget.Button[2]').click()

        android_driver.implicitly_wait(3)

    def test_winner_1(self, android_winner):
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.Button').click()
        test = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                                    '/android.widget.TextView[2]').text
        test_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.view'
                                                      '.ViewGroup/android.widget.TextView[3]').text
        assert test == 'Задайте код доступа'
        assert test_2 == 'Повторите код доступа'

        android_winner.find_element_by_class_name('android.widget.Button')[7].click()

        test_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/android.widget.TextView[2]').text
        assert test_3 == 'Личный кабинет'
