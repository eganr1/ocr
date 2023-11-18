# OCR

I created this repo as a tool for students like me who find it difficult to annotate low-quality PDF scans. This code uses optical character recognition (OCR) which identifies a file's text, thereby enabling readers to select it, highlight it, copy it, and more. After experimenting with Tesseract, Pytesseract, and OpenCV, I ultimately found the code contained in Jonathon Lee's [Medium article](https://medium.com/social-impact-analytics/extract-text-from-unsearchable-pdfs-for-data-analysis-using-python-a6a2ca0866dd) to be the most successful in terms of its balance of efficacy and simplicity. As such, the steps for running this code are easy:

## Preliminary Installation

The following steps describe the process of installing Tesseract and the required packages using Terminal. If these are already installed on your device, proceed to step 3.

1. Install Tesseract:
  `brew install tesseract`
3. Install the following packages:
  `pip install ocrmypdf`
  `pip install pytesseract`
  `pip install opencv-python`
  `pip install pdf2image`

## Running the Code

1. Clone this ocr git repository to your local device.
2. Open the ocr folder and delete the Genette PDF and the OCR_Genette PDF. This is important because the code generates an OCR version of any PDF within the folder.
3. Place your PDF in the ocr folder.
4. Navigate to `ocr_converter.py` and run the code. This will create a new PDF with "OCR_" before the original title.
5. Locate the generated PDF within the ocr folder.
