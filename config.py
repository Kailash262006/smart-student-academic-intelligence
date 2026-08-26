SECRET_KEY = "super_secret_key"
DATABASE = "database.db"

# MySQL configuration (used for migration)
MYSQL_USER = "root"
MYSQL_PASSWORD = "Kg@2006"
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
# Using the same name as your SQLite file (without extension)
MYSQL_DB = "database"

from urllib.parse import quote_plus

SQLALCHEMY_DATABASE_URI = (
	f"mysql+pymysql://{MYSQL_USER}:{quote_plus(MYSQL_PASSWORD)}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)
