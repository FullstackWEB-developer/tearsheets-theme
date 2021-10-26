# Portformer Tearsheet Generator

## Getting started

```
   npm install
   npm run dev
```

## Two ways to generate PDFS:

Dependencies for pdf

Version 1

```bash
pip install pdfkit
sudo apt-get install wkhtmltopdf
```

```python
import pdfkit
pdfkit.from_url('http://localhost:1313/fund/cbls/','my_testpdf.pdf', options={'page-width':2024, 'orientation':'Landscape'})  #https://pypi.org/project/pdfkit/

```
Version 2
https://weasyprint.org/samples/
https://weasyprint.readthedocs.io/en/latest/index.html

```bash
pip install weasyprint
weasyprint http://localhost:1313/fund/cbls/ test_weasyprint.pdf
```

Dimensions

 * `8.5 x 11` inches
 * `612 x 792` px


Misc Sources
 * https://build.vsupalov.com/tailwind-with-static-site/

# Printing Headers and Footers
 * https://medium.com/@Idan_Co/the-ultimate-print-html-template-with-header-footer-568f415f6d2a
 * https://stackoverflow.com/a/64599494/2988073
