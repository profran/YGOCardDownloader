#!/usr/bin/env python

import requests
import os

clear = lambda: os.system('cls')

def newDeckPrint():

	clear()
	print("Welcome to Yu-Gi-Oh PDF printable cards!\n")

	dir = os.getcwd()
	deckArray = []

	for file in os.listdir(dir):

		if (file.endswith(".ydk")):

			deckArray.append(file)

	print("Wich deck do you want to download?: \n")

	for deck, x in zip(deckArray, range(0, len(deckArray))):

		print("-->({0}): ".format(x) + deck)

	while (True):
		
		selectedDeck = int(input("--> "))

		if (selectedDeck > len(deckArray)):
			pass
		else:
			break

	clear()

	print("Now downloading " + str(deckArray[selectedDeck])[:-4] + "... \n")

	downloadImages(str(deckArray[selectedDeck]))

def resizeImage(infile, output_dir="", size=(1024,768)):
	outfile = os.path.splitext(infile)[0]+"_resized"
	extension = os.path.splitext(infile)[1]

	if (cmp(extension, ".jpg")):
			return

	if infile != outfile:
		try :
			im = Image.open(infile)
			im.thumbnail(size, Image.ANTIALIAS)
			im.save(output_dir+outfile+extension,"JPEG")
		except IOError:
			print("cannot reduce image for ", infile)

def downloadImages(deckName):

	urls = []
	lines = []

	directory = os.getcwd()

	with open(deckName) as f:
		for line in f:

			if ('#' not in line and '!' not in line):

				urls.append("https://www.ygoprodeck.com/pics/" + line + ".jpg")
				lines.append(line[:-2])

	totalDownloads = len(urls)

	for x, y in zip(urls, range(0, (totalDownloads))):

		while (True):
			
			print("Downloading card " + str(y) + " out of " + str(totalDownloads))

			r = requests.get(x, allow_redirects=False)

			headers = {"authority" : "www.ygoprodeck.com",
						"method" : "GET",
						"path" : str(lines[y]),
						"scheme" : "https",
						"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
						"accept-encoding" : "gzip, deflate, br",
						"accept-language" : "en-US,es-AR;q=0.8,es;q=0.6,en;q=0.4",
						"cache-control" : "max-age=0",
						"cookie" : "__cfduid=d44a7d84ccf5584239828478ed1850abf1508689423; _ga=GA1.2.324886416.1508689429; _gid=GA1.2.1979240285.1508689429",
						"upgrade-insecure-requests" : "1",
						"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

			r = requests.get(x, headers=headers)
			print(r.status_code)

			if(r.status_code == requests.codes.ok):

				filename = str(y) + ".jpg"

				cardDirectory = os.path.join(str(directory), str(deckName[:-4]))

				if not os.path.exists(cardDirectory):

					os.makedirs(cardDirectory)

				with (open(os.path.join(cardDirectory, filename), 'ab')) as fh:

					fh.write(r.content)

				break

	downloadImage(urls, deckName)

def downloadImage(urls, deckName):

	print("Do you need to re-download a card?")

	while(True):

		election = input("Card number: ")

		if (str(election) == ""):
			break
		else:

			directory = os.getcwd()
			totalDownloads = len(urls)

			print("Downloading card " + str(election))

			r = requests.get(x, allow_redirects=False)

			headers = {"authority" : "www.ygoprodeck.com",
						"method" : "GET",
						"path" : str(lines[y]),
						"scheme" : "https",
						"accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
						"accept-encoding" : "gzip, deflate, br",
						"accept-language" : "en-US,es-AR;q=0.8,es;q=0.6,en;q=0.4",
						"cache-control" : "max-age=0",
						"cookie" : "__cfduid=d44a7d84ccf5584239828478ed1850abf1508689423; _ga=GA1.2.324886416.1508689429; _gid=GA1.2.1979240285.1508689429",
						"upgrade-insecure-requests" : "1",
						"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

			r = requests.get(x, headers=headers)
			filename = "re-download-" + str(election) + ".jpg"

			cardDirectory = os.path.join(str(directory), str(deckName[:-4]))

			if not os.path.exists(cardDirectory):

				os.makedirs(cardDirectory)

			with (open(os.path.join(cardDirectory, filename), 'ab')) as fh:

				fh.write(r.content)




if __name__ == '__main__':

	newDeckPrint()

'''
if __name__=="__main__":
	output_dir = "resized"
	dir = os.getcwd()

	if not os.path.exists(os.path.join(dir,output_dir)):
		os.mkdir(output_dir)

	for file in os.listdir(dir):
		resizeImage(file,output_dir)
'''