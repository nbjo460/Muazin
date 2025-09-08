from pymongo import MongoClient
from gridfs import GridFSBucket, errors
from pathlib import Path
from src.utils.config import MongoDBConfig

class DAL:
    def __init__(self):
        db_name = MongoDBConfig.DB_NAME
        client = self._set_client()
        self.db = client[db_name]
        self.fs = GridFSBucket(self.db)

    def _set_client(self):
        uri = self._get_uri()
        return MongoClient(uri)

    @staticmethod
    def _get_uri() -> str:
        """
        Build an URI string with by check if is an atlas mongo.
        And by check if user&pass exists, or not.
        :return: URI of mongo.
        """
        user_name = MongoDBConfig.USER_NAME
        password = MongoDBConfig.PASSWORD

        host = MongoDBConfig.HOST
        port= MongoDBConfig.PORT
        prefix = f"{MongoDBConfig.PREFIX}://"
        if  user_name and password:
            return f"{prefix}{user_name}:{password}@{host}:{port}"
        else:
            return f"{prefix}{host}:{port}"

    def upload_file(self, file_path, _id):
        file_name = Path(file_path).name
        try:
            with open(file_path, 'rb') as file:
                with self.fs.open_upload_stream_with_id(_id, filename=file_name) as fs_stream:
                    fs_stream.write(file)
        except errors.FileExists:
            print("FILE ALREADY EXISTS, NOT UPLOADED AGAIN")

# if __name__ == "__main__":
#     dal = DAL()
#     dal.upload_file(r"C:\Users\Menachem\Desktop\Galil\Muazin\data\podcasts\download (6).wav", "5d41402abc4b2a76b9719d911017c592")
