from core.models import db
from core.app import application
from core.models import event_listener
from datetime import datetime


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    sname = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(1), nullable=False)
    id_no = db.Column(db.Integer, nullable=False)
    tsc_no = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(30), nullable=False)
    phone_no = db.Column(db.String(13), nullable=False)
    county = db.Column(db.String(15), nullable=False)
    year_of_birth = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    subjects = db.relationship(
        "Subject", secondary="teacher_subject", backref="teachers", lazy=True
    )
    salary = db.Column(db.Numeric(10, 2), nullable=False)
    residence = db.Column(db.String(25), nullable=False)
    special_info = db.Column(db.Text, nullable=True)
    bom = db.Column(db.Boolean(), default=False)
    is_parent = db.Column(db.Boolean(), default=False)
    is_admin = db.Column(db.Boolean(), default=False)
    is_authenticated = db.Column(db.Boolean(), nullable=True)
    is_active = db.Column(db.Boolean(), nullable=True)
    is_anonymous = db.Column(db.Boolean(), nullable=True)
    password = db.Column(db.String(40), nullable=False, default="teachers")
    token = db.Column(db.String(8), nullable=True)
    lastly_modified = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    stream_id = db.Column(
        db.Integer,
        db.ForeignKey("streams.id", onupdate="CASCADE", ondelete="SET NULL"),
        autoincrement=True,
    )
    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id", onupdate="CASCADE", ondelete="SET NULL"),
        autoincrement=True,
    )
    class_id = db.Column(
        db.Integer,
        db.ForeignKey("classes.id", onupdate="CASCADE", ondelete="SET NULL"),
        autoincrement=True,
    )
    classstreams_id = db.Column(
        db.Integer,
        db.ForeignKey("classstreams.id", onupdate="CASCADE", ondelete="SET NULL"),
        autoincrement=True,
    )
    activity_id = db.Column(db.Integer,db.ForeignKey("activities.id",onupdate="CASCADE",ondelete="SET NULL"),autoincrement=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id",onupdate="CASCADE",ondelete="SET NULL"),autoincrement=True)
    
    def __repr__(self):
        return "<Teacher %r>" % self.id

    def __str__(self):
        return self.fullname

    def get_id(self):
        return "%r" % self.id

    @property
    def fullname(self):
        return f"{self.fname} {self.sname if self.sname else ''}"


class Subject(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    subject_lead = db.relationship("Teacher", lazy=True, uselist=False)
    lastly_modified = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # db.Column(db.String(40),db.ForeignKey("teachers.fname"))
    exam_id = db.Column(db.Integer, db.ForeignKey("exams.id",onupdate="CASCADE",ondelete="SET NULL"))
    
    def __repr__(self):
        return "<Subject %s>" % self.name

    def __str__(self):
        return self.name


class Stream(db.Model):
    __tablename__ = "streams"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    streams_lead = db.relationship("Teacher", uselist=False, lazy=True)
    lastly_modified = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # classStream_id= db.Column(db.Integer,db.ForeignKey("classstreams.id", onupdate="CASCADE",ondelete="SET NULL"),autoincrement=True)

    def __repr__(self):
        return "<Stream %r>" % self.id

    def __str__(self):
        return self.name


class TeacherSubject(db.Model):
    """Links teachers with subjects"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))


class AcademicYear(db.Model):
	"""Academic year """
	# Register in admin
	__tablename__="academicyears"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	year = db.Column(db.Integer,nullable=False,default=datetime.now().year)
	term = db.Column(db.Integer,nullable=False)
	created_at = db.Column(db.DateTime(), default=datetime.utcnow)
	class_id = db.Column(db.Integer,db.ForeignKey("classes.id",ondelete="SET NULL", onupdate="CASCADE",name="class_id"),autoincrement=True)
	exam_id = db.Column(db.Integer,db.ForeignKey("exams.id",ondelete="SET NULL",onupdate="CASCADE"))
	
	def __repr__(self):
		return "<AcademicYear %r>"%self.year
	
	def __str__(self):
		return "{}/{}".format(self.year,self.term)

class Activity(db.Model):
	"""School activities"""
	__tablename__="activities"
	id = db.Column(db.Integer, autoincrement=True,primary_key=True)
	title = db.Column(db.String(20),nullable=False)
	department = db.relationship("Department",lazy=True,uselist=True,backref="activities")
	date = db.Column(db.Date(),nullable=False)
	time = db.Column(db.Time(),nullable=False)
	leads = db.relationship("Teacher",lazy=True,uselist=True,backref="activities")
	detail = db.Column(db.Text)
	duration = db.Column(db.String(20),nullable=True)
	location = db.Column(db.String(20),default="School")
	expenditure = db.Column(db.Numeric(10,2),default=0)
	notify_supervisor = db.Column(db.Boolean(),default=False)
	is_over = db.Column(db.Boolean(),default=False)
	# Add event listener that will send the message to Supervisor
	lastly_updated = db.Column(db.DateTime(),default=datetime.utcnow,onupdate=datetime.utcnow)
	created_at = db.Column(db.DateTime(),default=datetime.utcnow)
	
	def __repr__(self):
		return "<Activity %r>"%self.id
	
	def __str__(self):
		return "{}. {}".format(self.id,self.title)

class Department(db.Model):
	"""School departments"""
	__tablename__="departments"
	id = db.Column(db.Integer, autoincrement=True,primary_key=True)
	name = db.Column(db.String(20),nullable=False,unique=True)
	lead = db.relationship("Teacher",lazy=True,uselist=False)
	objectives = db.Column(db.Text,)
	activity_id = db.Column(db.ForeignKey("activities.id",onupdate="CASCADE",ondelete="SET NULL"),autoincrement=True)
	lastly_modified = db.Column(db.DateTime(),default=datetime.utcnow, onupdate=datetime.utcnow)
	created_at = db.Column(db.DateTime(),default=datetime.utcnow)
	
	def __repr__(self):
		return "<Department %r>"%self.id
		
	def __str__(self):
		return self.name
		
db.event.listen(Teacher, "before_insert", event_listener.insert_age)
