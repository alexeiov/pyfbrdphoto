from typing import Optional
import typer
from getphoto import getphoto_proc
from getphoto import config

from getphoto import __app_name__, __version__, __author__, __year__

app = typer.Typer()
dbp = ''

gh = getphoto_proc.PhotoGetter()


@app.command(name='get-list')
def get_photos_list(db_path: str = typer.Option(config.DEFAULT_DB,
                                                '--db-path',
                                                prompt='Please enter full path to database '
                                                             'in DBMaster format or use default')) -> None:
    """Указать путь к базе проекта и получить список фото"""
    # print('Указать путь к базе проекта и получить список активов с фотографиями')
    gh.db_path = db_path
    gh.get_photos_list()
    # print('Use "getphoto.exe --help" to get commands list')
    # input('Press any key to close ...')


@app.command(name='get-photo')
def get_db_path(db_path: str = typer.Option(config.DEFAULT_DB,
                                            '--db-path',
                                            prompt='Please enter full path to database '
                                                         'in DBMaster format or use default')) -> None:
    """Указать путь к базе проекта и выгрузить фото"""
    # print('Указать путь к базе проекта и сохранить фотографию')
    gh.db_path = db_path
    gh.get_photo()
    print('Use "getphoto.exe --help" to get commands list')
    # input('Press any key to close ...')


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f'{__app_name__} v{__version__} by {__app_name__}. {__year__}')
        raise typer.Exit()


@app.callback()
def main(version: Optional[bool] = typer.Option(None, "--version", "-v",
                                                help="Show the application version and exit.",
                                                callback=_version_callback,
                                                is_eager=True)) -> None:
    return
