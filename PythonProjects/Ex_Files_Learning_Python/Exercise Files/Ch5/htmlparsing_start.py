# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

metacount = 0;

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    global metacount
    if tag == "meta":
      metacount += 1

    print ("Encountered a start tag:", tag)
    pos = self.getpos() # returns a tuple indication line and character
    print ("\tAt line: ", pos[0], " position ", pos[1])

    if attrs.__len__() > 0:
      print ("\tAttributes:")
      for a in attrs:
        print ("\t", a[0],"=",a[1])
      
  def handle_endtag(self, tag):
    print ("Encountered an end tag:", tag)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])
    
  def handle_data(self, data):
    if (data.isspace()):
      return
    print ("Encountered some text data:", data)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])
  
  def handle_comment(self, data):
    print ("Encountered comment:", data)
    pos = self.getpos()
    print ("\tAt line: ", pos[0], " position ", pos[1])

def main():
  parser = MyHTMLParser()    
  f = open("samplehtml.html", "r")

  if f.mode == "r":
    contents = f.read()
    parser.feed(contents)

  print("%d meta tags encountered" % metacount)
  f.close()
  parser.close()

if __name__ == "__main__":
  main();
  