import sys
sys.path.insert(0, '/var/www/html/bapbot')
sys.path.insert(0, '/var/www/html/bapbot/apps')
sys.path.append('/var/www/html/bapbot/env/lib/python3.6/site-packages/')
sys.path.append('/var/www/html/bapbot/env/lib/python3.6/site-packages')

from bapbotapp import app as application
