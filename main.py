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
import cgi

def valid_username(username):
    if ' ' in username:
        return False
    else:
        return username

#def verify_password(password):

def valid_email(email):
    if '@' not in email:
        return False

header = """<h2>I want to sign-up</h2>"""
form = """<form action='/' method='post'>
                <label>Username:<input type='text' name='username' required/></label>
                <br>
                <label>Password:<input type='text' name='password' required/><label>
                <br>
                <label>Verify Password:<input type='text' name='verify_password' required/></label>
                <br>
                <label>E-mail(Optional):<input type='text' name='email'/><label>
                <br>
                <input type='submit' value="signup"/></form>"""
#def verify_password(password,verfify_password):

#def valid_email(email):


class MainHandler(webapp2.RequestHandler):

    def get(self):
        #head = "<head><style>.error{color:red;}</style></head>"
        #Username= "<tr><td><label for='username'>Username</label><td><td><input name='username' type ='text' value required><span class='error'></span></td></tr>"
        #Password= "<tr><td><label for='password'>Password</label></td><td><input name='password' type ='text' value required><span class='error'></span></td></tr>"
        #Verify_password= "<tr><td><label for 'verify password'>Verify Password</label></td><td><input name='Verify password' type='text' required><span class='error'></span></td></tr>"
        #Email= "<tr><td><label for='email'>E-mail(Optional)</label></td><td><input name='email' type='text' value required><span class='error'></span></td></tr>"
        #formarea = "<form method='post'></table></tbody>"+Username+"<br>"+Password+"<br>"+Verify_password+"<br>"+Email+"</tbody><br><input type='submit'></form>"
        #body = "<body><h1>Signup</h1></body>" + formarea
        #content = head + body

        self.response.write(header+form)

    def post(self):

        username = self.request.get('username')
        email = self.request.get('email')
        signup_confirm = username +' has signed up.'


        if (valid_username(username) == False):
            self.response.write(header+form)
        #else:
        #    self.response.write('valid username')

        if (valid_email(email) == False):
            self.response.write(header+form)

            #self.response.write(header+form)

#class SignupHandler(webapp2.RequestHandler):

#    def post(self):
#        header = '<h2>Sign-up</h2>'
#        username = self.request.get('username')
#        password = self.request.get('password')
#        verify_password = self.request.get('verify_password')
#        signup_confirm = username +' has signed up.'
#        error = 'Passwords do not match'

#        self.response.write(header+signup_confirm)

        #if (password /= verify_password):
        #    self.redirect('/?error='+error)

#class LoginHandler(webapp2.LoginHandler):

app = webapp2.WSGIApplication([
    ('/', MainHandler),
#    ('/signup',SignupHandler),
], debug=True)
#app = webapp2.WSGIApplication(  [
#    ('/', MainHandler),
#    #('/login',LoginHandler)
#], debug=True)
