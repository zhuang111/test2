from urllib import request
import re

page = request.urlopen('https://www.baidu.com')
htmlcode = page.read()

print(htmlcode)

reg = r'src="(.+?/.jpg)"'
htmlcode = htmlcode.decode('UTF-8')
reg_word = re.compile(reg)

imglist = reg_word.findall(htmlcode)

for img in imglist:
    print("tupian "&img)

