import urllib.request

# Specify the URL you want to open
url = "https://en.wikipedia.org/wiki/10BASE2"

# Open the URL
response = urllib.request.urlopen(url)

# Read the contents of the URL
data = response.read()

# Print the data
print(data)
