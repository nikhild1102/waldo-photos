from app import db
import enum,datetime
from sqlalchemy.dialects.postgresql import UUID

class Photo_Status(enum.Enum):
  Pending = 'pending'
  Processing = 'processing'
  Failed = 'failed'
  Completed = 'completed'

class Photos(db.Model):
  uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
  url= db.Column(db.String, nullable=False)
  status = db.Column(db.Enum(Photo_Status), nullable=False, default='pending')
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Photo_Thumbnails(db.Model):
  uuid= db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
  photo_uuid= db.Column(UUID(as_uuid=True), db.ForeignKey('photos.uuid'), nullable=False)
  width= db.Column(db.Integer, nullable=False)
  height= db.Column(db.Integer, nullable=False)
  url= db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
  
if __name__ == '__main__':
  db.create_all()
