
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()	




	def login(self):
		bot = self.bot


		bot.get('https://www.instagram.com/accounts/login/')
		time.sleep(3)



		email = bot.find_element_by_name('username').send_keys(self.username)
		password = bot.find_element_by_name('password').send_keys(self.password)



		time.sleep(1)
		bot.find_element_by_name('password').send_keys(Keys.RETURN)



		time.sleep(3)



	def findMyFollowers(self, number_of_followers):

		bot = self.bot



		bot.get('https://instagram.com/' + self.username)
		time.sleep(2)


		bot.find_element_by_xpath('//a[@href="/' + self.username + '/followers/"]').click()


		time.sleep(1)


		popup = bot.find_element_by_class_name('isgrP')


		followers_array = []

		i = 1


		while len(followers_array) <= number_of_followers:

			bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)

			time.sleep(0.4)

			followers = bot.find_elements_by_class_name('FPmhX')


			for follower in followers:

				if follower not in followers_array:

					followers_array.append(follower.text)


			i+=1


		print(followers_array)


		self.followers = followers_array


	def followTheirFollowers(self, number_to_follow):

		bot = self.bot


		for follower in self.followers:

			bot.get('https://instagram.com/' + follower)

			time.sleep(2)


			if(len(bot.find_elements_by_xpath("//*[contains(text(), 'This Account is Private')]")) > 0):


				continue


			bot.find_element_by_xpath('//a[@href="/' + follower + '/followers/"]').click()

			time.sleep(3)


			follow = bot.find_elements_by_xpath("//button[contains(text(), 'Follow')]")


			i = 1


			for follower in follow:

				if(i != 1):

					bot.execute_script("arguments[0].click();", follower)


				if(i > number_to_follow):

					break

				i+=1

			time.sleep(2)



insta = InstagramBot('username', 'password')

insta.login()

insta.findMyFollowers(5)

insta.followTheirFollowers(10)


	