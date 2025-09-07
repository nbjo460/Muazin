from pymongo import MongoClient
from gridfs import GridFS

class DAL:
    def __init__(self):

        pass
    def upload_file(self, file_path):
        client = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB connection string
        db = client['your_database_name']  # Replace with your database name
        fs = GridFS(db)
        file_path = r'C:\Users\Menachem\Desktop\Galil\Muazin\data\podcasts\download (5).wav'  # Replace with the actual path to your WAV file
        file_name = 'audio.wav'  # Desired name for the file in GridFS

        with open(file_path, 'rb') as f:
            file_id = fs.put(f, filename=file_name, content_type='audio/wav')
            print(f"File '{file_name}' uploaded with ID: {file_id}")

d = DAL()
d.upload_file()