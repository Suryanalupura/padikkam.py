import PIL
from PIL import Image
from tkinter.filedialog import*

print("IMAGE COMPRESSOR")
print("UPLOAD FILE")
file_path = askopenfilename()
img = PIL.Image.open(file_path)
#myHeight , myWidth = img.size
#size can be adjusted or set to default as the original image size
#here size is set at 50x50
img = img.resize((50,50) , PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()
img.save(save_path+"_compressed.JPG")
