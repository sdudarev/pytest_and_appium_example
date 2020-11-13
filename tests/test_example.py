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
        android_winner.refresh()
        # сделать рефреш формы.

    def test_winner_5(self, android_winner):  # Проверяем названия разделов в закладке "Кабинет"
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
        assert test_13 == 'Winner'
        assert test_14 == 'Личный кабинет'

    def test_winner_6(self, android_winner):  # Проверяем названия разделов в закладке "Бонусы"
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
        assert test_12 == 'О программе'
        assert test_13 == 'Статус'
        assert test_14 == 'Каталог призов'
        assert test_15 == 'Счет'
        assert test_16 == 'История заказов'
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
        assert test_13 == 'Winner'
        assert test_14 == 'Личный кабинет'
