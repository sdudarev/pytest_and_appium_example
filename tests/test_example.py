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

