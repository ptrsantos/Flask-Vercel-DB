import os

class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://Flask-Vercel-DB_owner:npg_nY7Uzrk8jpJW@ep-royal-pine-acra8qhx-pooler.sa-east-1.aws.neon.tech/Flask-Vercel-DB?sslmode=require')
    SQLALCHEMY_DATABASE_URI = 'postgresql://Flask-Vercel-DB_owner:npg_nY7Uzrk8jpJW@ep-royal-pine-acra8qhx-pooler.sa-east-1.aws.neon.tech/Flask-Vercel-DB?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # or another method to set a secret key
