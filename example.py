# -*- coding: utf-8 -*-

# The MIT License
# 
# Copyright (c) 2011 Comfirm <http://www.amail.io/>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from comfirm_alphamail_client import * 

 
# Hello World-message with data that we've defined in our template
class HelloWorldMessage:
	def __init__(self):
		self.message = '' 		# Represents the <# payload.message #> in our template
		self.some_other_message = ''	# Represents the <# payload.some_other_message #> in our template


# Step 1: Let's start by entering the web service URL and the API-token you've been provided
# If you haven't gotten your API-token yet. Log into AlphaMail or contact support at 'support@amail.io'.
email_service = AlphaMailEmailService('http://api.amail.io/v2', 'YOUR-ACCOUNT-API-TOKEN-HERE')

# Step 2: Let's fill in the gaps for the variables (stuff) we've used in our template
message = HelloWorldMessage()
message.message = 'Hello world like a boss!'
message.some_other_message = 'And to the rest of the world! Chíkmàa! مرحبا! नमस्ते! Dumelang!'

# Step 3: Let's set up everything that is specific for delivering this email
payload = EmailMessagePayload()
payload.set_project_id(2)
payload.set_sender(EmailContact('Sender Company Name', 'your-sender-email@your-sender-domain.com'))
payload.set_receiver(EmailContact('Joe E. Receiver', 'email-of-receiver@amail.io', 1234)) # The 3rd argument is the optional receiver id and should be either a string or an integer
payload.set_body_object(message)

# Step 4: Haven't we waited long enough. Let's send this!
email_service.queue(payload)

