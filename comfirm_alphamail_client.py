# -*- coding: utf-8 -*-
import urllib2
import json

# Email contact class
class EmailContact:
	def __init__(self, name, email):
		self.name = name
		self.email = email

	def set_name(self, value):
		self.name = value

	def set_email(self, value):
		self.email = value

# Message payload class
class EmailMessagePayload:
	def __init__(self):
		self.project_id = ''
		self.receiver_id = 0
		self.sender_name = ''
		self.sender_email = ''
		self.receiver_name = ''
		self.receiver_email = ''
		self.body = ''

	def set_project_id(self, id):
		self.project_id = id
		
	def set_receiver_id(self, id):
		self.receiver_id = id
		
	def set_sender(self, contact):
		self.sender_name = contact.name
		self.sender_email = contact.email
		
	def set_receiver(self, contact):
		self.receiver_name = contact.name
		self.receiver_email = contact.email
		
	def set_body_object(self, object):
		self.body = json.dumps(object.__dict__)

# Alpha-mail email service
class AlphaMailEmailService:
	def __init__(self, service_url, api_token):
		self.service_url = service_url
		self.api_token = api_token

	def queue(self, payload):
		# Basic Authentication
		password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
		password_manager.add_password(
			None, self.service_url, '', self.api_token
		)
		auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
		opener = urllib2.build_opener(auth_handler)
		urllib2.install_opener(opener)

		# Queue the message
		response = urllib2.urlopen(self.service_url+'/email/queue', json.dumps(payload.__dict__)).read()
		print 'Message was successfully queued!'
		
