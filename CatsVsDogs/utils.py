import os
import piexif

def train_test_split(src_folder):
	# These are files that should not be used, as the jpgs are corrupted, 
	# and the .db files aren't images
	bad_files_cat = ['Thumbs.db', '666.jpg', '835.jpg']
	bad_files_dog = ['Thumbs.db', '11702.jpg']

	# **ADD YOUR CODE HERE*
	train_cat = os.path.join(src_folder, 'Train', 'Cat')
	train_dog = os.path.join(src_folder, 'Train', 'Dog')
	test_cat = os.path.join(src_folder, 'Test', 'Cat')
	test_dog = os.path.join(src_folder, 'Test', 'Dog')

	for directory in [train_cat, train_dog, test_cat, test_dog]:
		if not os.path.exists(directory):
			os.makedirs(directory)
	
	cat = os.path.join(src_folder, 'Cat')
	dog = os.path.join(src_folder, 'Dog')

	cat_images = [img for img in os.listdir(cat) if img not in bad_files_cat]
	dog_images = [img for img in os.listdir(dog) if img not in bad_files_dog]
	
	split_cat = int(len(cat_images) * 0.8)
	split_dog = int(len(dog_images) * 0.8)

	train_cats = cat_images[:split_cat]
	test_cats = cat_images[split_cat:]
    
	train_dogs = dog_images[:split_dog]
	test_dogs = dog_images[split_dog:]
	
	for img in train_cats:
		src = os.path.join(cat, img)
		dst = os.path.join(train_cat, img)
		os.system(f'cp "{src}" "{dst}"')

	for img in test_cats:
		src = os.path.join(cat, img)
		dst = os.path.join(test_cat, img)
		os.system(f'cp "{src}" "{dst}"')
	
	for img in train_dogs:
		src = os.path.join(dog, img)
		dst = os.path.join(train_dog, img)
		os.system(f'cp "{src}" "{dst}"')

	for img in test_dogs:
		src = os.path.join(dog, img)
		dst = os.path.join(test_dog, img)
		os.system(f'cp "{src}" "{dst}"')

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
# train_test_split('Dataset/PetImages/')
