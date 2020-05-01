from selenium import webdriver
from selenium.webdriver.common.key import keys
import time


class Twitbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()


    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self, hashtag):
        bot = self.bot
        bot.get('http://twitter.com/search?q=' +hashtag+' &src=tyd')
        time.sleep(3)
        for i in range(1,20):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_element_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.find_element_by_class_name('HeartAnimation').click()
                time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


ed = Twitbot('','')
ed.login()
ed.like_tweet('webdevelopment')    