# -*- coding: utf-8 -*-
import urllib2
import json

# Email contact class
class EmailContact:
	def __init__(self, name, email, id='0'):
		self.name = name
		self.email = email
		self.id = id
	
	def set_name(self, value):
		self.name = value

	def set_email(self, value):
		self.email = value

	def set_id(self, value):
		self.id = value

# Message payload class
class EmailMessagePayload:
	def __init__(self):
		self.project_id = ''
		self.sender = EmailContact('', '', 0)
		self.receiver = EmailContact('', '', 0)
		self.payload = ''

	def set_project_id(self, id):
		self.project_id = id
		
	def set_sender(self, contact):
		self.sender = contact
		
	def set_receiver(self, contact):
		self.receiver = contact
		
	def set_body_object(self, object):
		self.payload = object

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
		
