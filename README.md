# Instructions for Generating PDF OCR Using Terminal

1. Install PyPDFOCR using `pip install pypdfocr`

2. Clone repo using `git clone https://github.com/virantha/pypdfocr.git`

3. Install the following libraries:

`pip install Pillow`
`pip install reportlab`
`pip install watchdog`
`pip install pypdf2`

4. Install the following dependencies:

`brew install tesseract`
`brew install ghostscript`
`brew install poppler`
`brew install imagemagick`

5. Convert to OCR using `pypdfocr file.pdf`

----

Optical character recognition (OCR) identifies text in scanned documents and images. 

1. Install the OCR engine Tesseract library using `brew install Tesseract`

2. Install the pytesseract package using `pip install pytesseract`