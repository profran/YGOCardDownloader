#!/usr/bin/env python

import xml.etree.ElementTree as ET
import os
import base64

def use_template():

	array = []
	x = 0
	y = 0

	for file in os.listdir():

		filename = os.fsdecode(file)

		if filename.endswith(".jpg"):

			if (x < 9):

				with open(filename, "rb") as image_file:

					encoded_string = "data:image/jpeg;base64," + str(base64.b64encode(image_file.read()))[1:-1]
					array.append(encoded_string)
				x += 1

			elif (x == 9):
				x = 0
				print(y)
				template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
			<!-- Created with Inkscape (http://www.inkscape.org/) -->
			<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="210mm" height="297mm" viewBox="0 0 210 297" version="1.1" id="svg8" inkscape:version="0.92.1 r15371" sodipodi:docname="template.svg">
				<defs id="defs2" />
				<sodipodi:namedview id="base" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageopacity="0.0" inkscape:pageshadow="2" inkscape:zoom="0.45254834" inkscape:cx="1014.6284" inkscape:cy="865.54351" inkscape:document-units="mm" inkscape:current-layer="layer1" showgrid="false" inkscape:snap-bbox="true" inkscape:bbox-nodes="true" inkscape:snap-bbox-edge-midpoints="true" showguides="true" inkscape:guide-bbox="true" inkscape:bbox-paths="true" inkscape:snap-page="true" inkscape:window-width="1600" inkscape:window-height="847" inkscape:window-x="-8" inkscape:window-y="-8" inkscape:window-maximized="1">
					<sodipodi:guide position="0,297" orientation="1,0" id="guide4485" inkscape:locked="false" />
				</sodipodi:namedview>
				<metadata id="metadata5">
					<rdf:RDF>
						<cc:Work rdf:about="">
							<dc:format>image/svg+xml</dc:format>
							<dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
							<dc:title></dc:title>
						</cc:Work>
					</rdf:RDF>
				</metadata>
				<g inkscape:label="layer_1" inkscape:groupmode="layer" id="layer1">
					<rect style="opacity:1;fill:#ffffff;fill-opacity:1;fill-rule:evenodd;stroke:#000000;stroke-width:0.28200001;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" 
						id="rect4492"
				       width="210"
				       height="297"
				       x="0"
				       y="0" />
					<image y="211" x="0" id="image_1" xlink:href="{0}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="211" x="59" id="image_2" xlink:href="{1}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="211" x="118" id="image_3" xlink:href="{2}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="125" x="0" id="image_4" xlink:href="{3}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="125" x="59" id="image_5" xlink:href="{4}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="125" x="118" id="image_6" xlink:href="{5}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="39" x="0" id="image_7" xlink:href="{6}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="39" x="59" id="image_8" xlink:href="{7}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
					<image y="39" x="118" id="image_9" xlink:href="{8}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				</g>
			</svg>""".format(*array)

				file = open(str("page" + str(y) + ".svg"), "w")
				file.write(template)
				file.close()
				y += 1
				array = []

		else:

			pass


def use_template_1():

	array = []
	x = 0
	y = 0
	z = 0

	error = False

	while (not error):
		
		filename = str(z) + ".jpg"

		if (x < 9):

			try:
				
				with open(filename, "rb") as image_file:

					encoded_string = "data:image/jpeg;base64," + str(base64.b64encode(image_file.read()))[1:-1]
					array.append(encoded_string)

					z += 1
					x += 1

			except Exception as e:

				while x < 9:

					with open("Backcover.jpg", "rb") as image_file:

						encoded_string = "data:image/jpeg;base64," + str(base64.b64encode(image_file.read()))[1:-1]
						array.append(encoded_string)

						x += 1

				error = True
					
		if (x == 9):

			x = 0

			print(y)

			template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
		<!-- Created with Inkscape (http://www.inkscape.org/) -->
		<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" width="210mm" height="297mm" viewBox="0 0 210 297" version="1.1" id="svg8" inkscape:version="0.92.1 r15371" sodipodi:docname="template.svg">
			<defs id="defs2" />
			<sodipodi:namedview id="base" pagecolor="#ffffff" bordercolor="#666666" borderopacity="1.0" inkscape:pageopacity="0.0" inkscape:pageshadow="2" inkscape:zoom="0.45254834" inkscape:cx="1014.6284" inkscape:cy="865.54351" inkscape:document-units="mm" inkscape:current-layer="layer1" showgrid="false" inkscape:snap-bbox="true" inkscape:bbox-nodes="true" inkscape:snap-bbox-edge-midpoints="true" showguides="true" inkscape:guide-bbox="true" inkscape:bbox-paths="true" inkscape:snap-page="true" inkscape:window-width="1600" inkscape:window-height="847" inkscape:window-x="-8" inkscape:window-y="-8" inkscape:window-maximized="1">
				<sodipodi:guide position="0,297" orientation="1,0" id="guide4485" inkscape:locked="false" />
			</sodipodi:namedview>
			<metadata id="metadata5">
				<rdf:RDF>
					<cc:Work rdf:about="">
						<dc:format>image/svg+xml</dc:format>
						<dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
						<dc:title></dc:title>
					</cc:Work>
				</rdf:RDF>
			</metadata>
			<g inkscape:label="layer_1" inkscape:groupmode="layer" id="layer1">
				<image y="211" x="0" id="image_1" xlink:href="{0}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="211" x="59" id="image_2" xlink:href="{1}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="211" x="118" id="image_3" xlink:href="{2}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="125" x="0" id="image_4" xlink:href="{3}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="125" x="59" id="image_5" xlink:href="{4}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="125" x="118" id="image_6" xlink:href="{5}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="39" x="0" id="image_7" xlink:href="{6}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="39" x="59" id="image_8" xlink:href="{7}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
				<image y="39" x="118" id="image_9" xlink:href="{8}" preserveAspectRatio="none" height="86" width="60" style="stroke-width:1.85008931" />
			</g>
		</svg>""".format(*array)

			file = open(str("page_" + str(y) + ".svg"), "w")
			file.write(template)
			file.close()
			y += 1
			array = []

use_template_1()

