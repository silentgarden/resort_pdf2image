from pdf2image import convert_from_path

url = r'C:\Users\Admin\Documents\Bank Information.pdf'
images = convert_from_path(url)

images[0].save('pagex'+'.jpg', 'JPEG')
