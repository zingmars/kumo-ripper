from bs4 import BeautifulSoup
import sys,io,time,urllib.request,pdfkit,os

startTime = time.time()
domain = sys.argv[1]
htmlFileName = "rtd-single.html"
pdfFileName = "rtd-single.pdf"
htmlFile = None

#Functions
def createHTMLFile():
	global htmlFile
	initialHTML =  """<!DOCTYPE html>
<html>
	<head>
		<title>Kumo-desu WN</title>
		<meta charset="UTF-8">
	</head>
	<body>
	"""
	f = open(htmlFileName, "w")
	f.write(initialHTML)
	f.close()
	htmlFile = open(htmlFileName, mode="a", encoding="utf-8") #Open the file for appending

def appendToHTML(data):
	global htmlFile
	htmlFile.write(data)

def finishHTMLFile():
	global htmlFile
	endingHTML = """
</body>
</html>"""
	htmlFile.write(endingHTML)
	htmlFile.close()

#Take our HTML file and convert it to a PDF file.
def htmlToPDF():
	pdfkit.from_file(htmlFileName, pdfFileName)

# Downloader
def ripSite():
	# Get the main site
	handle = None
	print("Requesting "+ domain + "...")
	try:
		handle = urllib.request.urlopen(domain)
	except:
		return False
	html = handle.read().decode("UTF-8")
	soup = BeautifulSoup(html, 'html.parser')

	# Remove all the wordpress stuff
	post = soup.find("div", { "class":"post-single-content" })
	post.find("div", { "class":"tags" }).decompose()
	post.find("div", { "class":"wp-post-navigation" }).decompose()
	appendToHTML(str(post))

createHTMLFile()
ripSite()
finishHTMLFile()
print("Creating pdf...")
htmlToPDF()
print("Script finished in " + str(time.time() - startTime) + " seconds!")
