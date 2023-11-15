from pdf2image import convert_from_path

images = convert_from_path('example2.pdf')

images[0].save('pagex'+'.jpg', 'JPEG')
