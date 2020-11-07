# 
# Example file for retrieving data from the internet
#
import urllib.request

def main():
  webUrl = urllib.request.urlopen("http://www.google.com")
  print("result code: " + str(webUrl.getcode()))	# 200 means the url was found
  data = webUrl.read()	# reads the URL of Google's homepage and prints it
  print(data)

if __name__ == "__main__":
  main()
