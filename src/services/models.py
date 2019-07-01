from app import db
import enum,datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

class Photo_Status(enum.Enum):
  pending = 'pending'
  processing = 'processing'
  failed = 'failed'
  completed = 'completed'

class Photos(db.Model):
  uuid = db.Column(UUID(as_uuid=True), unique=True, default=uuid4, primary_key=True)
  url= db.Column(db.String, nullable=False)
  status = db.Column(db.Enum(Photo_Status), nullable=False, default='pending')
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class PhotoThumbnails(db.Model):
  uuid= db.Column(UUID(as_uuid=True), unique=True, default=uuid4, primary_key=True)
  photo_uuid= db.Column(UUID(as_uuid=True), db.ForeignKey('photos.uuid'), nullable=False)
  width= db.Column(db.Integer, nullable=False)
  height= db.Column(db.Integer, nullable=False)
  url= db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
  
if __name__ == '__main__':
  db.drop_all(bind=None)
  db.session.commit()
  db.create_all()
  
  photo1 = Photos(url='https://s3.amazonaws.com/waldo-thumbs-dev/large/71840919-e422-552d-8c8d-9b2b360ce98c.jpg')
  photo2 = Photos(url='https://s3.amazonaws.com/waldo-thumbs-dev/large/72800f95-c406-5475-85ac-b8943877b15f.jpg')
  photo3 = Photos(url='https://s3.amazonaws.com/waldo-thumbs-dev/large/366ad885-aafd-48a4-8ff5-c38a1bbc84c8.jpg')
  photo4 = Photos(url='https://s3.amazonaws.com/waldo-thumbs-dev/large/b3cbaef4-ff6d-523e-beea-704629c42ca2.jpg')
  photo5 = Photos(url='https://s3.amazonaws.com/waldo-thumbs-dev/large/49dd12b2-f019-59c5-bf17-b1b3bb208eba.jpg')
  photo6 = Photos(url='https://s3.amazonaws.com/waldo-thumbs-dev/large/c9391205-1892-5139-abe5-b5df3ced8d61.jpg')
  
  photo_array = [photo1,photo2,photo3,photo4,photo5,photo6]
  db.session.bulk_save_objects(photo_array)
  db.session.commit()
