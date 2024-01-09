# Pdf-to-text
Small code that converts a pdf file into txt by using image recognition AI to scan the page and transform it into text.

To use it, first you must install Tesseract, to do this, use the following link:
https://github.com/UB-Mannheim/tesseract/wiki

The pdf reader is configured to use portuguese as the trained language, so to use it, you also must download the portuguese training data for tesseract using the following link:
https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata

After downloading it, save it in your tesseract training data folder, located inside where you installed pytesseract (EX: C:\...\Tesseract-OCR\tessdata)

