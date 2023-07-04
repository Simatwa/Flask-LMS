from ..models import db
from ..app import application


class Parents(db.Model):
    __tablename__ = "parents"
    id = db.Column(db.Integer, primary_key=True)
    students_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", onupdate="CASCADE", ondelete="SET NULL"),
        name="unique_user_id",
        primary_key=True,
        default="users.id",
    )
    student = db.relationship(
        "User", backref=db.backref("parents", passive_deletes=True), lazy=True
    )

    def __repr__(self):
        return "%d" % self.id

    def __unicode__(self):
        return "%d" % self.id


with application.app_context():
    db.create_all()
