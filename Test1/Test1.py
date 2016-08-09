import urllib
import urllib2
import re
import webbrowser



# webbrowser.open('http://www.fender.com/en-US')

html_content = urllib2.urlopen('http://www.fender.com/en-US').read()
print html_content
matches = re.findall('Finest', html_content)
if len(matches) == 0:
   print 'did not find anything'
else:
   print 'found it $matches'


webbrowser.open('http://shop.fender.com/en-US/best-reviewed-gear/')


