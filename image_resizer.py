import cv2
import argparse
from datetime import datetime


def resize(path, ratio=None, height=None, width=None):
	if path is None:
		print('Please specify path while executing python file')

	if ratio is not None and height is None:
		try:
			ratio = float(ratio)
			print('Reading Image...', end='')
			image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
			height, width, channels = image.shape 
			height = int(height*ratio)
			width = int(width*ratio)
			size = (height,width)
			print(f'\nConverting to {height}x{width} and Saving...', end='')
			savefile = 'IMG' + str(get_datetime()) + '.jpeg'
			cv2.imwrite(savefile ,cv2.resize(image, size))
			print(f'\nImage {savefile} Saved to CWD', end='')
			return
		except Exception as e:
			print(' !! Failed !! ERR:', e)

	elif height is not None and width is not None:
		try:
			print('Reading Image...', end='')
			image = cv2.imread(path, cv2.IMREAD_UNCHANGED)
			size = (int(height),int(width))
			print(f'\nConverting to {height}x{width} and Saving...', end='')
			savefile = 'IMG' + str(get_datetime()) + '.jpeg'
			cv2.imwrite(savefile ,cv2.resize(image, size))
			print(f'\nImage {savefile} Saved to CWD', end='')
			return 
		except Exception as e:
			print(' !! Failed !! ERR:', e)
	else:
		print('Please specify either Ratio with {ratio = <value>} or height and width using {height = <value> width = <value>}')


def get_datetime():
	timestamp = datetime.now()
	timestamp_str = timestamp.strftime("%d%m%Y%H%M%S")
	return timestamp_str


if __name__ == '__main__':
	print('## To convert using ratio --> python resizer.py <path> <ratio>\n## To convert using height and width --> python resizer.py <path> <ratio> <height> <width>')
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	parser.add_argument('ratio', nargs='?', default = None)
	parser.add_argument('height', nargs='?', default = None)
	parser.add_argument('width', nargs='?', default = None)
	args = parser.parse_args()
	resize(args.path, args.ratio, args.height, args.width)