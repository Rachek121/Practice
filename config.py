import os


DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'pc_club.db')}"