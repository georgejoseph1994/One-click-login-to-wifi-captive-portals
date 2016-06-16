#!/usr/bin/python
import re 
from mechanize import Browser
br = Browser()

#install mechanise for running this script
#python 2.7


# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a user-agent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

# Retrieve the captive portal login page
br.open( "http://192.168.0.66:8090/" )

# Select the form and username password colum
# For other users change the form name and username ,password 
# by looking into the source of login page{ for windows ctrl+u};

br.select_form( 'frmHTTPClientLogin' ) #form name
br.form[ 'username' ] = ''			   #Modify whats inside br.form[''] and enter the desired username in ''
br.form['password'] = ''			   #Modify whats inside br.form[''] and enter the desired password in ''


# login
br.submit()
