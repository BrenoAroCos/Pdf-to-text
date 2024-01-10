# Pdf-to-text
Small code that converts a pdf file into txt by using image recognition AI to scan the page and transform it into text.

To use it, first you must install Tesseract, to do this, use the following link:
https://github.com/UB-Mannheim/tesseract/wiki

The pdf reader is configured to use portuguese as the trained language, so to use it, you must select the portuguese training data while installing, it is also possible to download the portuguese training data the following link:
https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata

After downloading it, save it in your tesseract training data folder, located inside where you installed Tesseract (EX: C:\...\Tesseract-OCR\tessdata)

lastly, you must add an environment path to your tesseract installation. After doing that, all there is left to do is run the executable and convert your pdf to text!
