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

    def test_winner_1(self, android_winner):  # Проверяем Валидный логин и пароль без имперсонации
        android_winner.implicitly_wait(5)
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
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.view.ViewGroup/android.widget.Button').click()
        test_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/android.widget.TextView[2]').text
        test_4 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/android.widget.Button[2]').text
        assert test_3 == 'Личный кабинет'
        assert test_4 == 'ЗАБЫЛИ ПАРОЛЬ?'
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.RelativeLayout/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/android.widget.Button[2]').click()

    def test_winner_2(self, android_winner):  # Проверяем Валидный логин и пароль с имперсонацией
        android_winner.implicitly_wait(5)
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        android_winner.implicitly_wait(5)
        password_imper = android_winner.find_elements_by_class_name('android.widget.EditText')[2]
        password_imper.click()
        password_imper.send_keys('3492440')
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
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.view.ViewGroup/android.widget.Button').click()
        test_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/android.widget.TextView[2]').text
        assert test_3 == 'Личный кабинет'

    def test_winner_3(self, android_winner):  # Проверяем Возможность задать пароль после авторизации
        android_winner.implicitly_wait(5)
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        android_winner.implicitly_wait(5)
        password_imper = android_winner.find_elements_by_class_name('android.widget.EditText')[2]
        password_imper.click()
        password_imper.send_keys('3492440')
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
        android_winner.implicitly_wait(5)
        click_one = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.view'
                                                         '.ViewGroup/android.widget.LinearLayout['
                                                         '3]/android.view.ViewGroup[4]/android.widget.Button')
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        android_winner.implicitly_wait(5)
        test_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.view'
                                                      '.ViewGroup/androidx.viewpager.widget.ViewPager/android.view'
                                                      '.ViewGroup/android.widget.LinearLayout/android.widget.TextView[1]').text
        assert test_3 == 'Передавайте клиентов'
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.ImageView').click()
        test_4 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                      '.view.ViewGroup/android.widget.TextView').text
        android_winner.implicitly_wait(5)
        assert test_4 == 'Лента событий'

    def test_winner_4(self, android_winner):  # Открываем профиль
        android_winner.implicitly_wait(5)
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        android_winner.implicitly_wait(5)
        password_imper = android_winner.find_elements_by_class_name('android.widget.EditText')[2]
        password_imper.click()
        password_imper.send_keys('3492440')
        android_winner.back()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.Button').click()
        android_winner.implicitly_wait(5)
        click_one = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.view'
                                                         '.ViewGroup/android.widget.LinearLayout['
                                                         '3]/android.view.ViewGroup[4]/android.widget.Button')
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        android_winner.implicitly_wait(5)
        test_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.view'
                                                      '.ViewGroup/androidx.viewpager.widget.ViewPager/android.view'
                                                      '.ViewGroup/android.widget.LinearLayout/android.widget'
                                                      '.TextView[1]').text
        assert test_2 == 'Передавайте клиентов'
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.ImageView').click()
        android_winner.find_element_by_class_name('android.widget.ImageButton').click()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.LinearLayout').click()
        test_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                      '.view.ViewGroup/android.widget.TextView').text
        assert test_3 == 'Мой профиль'
        # android_winner.refresh()
        # сделать рефреш формы.

    def test_winner_5(self, android_winner):
        """Открываем редактирование профиля и выходим из режима редактирования без сохранения."""
        android_winner.implicitly_wait(5)
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        android_winner.implicitly_wait(5)
        password_imper = android_winner.find_elements_by_class_name('android.widget.EditText')[2]
        password_imper.click()
        password_imper.send_keys('3492440')
        android_winner.back()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.Button').click()
        android_winner.implicitly_wait(5)
        click_one = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.view'
                                                         '.ViewGroup/android.widget.LinearLayout['
                                                         '3]/android.view.ViewGroup[4]/android.widget.Button')
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        android_winner.implicitly_wait(5)
        test_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.view'
                                                      '.ViewGroup/androidx.viewpager.widget.ViewPager/android.view'
                                                      '.ViewGroup/android.widget.LinearLayout/android.widget'
                                                      '.TextView[1]').text
        assert test_2 == 'Передавайте клиентов'
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.ImageView').click()
        android_winner.find_element_by_class_name('android.widget.ImageButton').click()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.LinearLayout').click()
        android_winner.implicitly_wait(3)
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout'
                                             '.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                             '/android.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                             '.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android'
                                             '.widget.TextView').click()
        test_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                      '.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                                      '.ScrollView/android.widget.LinearLayout/android.view'
                                                      '.ViewGroup/android.widget.TextView[1]').text
        test_4 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                      '.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                                      '.ScrollView/android.widget.LinearLayout/android.view'
                                                      '.ViewGroup/android.widget.TextView[2]').text
        assert test_3 == 'Загрузить фото'
        assert test_4 == 'Отменить изменения'
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                             '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                             '.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                             '.ScrollView/android.widget.LinearLayout/android.view'
                                             '.ViewGroup/android.widget.TextView[2]').click()
        test_5 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                      '.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                                      '.ScrollView/android.widget.LinearLayout/android.view.ViewGroup'
                                                      '/android.widget.TextView').text
        assert test_5 == 'Изменить данные'

    def test_winner_6(self, android_winner):
        """Открываем редактирование профиля и выходим не вводя изменений с
        сохранением. Смотрим текст после сохранения и переходим в ленту событий"""
        android_winner.implicitly_wait(5)
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        android_winner.implicitly_wait(5)
        password_imper = android_winner.find_elements_by_class_name('android.widget.EditText')[2]
        password_imper.click()
        password_imper.send_keys('3492440')
        android_winner.back()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.Button').click()
        android_winner.implicitly_wait(5)
        click_one = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.view'
                                                         '.ViewGroup/android.widget.LinearLayout['
                                                         '3]/android.view.ViewGroup[4]/android.widget.Button')
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        android_winner.implicitly_wait(5)
        test = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.view'
                                                    '.ViewGroup/androidx.viewpager.widget.ViewPager/android.view'
                                                    '.ViewGroup/android.widget.LinearLayout/android.widget'
                                                    '.TextView[1]').text
        assert test == 'Передавайте клиентов'
        android_winner.find_element_by_class_name('android.widget.ImageView').click()
        android_winner.find_element_by_class_name('android.widget.ImageButton').click()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.LinearLayout').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout'
                                             '.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout'
                                             '/android.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                             '.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android'
                                             '.widget.TextView').click()
        android_winner.find_element_by_class_name('android.widget.Button').click()
        test_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                      '.view.ViewGroup/android.widget.TextView').text
        test_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                      '.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                                      '.TextView[1]').text
        test_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                      '.widget.RelativeLayout/android.view.ViewGroup/android.widget'
                                                      '.TextView[2]').text
        test_4 = android_winner.find_element_by_class_name('android.widget.Button').text
        assert test_1 == 'Мой профиль'
        assert test_2 == 'Ваша заявка на изменение персональных данных принята'
        assert test_3 == 'Мы свяжемся с вами в ближайшее время для подтверждения корректности данных.'
        assert test_4 == 'ПЕРЕЙТИ К ЛЕНТЕ СОБЫТИЙ'
        android_winner.find_element_by_class_name('android.widget.Button').click()
        test_5 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                      '.view.ViewGroup/android.widget.TextView').text
        assert test_5 == 'Лента событий'

    def test_winner_7(self, android_winner):
        """Проверяем в закладке "Кабинет" названия разделов и возможность их открыть."""
        android_winner.implicitly_wait(5)
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        password_imper = android_winner.find_elements_by_class_name('android.widget.EditText')[2]
        password_imper.click()
        password_imper.send_keys('3492440')
        android_winner.back()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.Button').click()
        android_winner.implicitly_wait(8)
        click_one = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.view'
                                                         '.ViewGroup/android.widget.LinearLayout['
                                                         '3]/android.view.ViewGroup[4]/android.widget.Button')
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        android_winner.implicitly_wait(3)
        test_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.view'
                                                      '.ViewGroup/androidx.viewpager.widget.ViewPager/android.view'
                                                      '.ViewGroup/android.widget.LinearLayout/android.widget'
                                                      '.TextView[1]').text
        assert test_2 == 'Передавайте клиентов'
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.ImageView').click()
        android_winner.implicitly_wait(8)
        android_winner.find_element_by_class_name('android.widget.ImageButton').click()
        test_3 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                      '@content-desc="Бонусы"]/android.widget.TextView').text
        test_4 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                      '@content-desc="Кабинет"]/android.widget.TextView').text
        test_5 = android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                                      "/android.widget.LinearLayout/androidx.viewpager.widget"
                                                      ".ViewPager/android.widget.ScrollView/android.widget"
                                                      ".LinearLayout/android.widget.ScrollView/android.widget"
                                                      ".LinearLayout/androidx.recyclerview.widget.RecyclerView"
                                                      "/android.widget.LinearLayout[1]/android.widget.TextView").text
        test_6 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                      '.ViewPager/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                                      '/android.widget.LinearLayout[2]/android.widget.TextView').text
        test_7 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                      '.ViewPager/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                                      '/android.widget.LinearLayout[3]/android.widget.TextView').text
        test_8 = android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                                      "/android.widget.LinearLayout/androidx.viewpager.widget"
                                                      ".ViewPager/android.widget.ScrollView/android.widget"
                                                      ".LinearLayout/android.widget.ScrollView/android.widget"
                                                      ".LinearLayout/androidx.recyclerview.widget.RecyclerView"
                                                      "/android.widget.LinearLayout[4]/android.widget.TextView").text
        test_9 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                      '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                      '.ViewPager/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/android.widget.ScrollView/android.widget'
                                                      '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                                      '/android.widget.LinearLayout[5]/android.widget.TextView').text
        test_10 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                       '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                       '.ViewPager/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                                       '/android.widget.LinearLayout[6]/android.widget.TextView').text
        test_11 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                       '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                       '.ViewPager/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                                       '/android.widget.LinearLayout[7]/android.widget.TextView').text
        test_12 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                       '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                       '.ViewPager/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.LinearLayout/android.widget.TextView').text
        assert test_3 == 'БОНУСЫ'
        assert test_4 == 'КАБИНЕТ'
        assert test_5 == 'Акции'
        assert test_6 == 'Лента событий'
        assert test_7 == 'Передать обращение'
        assert test_8 == 'Очередь обращений'
        assert test_9 == 'Мои проекты'
        assert test_10 == 'Премия'
        assert test_11 == 'Связаться с нами'
        assert test_12 == 'Выйти'
        android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                             ".LinearLayout/android.widget.FrameLayout/android.widget"
                                             ".LinearLayout/android.widget.FrameLayout/android.widget"
                                             ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                             "/android.widget.LinearLayout/androidx.viewpager.widget"
                                             ".ViewPager/android.widget.ScrollView/android.widget"
                                             ".LinearLayout/android.widget.ScrollView/android.widget"
                                             ".LinearLayout/androidx.recyclerview.widget.RecyclerView"
                                             "/android.widget.LinearLayout[1]/android.widget.TextView").click()
        test_5_1 = android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                                        ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                        ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                        ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                                        "/android.view.ViewGroup/android.widget.LinearLayout/android"
                                                        ".view.ViewGroup/android.widget.TextView").text
        test_5_2 = android_winner.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Все '
                                                        'акции"]/android.widget.TextView').text
        test_5_3 = android_winner.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Получен '
                                                        'приз"]/android.widget.TextView').text
        assert test_5_1 == 'Акции'
        assert test_5_2 == 'ВСЕ АКЦИИ'
        assert test_5_3 == 'ПОЛУЧЕН ПРИЗ'
        # android_winner.implicitly_wait(3)
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                             '2]/android.widget.TextView').click()
        test_6_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                        '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                        '.view.ViewGroup/android.widget.TextView').text
        assert test_6_1 == 'Лента событий'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                             '3]/android.widget.TextView').click()
        test_7_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                        '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                        '.view.ViewGroup/android.widget.TextView').text
        assert test_7_1 == 'Передать обращение'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                             '4]/android.widget.TextView').click()
        test_8_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                        '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                        '.view.ViewGroup/android.widget.TextView').text
        assert test_8_1 == 'Очередь обращений'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                             '/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                             '/android.widget.LinearLayout[5]/android.widget.TextView').click()
        test_9_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                        '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                        '.view.ViewGroup/android.widget.TextView').text
        test_9_2 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                        '@content-desc="Фильтр"]/android.widget.TextView').text
        assert test_9_1 == 'Мои проекты'
        assert test_9_2 == 'ФИЛЬТР'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                             '6]/android.widget.TextView').click()
        test_10_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                         '.view.ViewGroup/android.widget.TextView').text
        test_10_2 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                         '@content-desc="Месяц"]/android.widget.TextView').text
        test_10_3 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                         '@content-desc="Квартал"]/android.widget.TextView').text
        test_10_4 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                         '@content-desc="Год"]/android.widget.TextView').text
        test_10_5 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                         '@content-desc="Все"]/android.widget.TextView').text
        assert test_10_1 == 'Премия'
        assert test_10_2 == 'МЕСЯЦ'
        assert test_10_3 == 'КВАРТАЛ'
        assert test_10_4 == 'ГОД'
        assert test_10_5 == 'ВСЕ'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                             '7]/android.widget.TextView').click()
        test_11_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                         '.view.ViewGroup/android.widget.TextView').text
        assert test_11_1 == 'Связаться с нами'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                             '/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/android.widget.LinearLayout/android.widget.TextView').click()
        test_13 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.TextView[1]').text
        test_14 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.TextView[2]').text
        assert test_13 == 'Партнёр'
        assert test_14 == 'Личный кабинет'

    def test_winner_8(self, android_winner):
        """Проверяем в закладке "Бонусы" названия разделов и возможность их открыть."""
        android_winner.implicitly_wait(5)
        android_winner.find_elements_by_class_name('android.widget.EditText')[0].send_keys('vvd1')
        password = android_winner.find_elements_by_class_name('android.widget.EditText')[1]
        password.click()
        password.send_keys('qwerty123')
        android_winner.back()
        android_winner.implicitly_wait(5)
        password_imper = android_winner.find_elements_by_class_name('android.widget.EditText')[2]
        password_imper.click()
        password_imper.send_keys('3492440')
        android_winner.back()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.Button').click()
        android_winner.implicitly_wait(5)
        click_one = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.view'
                                                         '.ViewGroup/android.widget.LinearLayout['
                                                         '3]/android.view.ViewGroup[4]/android.widget.Button')
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        click_one.click()
        android_winner.implicitly_wait(5)
        test_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.view'
                                                      '.ViewGroup/androidx.viewpager.widget.ViewPager/android.view'
                                                      '.ViewGroup/android.widget.LinearLayout/android.widget'
                                                      '.TextView[1]').text
        assert test_2 == 'Передавайте клиентов'
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_class_name('android.widget.ImageView').click()
        android_winner.find_element_by_class_name('android.widget.ImageButton').click()
        android_winner.implicitly_wait(5)
        android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                             '@content-desc="Бонусы"]/android.widget.TextView').click()
        test_12 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                       '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                       '.ViewPager/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                                       '/android.widget.LinearLayout[1]/android.widget.TextView').text
        test_13 = android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                                       ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                       ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                       ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                                       "/android.widget.LinearLayout/androidx.viewpager.widget"
                                                       ".ViewPager/android.widget.ScrollView/android.widget"
                                                       ".LinearLayout/android.widget.ScrollView/android.widget"
                                                       ".LinearLayout/androidx.recyclerview.widget.RecyclerView"
                                                       "/android.widget.LinearLayout[2]/android.widget.TextView").text
        test_14 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                       '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                       '.ViewPager/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                                       '/android.widget.LinearLayout[3]/android.widget.TextView').text
        test_15 = android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                                       ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                       ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                       ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                                       "/android.widget.LinearLayout/androidx.viewpager.widget"
                                                       ".ViewPager/android.widget.ScrollView/android.widget"
                                                       ".LinearLayout/android.widget.ScrollView/android.widget"
                                                       ".LinearLayout/androidx.recyclerview.widget.RecyclerView"
                                                       "/android.widget.LinearLayout[4]/android.widget.TextView").text
        test_16 = android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                                       ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                       ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                       ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                                       "/android.widget.LinearLayout/androidx.viewpager.widget"
                                                       ".ViewPager/android.widget.ScrollView/android.widget"
                                                       ".LinearLayout/android.widget.ScrollView/android.widget"
                                                       ".LinearLayout/androidx.recyclerview.widget.RecyclerView"
                                                       "/android.widget.LinearLayout[5]/android.widget.TextView").text
        test_17 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                       '/android.widget.LinearLayout/androidx.viewpager.widget'
                                                       '.ViewPager/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.LinearLayout/android.widget.TextView').text
        assert test_12 == 'О программе'
        assert test_13 == 'Статус'
        assert test_14 == 'Каталог призов'
        assert test_15 == 'Счет'
        assert test_16 == 'История заказов'
        assert test_17 == 'Выйти'
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                             '/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/androidx.recyclerview.widget.RecyclerView'
                                             '/android.widget.LinearLayout[1]/android.widget.TextView').click()
        test_12_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                         '.view.ViewGroup/android.widget.TextView').text
        assert test_12_1 == 'О программе'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                             '2]/android.widget.TextView').click()
        test_13_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                         '.view.ViewGroup/android.widget.TextView').text
        test_13_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                         '.widget.LinearLayout/android.widget.LinearLayout/android'
                                                         '.widget.LinearLayout[1]/android.widget.TextView').text
        test_13_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                         '.widget.LinearLayout/android.widget.LinearLayout/android'
                                                         '.widget.LinearLayout[2]/android.widget.TextView').text
        assert test_13_1 == 'Статус'
        assert test_13_2 == 'Текущий статус'
        assert test_13_3 == 'Баллы'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget.LinearLayout'
                                             '/android.widget.ScrollView/android.widget.LinearLayout/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                             '3]/android.widget.TextView').click()
        test_14_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                         '.view.ViewGroup/android.widget.TextView').text
        test_14_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                         '.view.ViewGroup/android.widget.LinearLayout/android.widget'
                                                         '.LinearLayout[1]/android.widget.TextView').text
        test_14_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                         '.view.ViewGroup/android.widget.LinearLayout/android.widget'
                                                         '.LinearLayout[2]/android.widget.TextView').text
        assert test_14_1 == 'Каталог призов'
        assert test_14_2 == 'Текущий статус'
        assert test_14_3 == 'Баллы'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget"
                                             ".LinearLayout/android.widget.FrameLayout/android.widget"
                                             ".LinearLayout/android.widget.FrameLayout/android.widget"
                                             ".RelativeLayout/androidx.drawerlayout.widget.DrawerLayout"
                                             "/android.widget.LinearLayout/androidx.viewpager.widget"
                                             ".ViewPager/android.widget.ScrollView/android.widget"
                                             ".LinearLayout/android.widget.ScrollView/android.widget"
                                             ".LinearLayout/androidx.recyclerview.widget.RecyclerView"
                                             "/android.widget.LinearLayout[4]/android.widget.TextView").click()
        test_15_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                         '.view.ViewGroup/android.widget.TextView').text
        test_15_2 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                         '.widget.LinearLayout/android.widget.LinearLayout/android'
                                                         '.widget.LinearLayout[1]/android.widget.TextView').text
        test_15_3 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.FrameLayout/android'
                                                         '.widget.LinearLayout/android.widget.LinearLayout/android'
                                                         '.widget.LinearLayout[2]/android.widget.TextView').text
        assert test_15_1 == 'Счет'
        assert test_15_2 == 'Текущий статус'
        assert test_15_3 == 'Баллы'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                             ".FrameLayout/android.widget.RelativeLayout/androidx.drawerlayout.widget"
                                             ".DrawerLayout/android.widget.LinearLayout/androidx.viewpager.widget"
                                             ".ViewPager/android.widget.ScrollView/android.widget.LinearLayout"
                                             "/android.widget.ScrollView/android.widget.LinearLayout/androidx"
                                             ".recyclerview.widget.RecyclerView/android.widget.LinearLayout["
                                             "5]/android.widget.TextView").click()
        test_16_1 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                         '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                         '/android.view.ViewGroup/android.widget.LinearLayout/android'
                                                         '.view.ViewGroup/android.widget.TextView').text
        test_16_2 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                         '@content-desc="Исполнено"]/android.widget.TextView').text
        test_16_3 = android_winner.find_element_by_xpath('//android.widget.LinearLayout['
                                                         '@content-desc="Заказано"]/android.widget.TextView').text
        assert test_16_1 == 'История заказов'
        assert test_16_2 == 'ИСПОЛНЕНО'
        assert test_16_3 == 'ЗАКАЗАНО'
        android_winner.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Меню открыто"]').click()
        android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.LinearLayout/android.widget.FrameLayout/android.widget'
                                             '.RelativeLayout/androidx.drawerlayout.widget.DrawerLayout'
                                             '/android.widget.LinearLayout/androidx.viewpager.widget'
                                             '.ViewPager/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/android.widget.ScrollView/android.widget'
                                             '.LinearLayout/android.widget.LinearLayout/android.widget.TextView').click()
        test_18 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.TextView[1]').text
        test_19 = android_winner.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                       '.RelativeLayout/android.widget.ScrollView/android.widget'
                                                       '.LinearLayout/android.widget.TextView[2]').text
        assert test_18 == 'Партнёр'
        assert test_19 == 'Личный кабинет'
