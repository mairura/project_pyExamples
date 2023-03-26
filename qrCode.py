import pyqrcode

s = "https://www.instagram.com/python.times/"

url = pyqrcode.create(s)

url.svg("myinsta.svg", scale=8)
