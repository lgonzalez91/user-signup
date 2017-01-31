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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        head = "<head><style>.error{color:red;}</style></head>"
        Username= "<tr><td><label for='username'>Username</label><td><td><input name='username' type ='text' value required><span class='error'></span></td></tr>"
        Password= "<tr><td><label for='password'>Password</label></td><td><input name='password' type ='text' value required><span class='error'></span></td></tr>"
        Verify_password= "<tr><td><label for 'verify password'>Verify Password</label></td><td><input name='Verify password' type='text' required><span class='error'></span></td></tr>"
        Email= "<tr><td><label for='email'>E-mail(Optional)</label></td><td><input name='email' type='text' value required><span class='error'></span></td></tr>"
        formarea = "<form method='post'></table></tbody>"+Username+"<br>"+Password+"<br>"+Verify_password+"<br>"+Email+"</tbody><br><input type='submit'></form>"
        body = "<body><h1>Signup</h1></body>" + formarea
        content = head + body
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
