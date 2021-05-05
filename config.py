import os


class Config(object):
    """
    Class to contain the configuration values
    """
    server = 'ensembldb.ensembl.org'
    port = '3306'
    db_name = 'ensembl_website_102'
    username = 'anonymous'
    password = ''
    db_uri = 'mysql+pymysql://{username}:{password}@{server}:{port}/{db}'.format(
        username=username, password=password, server=server, port=port, db=db_name)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False
