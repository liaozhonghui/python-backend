import os 

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:123456@192.168.160.120:5433/ai-db")