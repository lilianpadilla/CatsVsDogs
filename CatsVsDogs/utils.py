import os
import random
import piexif

def train_test_split(src_folder):
	# These are files that should not be used, as the jpgs are corrupted, 
	# and the .db files aren't images
    bad_files_cat = ['Thumbs.db', '666.jpg', '835.jpg']
    bad_files_dog = ['Thumbs.db', '11702.jpg']

	# **ADD YOUR CODE HERE**
	

	# remove corrupted exif data from the dataset
    remove_exif_data(src_folder+'Train/')
    remove_exif_data(src_folder+'Test/')

# helper function to remove corrupt exif data from Microsoft's dataset
def remove_exif_data(src_folder):
	_, _, cat_images = next(os.walk(src_folder+'Cat/'))
	for img in cat_images:
		try:
			piexif.remove(src_folder+'Cat/'+img)
		except:
			pass

	_, _, dog_images = next(os.walk(src_folder+'Dog/'))
	for img in dog_images:
		try:
			piexif.remove(src_folder+'Dog/'+img)
		except:
			pass


# ** Run train test split on data here **
