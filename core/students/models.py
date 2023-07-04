# Exam
# Irregularity
from ..models import db, application


class Exam(db.Model):
    __tablename__ = "exams"
    id = db.Column(
        db.Integer,
        primary_key=True,
        default="users.id",
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", onupdate="CASCADE", ondelete="SET NULL"),
        primary_key=True,
        name="unique_users",
    )
    form = db.Column(db.Integer)
    stream = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer)
    term = db.Column(db.Integer)
    maths = db.Column(db.Integer, nullable=False)
    english = db.Column(db.Integer, nullable=False)
    kiswahili = db.Column(db.Integer, nullable=False)
    biology = db.Column(db.Integer, nullable=False)
    chemistry = db.Column(db.Integer, nullable=False)
    physics = db.Column(db.Integer)
    agriculture = db.Column(db.Integer)
    business_studies = db.Column(db.Integer)
    computer_studies = db.Column(db.Integer)
    geography = db.Column(db.Integer)
    cre = db.Column(db.Integer)
    history_and_government = db.Column(db.Integer)
    grade = db.Column(db.String(2), nullable=True)
    class_teacher_remark = db.Column(db.String(300), nullable=True)
    student = db.relationship(
        "User", backref=db.backref("exams", passive_deletes=True), lazy=True
    )

    def __unicode__(self):
        return self.student

    def __repr__(self):
        return "%r" % self.student


with application.app_context():
    db.create_all()
