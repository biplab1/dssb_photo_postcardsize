from PIL import Image

im = Image.open("test_image.jpg")
width, height = im.size 

required_width = 5.0  #postcard size 5 inches x 7 inches
required_height = 7.0

dpi = im.info['dpi']

dpi_one = dpi[0]

width_inches = width/dpi_one
extra = (width_inches - required_width)*dpi_one   #convert inches to pixels
cut = extra/2.0
cut_left = cut # cropping on the left
cut_right = width - cut # cropping on the right

(left, upper, right, lower) = (cut_left, 0, cut_right, height)

im_crop = im.crop((left, upper, right, lower))

im_crop.save("test.jpg")

width_new, height_new = im_crop.size

print (width_new/dpi_one, height_new/dpi_one)

im_crop.show()
