from bs4 import BeautifulSoup
import sys,io,time,urllib.request,pdfkit,os

startTime = time.time()

path = "/novels/kumo-desu-ga-nani-ka"
domain = "https://rtd.moe"
htmlFileName = "rtd.html"
htmlFile = None
pdfFileName = "rtd.pdf"

#Functions
def createHTMLFile():
	global htmlFile
	initialHTML =  """<!DOCTYPE html>
<html>
	<head>
		<title>Kumo-desu WN</title>
		<meta charset="UTF-8">
		<style>
			.margin {
				height: 50px;
			}
		</style>
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
	print("Requesting the main site...")
	try:
		handle = urllib.request.urlopen(domain+path)
	except:
		return False
	html = handle.read().decode("UTF-8")
	soup = BeautifulSoup(html, 'html.parser')

	# Get the links from the blog post
	toc = soup.find("div", { "class":"post-single-content" })
	links = toc.find_all("a")
	linkArr = []
	for link in links:
		parsedLink = link.get('href')
		linkArr.append(parsedLink)
	linkArr = linkArr[::-1]

	# Download and parse each link into our html file
	print("Downloading individual posts and saving them to file...")
	for link in linkArr:
		try:
			print("Downloading " + link + "...")
			handle = urllib.request.urlopen(link)
		except:
			print("Could not download " + link + "!")
			return False

		html = handle.read().decode("UTF-8")
		soup = BeautifulSoup(html, 'html.parser')

		# Remove all the wordpress stuff
		post = soup.find("div", { "class":"post-single-content" })
		post.find("div", { "class":"tags" }).decompose()
		post.find("div", { "class":"wp-post-navigation" }).decompose()

		appendToHTML(str(post))
		appendToHTML("<div>==============================</div>")
		appendToHTML("<div class='margin'></div>")

createHTMLFile()
ripSite()
finishHTMLFile()
print("Creating pdf...")
htmlToPDF()
print("Script finished in " + str(time.time() - startTime) + " seconds!")
