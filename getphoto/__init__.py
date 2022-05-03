__app_name__ = 'getphoto'
__version__ = '0.1.0'
__author__ = 'Alexei Ovsiannikov'
__year__ = '2022'

(SUCCESS, DIR_ERROR, FILE_ERROR, DB_CONNECT_ERROR, DB_WRITE_ERROR, DB_READ_ERROR, FILE_SAVED, NO_PHOTO_ID, NO_ID) = range(9)
ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config_file_error",
    DB_CONNECT_ERROR: "database connect error",
    DB_WRITE_ERROR: "database write error",
    DB_READ_ERROR: "database read error",
    NO_PHOTO_ID: 'There is no photo for the item with this ID in the technical data table',
          NO_ID: 'There is no item with this ID in the technical data table'}
