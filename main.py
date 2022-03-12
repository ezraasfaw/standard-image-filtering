from PIL import Image, ImageFilter
from tqdm import tqdm

# region Optional: A task bar to show progress.
pbar = tqdm(total=5)
pbar.set_description('Processing Pipeline')
# endregion
# region Open the file.
filename = r'Media\penicillin.jpg'
Img = Image.open(filename)
pbar.update()
# endregion
# region Apply the blur filters.
Blurred_1 = Img.filter(ImageFilter.BLUR)
Blurred_2 = Img.filter(ImageFilter.BoxBlur(20))
Blurred_3 = Img.filter(ImageFilter.GaussianBlur(10))
pbar.update()
# Blurred_3.show()
# endregion
# region Apply the median filter.
Median_1 = Img.filter(ImageFilter.MedianFilter(9))
pbar.update()
# endregion
# region Apply the max filter.
Max = Img.filter(ImageFilter.MaxFilter(3))
pbar.update()
# endregion
# region Apply sharpen filters.
Sharpen_1 = Img.filter(ImageFilter.SHARPEN)
Sharpen_2 = Img.filter(ImageFilter.UnsharpMask(30))
pbar.update()
# endregion
# region Display only the sharpened 
image (unsharp mask)
Sharpen_2.show()
pbar.close()
# endregion
