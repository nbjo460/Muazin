from pymongo import MongoClient
from gridfs import GridFSBucket, errors
from pathlib import Path

from src.exceptions.exception import NoMongoConnection
from src.utils.config import MongoDBConfig
from src.utils.logger import Logger


class DAL:
    def __init__(self):
        self.logger = Logger().get_logger()
        self.db = None
        self.fs = None
        self._set_gridfs()

    def _set_gridfs(self):
        db_name = MongoDBConfig.MONGO_DB_NAME
        try:
            client = self._set_client()
            self.db = client[db_name]
            self.fs = GridFSBucket(self.db)
        except NoMongoConnection as e:
            pass

    def _set_client(self):
        self.logger.info("Connecting to MongoDB")
        try:
            uri = self._get_uri()
            client =  MongoClient(uri)
            client.admin.command("ping")
            self.logger.info("Connection work.")
            return client
        except Exception as e:
            self.logger.warning("Connection FAILED!!!")
            raise NoMongoConnection()

    @staticmethod
    def _get_uri() -> str:
        """
        Build an URI string with by check if is an atlas mongo.
        And by check if user&pass exists, or not.
        :return: URI of mongo.
        """
        user_name = MongoDBConfig.MONGO_USER_NAME
        password = MongoDBConfig.MONGO_PASSWORD

        host = MongoDBConfig.MONGO_HOST
        port= MongoDBConfig.MONGO_PORT
        prefix = f"{MongoDBConfig.MONGO_PREFIX}://"
        if  user_name and password:
            return f"{prefix}{user_name}:{password}@{host}:{port}"
        else:
            return f"{prefix}{host}:{port}"

    def upload_file(self, file_path, _id):
        file_name = Path(file_path).name
        try:
            self.logger.info(f"Uploading {file_name}")
            with open(file_path, 'rb') as file:
                with self.fs.open_upload_stream_with_id(_id, filename=file_name) as fs_stream:
                    fs_stream.write(file)
            self.logger.info(f"Uploaded {file_name}")
        except errors.FileExists:
            self.logger.warning(f"FILE {file_name} ALREADY EXISTS, NOT UPLOADED AGAIN")


# if __name__ == "__main__":
#     dal = DAL()
#     dal.upload_file(r"C:\Users\Menachem\Desktop\Galil\Muazin\data\podcasts\download (6).wav", "5d41402abc4b2a76b9719d911017c592")
