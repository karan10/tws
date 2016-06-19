# Code by : Anonyomus
# Date : xx-xx-xxxx

from selenium import webdriver
import random
from random import randint
import time


class TalkWithStranger :

	def __init__ ( self, no_of_targets ) :

		self.__random_name_list = [ 'Carol','Aradhna','Patrica','Tanya','Rebecca' ] # initialize random name list
		self.__initiator_list = [ 'hey! ', 'hello, ', 'welcome! ', 'there?? ', 'anybody?? ', 'Hi ' ] 
		self.__country_list = [ 'India, Delhi', 'UK, London', 'Australia, melbourne' ]
		self.__is_connected = True
		self.__chat_terminator = 'Bye!! :)'
		# This is not a COMMENT , this is a SEPERATOR
		self.__chat_list = [ 'Looks like bad day for you, isnt it? :P', 'Well!! I am female, ' + str ( randint ( 18,28 ) ) + ' and you ? ' , 'Where are you from?', 'Cool!! I am from ' + random.choice ( self.__country_list )  + ' :)', 'How do you know about this site?', 'Well, in my case my friend suggested this site. And it is great. ;)', 'What are your interests ?', 'I like music, tv series, and talking with strangers.', 'Can you suggest a tv series to me. I am bored these days. ;)', 'oops! sorry got to go. Talk to you later.' , self.__chat_terminator  ] # chats in order
		# Again this is not a COMMENT , this is a SEPERATOR
		self.__total_targets = no_of_targets  # no of different persons to chat
		self.__target_no = 0
		self.__victim_site = 'http://talkwithstranger.com/' # site's url
		self.__driver_obj = self.__browser_initiator ( )  # open the browser, set driver
		self.__is_disconnected = False  # will be false if new session setup


	def __browser_initiator ( self ) :

		ext = webdriver.FirefoxProfile()
		adblockfile = 'adblockplusfirefox.xpi'
		ext.add_extension(adblockfile)
		ext.set_preference("extensions.adblockplus.currentVersion", "2.4")

		driver = webdriver.Firefox( ext )

		return driver

	# main code driving function
	def _here_the_fun_begins ( self ) :

		self.__initialize_connection ( )
		self.__send_message ( random.choice( self.__initiator_list ) ) # Send message to initiate conversation
		self.__enjoy_the_moment ( ) 

	# initialize a connection by setting a user name
	def __initialize_connection ( self ) :

		self.__driver_obj.get( self.__victim_site )
		input_name_obj = self.__driver_obj.find_elements_by_class_name('usernameInput')
		input_name_obj[0].send_keys( random.choice( self.__random_name_list ) )
		enter_chat_obj = self.__driver_obj.find_element_by_id('talk')
		enter_chat_obj.click()


	# write text in chat box and send it
	def __send_message ( self, text_to_send ) :

		chat_box_obj = self.__driver_obj.find_elements_by_class_name('form-control')
		chat_box_obj[0].send_keys( text_to_send )
		send_obj = self.__driver_obj.find_element_by_id('send')
		send_obj.click()


	def __enjoy_the_moment ( self ) :

		# loop till count < no of chat session
		while self.__target_no < self.__total_targets :

			# if new session(previous disconnected) then send initiator message
			if self.__is_disconnected is True :
				self.__send_message ( random.choice( self.__initiator_list ) )
				self.__is_disconnected = False

			if self.__check_if_new_conn_setup ( ) is True : 
				self.__is_disconnected = True 

			else :

				for chat in self.__chat_list :

					# make new connection if stranger disconnected the session
					if self.__check_if_new_conn_setup ( ) is True : break

					# wait for random seconds to send next msg
					time.sleep( randint ( 11,25 ) )

					self.__send_message ( chat )

					if chat == self.__chat_terminator :
						self.__leave_the_chat ( )
				pass

				self.__target_no = self.__target_no + 1

	def __leave_the_chat ( self ) :

		time.sleep( randint ( 8,13 ) )
		leave_obj = self.__driver_obj.find_element_by_id('leave')
		leave_obj.click()


	def __check_if_new_conn_setup ( self ) :

		try :
			refresh_obj = self.__driver_obj.find_element_by_id('refresh')
			refresh_obj.click()
			input_name_obj = self.__driver_obj.find_elements_by_class_name('usernameInput')
			input_name_obj[0].send_keys( random.choice( self.__random_name_list ) )
			enter_chat_obj = self.__driver_obj.find_element_by_id('talk')
			enter_chat_obj.click()
			return True
		except :
			return False

# Found it, now start.
if __name__ == "__main__" :

	no_of_unique_chats = 2
	tws_obj = TalkWithStranger ( no_of_unique_chats ) 
	tws_obj._here_the_fun_begins ( )