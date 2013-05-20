# -*- coding: utf-8 -*-
import urllib2
import json

# Email contact class
class EmailContact:
	def __init__(self, name, email, id='0'):
		self.name = name
		self.email = email
		self.id = id
	
	def set_name(self, name):
		self.name = name
	
	def get_name(self):
		return self.name

	def set_email(self, email):
		self.email = email

	def get_email(self):
		return self.email

	def set_id(self, id):
		self.id = id
		
	def get_id(self):
		return self.id

# Message payload class
class EmailMessagePayload:
	def __init__(self):
		self.project_id = ''
		self.sender = EmailContact('', '', 0)
		self.receiver = EmailContact('', '', 0)
		self.payload = ''

	def set_project_id(self, id):
		self.project_id = id
	
	def get_project_id(self):
		return self.project_id
	
	def set_sender(self, contact):
		self.sender = contact
		
	def get_sender(self):
		return self.sender
		
	def set_receiver(self, contact):
		self.receiver = contact
		
	def get_receiver(self):
		return self.receiver
		
	def set_body_object(self, object):
		self.payload = object
		
	def get_body_object(self):
		return self.payload

# AlphaMail email service
class AlphaMailEmailService:
	def __init__(self, service_url, api_token):
		self.service_url = service_url
		self.api_token = api_token

	def set_service_url(self, url):
		self.service_url = url
	
	def get_service_url(self):
		return self.service_url

	def set_api_token(self, token):
		self.api_token = token
	
	def get_api_token(self):
		return self.api_token

	def queue(self, payload):
		# Basic Authentication
		password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
		password_manager.add_password(
			None, self.service_url, '', self.api_token
		)
		auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
		opener = urllib2.build_opener(auth_handler)
		urllib2.install_opener(opener)
	
		# build JSON data
		data = """
			{{ 
				"project_id": {0},
				"sender": {1},
				"receiver": {2}
				"payload": {3}
			}}
		""".format(
			payload.project_id, 
			json.dumps(payload.sender.__dict__), 
			json.dumps(payload.receiver.__dict__), 
			json.dumps(payload.payload.__dict__)
		)

		# Queue the message
		response = urllib2.urlopen(self.service_url+'/email/queue', data).read()
		print 'Message was successfully queued!'
		
