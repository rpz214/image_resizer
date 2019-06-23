import argparse
import os
from PIL import Image
import sys


class image_resizer:
    def __init__(self):
        # initialize arg parser
        self.parser = argparse.ArgumentParser(description='Resize source image to a square and write to destination')
        self.parser.add_argument('src', type=self._src_path, help='Source file, file path')
        self.parser.add_argument('dst', type=self._dst_path, help='Destination directory, directory path')
        self.parser.add_argument('size', type=self.check_positive_int, help='Size of destination file, positive int')
        # image properties
        self.format = None
        self.size = None
        self.mode = None

    @staticmethod
    def _src_path(path):
        """
        Checks if SRC path is valid file
        :param path: path to SRC
        """
        if not os.path.isfile(path):
            raise argparse.ArgumentTypeError('Input a valid source file. {} is not a file.'.format(path))
        return path

    @staticmethod
    def _dst_path(path):
        """
        Checks if DST path is valid dir
        :param path: path to DST
        """
        if not os.path.isdir(path):
            raise argparse.ArgumentTypeError('Input a valid destination directory. {} is not a directory.'.format(path))
        return path

    @staticmethod
    def check_positive_int(size):
        """
        Checks if size is a positive int
        :param size: size
        """
        size = int(size)
        if size <= 0:
            raise argparse.ArgumentTypeError('{} must be a positive int'.format(size))
        return size

    def _sanitize_format(self, sourceFile):
        """
        Sanitize format of input sourceFile
        :param sourceFile: source image file
        """
        if not self.format:
            raise argparse.ArgumentTypeError('Unable to process image format. Bad source file: {}'.format(sourceFile))

    def _sanitize_size(self, sourceFile):
        """
        Sanitize size of input sourceFile
        :param sourceFile: source image file
        """
        if not self.size:
            raise argparse.ArgumentTypeError('Unable to process image size. Bad source file: {}'.format(sourceFile))

    def _sanitize_mode(self, sourceFile):
        """
        Sanitize mode of input sourceFile
        :param sourceFile: source image file
        """
        if not self.mode:
            raise argparse.ArgumentTypeError('Unable to process image mode. Bad source file: {}'.format(sourceFile))

    def sanitize_args(self, sourceFile):
        """
        Sanitize input sourceFile
        :param sourceFile: source image file
        """
        try:
            with Image.open(sourceFile) as img:
                img.verify()
                # retrieve image file information
                self.format = img.format
                self.size = img.size
                self.mode = img.mode
        except IOError as errMsg:
            raise argparse.ArgumentTypeError('Error: {}'.format(errMsg))
        # sanitize image file information
        self._sanitize_format(sourceFile)
        self._sanitize_size(sourceFile)
        self._sanitize_mode(sourceFile)

    def print_image(self, sourceFile):
        """Prints image information"""
        print('{0} {1} {0}'.format('-' * 20, 'Current Image Properties'))
        print('Filename {}'.format(sourceFile))
        print('Format: {}'.format(self.format))
        print('Size: {}'.format(self.size))
        print('Mode: {}\n'.format(self.mode))

    @staticmethod
    def process_image(sourceFile, destinationFile, size):
        """
        Processes image and resizes it to the desired input square size
        :param sourceFile: source image file
        :param destinationFile: destination image file
        :param size: new square size of the source image file
        """
        print('Processing image...')
        with Image.open(sourceFile) as img:
            # resize image to new square size
            out = img.resize((size, size))
            # save new image as destination file
            out.save(destinationFile)
        print('Created {0} with size ({1}, {1})'.format(destinationFile, size))

    def run(self, args):
        """
        Run with args passed through argparse
        :param args: CLI args
        """
        # run parser to get args
        args = self.parser.parse_args(args=args)
        sourceFile = args.src
        destinationDir = args.dst
        destinationFile = os.path.join(destinationDir, os.path.basename(sourceFile))
        newSize = args.size
        # check size and image file
        self.sanitize_args(sourceFile)
        # print image data
        self.print_image(sourceFile)
        # process image
        self.process_image(sourceFile, destinationFile, newSize)


if __name__ == '__main__':
    image_resizer().run(sys.argv[1:])
