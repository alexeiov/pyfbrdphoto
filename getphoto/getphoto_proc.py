import csv
from pathlib import Path
from getphoto import db_connect
from getphoto import config
import datetime


class PhotoGetter:
    def __init__(self, db_path=None) -> None:
        self.db_path = db_path

    def get_photo(self):
        # c = db_connect.db_connect(self.db_path)
        # cur = c.cursor()

        cur = db_connect.db_connect(self.db_path)[1]

        id_mt = int(input('Enter Main Tab ID:'))
        save_path = input('Enter save path: ')

        blob_statement = cur.prep(config.BLOB_GET_PHOTO)
        cur.execute(blob_statement, (id_mt,))
        data_f = cur.fetchone()

        try:
            pic = data_f[0].read()
            asset_name = data_f[2].replace('\\', '_').replace('/', '_')
            pic_name = Path(save_path).joinpath(f'{data_f[1]}_-_{asset_name}.jpg')

            with open(pic_name, 'wb') as d_f:
                d_f.write(pic)
            print(f'Photo saved to the folder {save_path}')
        except AttributeError:
            print("Error: There is no photo for the item with this ID in the technical data table")
        except TypeError:
            print("Error: There is no item with this ID in the technical data table")
        except (FileNotFoundError, OSError):
            print('Error: can not process asset name')

        db_connect.db_connect(self.db_path)[0].commit()
        db_connect.db_connect(self.db_path)[0].close()

    def get_photos_list(self):
        save_path_l = input('Enter save path: ')
        time_l = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        pos = self.db_path.rfind('\\')
        db_name = self.db_path[pos+1:-4]
        list_name = Path(save_path_l).joinpath(f'{db_name}_photos_list_{time_l}.csv')

        cur = db_connect.db_connect(self.db_path)[1]
        list_statement = cur.prep(config.GET_PHOTO_LIST)
        cur.execute(list_statement)
        list_d = cur.fetchall()

        with open(list_name, 'w', newline='') as data_f:
            fieldnames = ['id_main_tab', 'inv', 'subdiv_name', 'name']
            writer = csv.writer(data_f, delimiter=';')
            writer.writerow(fieldnames)
            for line in list_d:
                writer.writerow(line)

        print(f'File with photos list saved: {list_name}')

