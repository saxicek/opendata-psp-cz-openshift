import urllib
import os
import logging
from importer.psp_cz import import_all
from optparse import OptionParser
from zipfile import ZipFile

class PspCzImport(object):
    files = {'poslanci.zip': 'http://www.psp.cz/eknih/cdrom/opendata/poslanci.zip',
             'hl-2010ps.zip': 'http://www.psp.cz/eknih/cdrom/opendata/hl-2010ps.zip'}

    def __init__(self, data_dir):
        self.data_dir = data_dir if data_dir[-1:] == '/' else data_dir + '/'

    def _file_download(self, source, destination):
        urllib.urlretrieve(source, destination)

    def download_files(self):
        for file, url in self.files.iteritems():
            logging.info('Downloading ' + url)
            file_path = self.data_dir + file
            if os.access(file_path, os.F_OK):
                os.remove(file_path)
            urllib.urlretrieve(url, file_path)

    def unzip_files(self):
        for file in self.files.keys():
            zip = ZipFile(self.data_dir + file)
            try:
                # FIXME: this is potentially dangerous, should check the
                #        zip does not use absolute paths or ..
                logging.info('Extracting ' + file)
                zip.extractall(self.data_dir)
            finally:
                zip.close()

    def all(self):
        """
        Downloads zip files from psp.cz, extracts them and imports into the
        dtabase.
        """
        self.download_files()
        self.unzip_files()
        logging.info('Starting import of the files...')
        import_all(self.data_dir)

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    parser = OptionParser()
    parser.add_option("-d", "--dir", dest="data_dir",
                      help="directory with psp.cz export files")

    (options, args) = parser.parse_args()
    if not options.data_dir:
        parser.error("Parameter --dir must be specified!")

    PspCzImport(options.data_dir).all()

if __name__ == '__main__':
    main()