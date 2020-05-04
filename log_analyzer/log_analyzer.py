#! python3
import re

text = open('log_analyzer/original.log', 'r')
login_regex = re.compile(
r'''username=[a-zA-Z0-9 !@#$%^&*./,]*&password=[a-zA-Z0-9 !@#$%^&*./,]*\s''')

credentials_list = []

for line in text:
    for user in login_regex.findall(line):
        user = user.strip()
        user_id, password = user.split('&')

        user_title, username = user_id.split('=')
        pass_title, passphrase = password.split('=')

        credentials_list.append('username:{}, password:{}'.format(
            username,passphrase))
text.close()

print(credentials_list)
