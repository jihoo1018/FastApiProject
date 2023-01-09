USERNAME = "root"
PASSWORD = "root"
HOSTNAME = "host.docker.internal" # "localhost"
DATABASE = "jjyudb"
PORT = 3306
CHARSET = "utf8"
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"