#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

examples = """
<form>
<input type="text" name="q" value="hello">
<br>
<input type="submit">
</form>
"""

form = """
<form action="http://www.google.com/search">
<input type="text" name="q">
<input type="submit">
</form>

<a href="plot/example48_interactive_legend.html">example48_interactive_legend</a>
"""

birthday_form = """
<form method="post" action="/birthday">
	What is your birthday?

	<br>

	<label>Month <input type="text" name="month"></label>
	<label>Day <input type="text" name="day"></label>
	<label>Year <input type="text" name="year"></label>

	<br>
	
	<input type="submit">

</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This is my first GAE app<br>I have a cute piglet!'+form)

class ExamplesHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Here are some examples:<br>' + examples)

class BirthdayHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(birthday_form)
	def post(self):
		self.response.write("You are 4 years old!")
		
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/birthday', BirthdayHandler),
    ('/examples', ExamplesHandler)
], debug=True)
