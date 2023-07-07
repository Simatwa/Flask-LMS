# Exam
# Irregularity
from core.models import db, application, event_listener
from datetime import datetime
from core.parents.models import Parent
from core.teachers.models import Subject, Stream, AcademicYear


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable=False)
    sname = db.Column(db.String(20), nullable=True)
    surname = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    year_of_birth = db.Column(db.Integer, nullable=False)
    admission_no = db.Column(db.Integer, nullable=False, unique=True)
    nemis_no = db.Column(db.String(10), nullable=True)  # Change to not-null
    email = db.Column(db.String(40), nullable=True)
    phone_no = db.Column(db.String(13), nullable=True)
    subjects = db.relationship(
        "Subject", secondary="student_subject", backref="students", lazy=True
    )
    Class = db.relationship("ClassStream", uselist=False, lazy=True)
    exams = db.relationship("Exam",uselist=True,lazy=True,backref="Student")
    fees_paid = db.Column(db.Numeric(10,2),default=0)
    fees_balance = db.Column(db.Numeric(10,2),default=0)
    payments = db.relationship("Payment",uselist=True,lazy=True, backref="Students")
    residence = db.Column(db.String(25), nullable=False)
    special_info = db.Column(db.Text, nullable=True)
    special_diet = db.Column(db.Boolean(), default=False)
    parents = db.relationship(
        "Parent", backref="students", secondary="student_parent", lazy=True
    )  # (parent) 1- M
    is_authenticated = db.Column(db.Boolean(), nullable=True)
    is_active = db.Column(db.Boolean(), nullable=True)
    is_anonymous = db.Column(db.Boolean(), nullable=True)
    password = db.Column(db.String(40), nullable=False, default="student")
    token = db.Column(db.String(8), nullable=True)
    last_modified = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    # classStream_rep = db.Column(db.ForeignKey("classstreams.id",onupdate="CASCADE",ondelete="SET NULL"))
    
    def __str__(self):
        return "{}. {}".format(self.admission_no, self.fullname)

    def __repr__(self):
        return "<Student %r>" % self.id

    def get_id(self):
        return "%r" % self.id

    @property
    def fullname(self):
        return f"{self.fname} {self.sname if self.sname else ''}"


class Class(db.Model):
    __tablename__ = "classes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=True, unique=True)
    class_lead = db.relationship(
        "Teacher",
        uselist=False,
        lazy=True,
    )
    streams = db.relationship(
        "Stream",
        secondary="classstreams",
        lazy=True,
    )
    academic_year = db.relationship("AcademicYear",lazy=True,uselist=False)
    school_fees = db.Column(db.Numeric(10,2),nullable=False)
    last_modified = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return "<Class %r>" % self.id

    def __str__(self):
        return self.name


class ClassStream(db.Model):
    """Identifies specific class e.g F1 Blue"""

    __tablename__ = "classstreams"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(
        db.Integer,
        db.ForeignKey("classes.id", onupdate="CASCADE", ondelete="SET NULL"),
        autoincrement=True,
    )
    stream_id = db.Column(
        db.Integer,
        db.ForeignKey("streams.id", onupdate="CASCADE", ondelete="SET NULL"),
        autoincrement=True,
    )
    stream_lead = db.relationship("Teacher", lazy=True, uselist=False)
    student_representative = db.relationship(
        "Student", uselist=False, lazy=True, overlaps="Class"
    )
    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id", onupdate="CASCADE", ondelete="SET NULL"),
        autoincrement=True,
    )
    Class = db.relationship(
        "Class", uselist=False, lazy=True, overlaps="streams"
    )  # backref="classstreams")
    Stream = db.relationship(
        "Stream", uselist=False, lazy=True, overlaps="streams"
    )  # backref="classstreams")

    def __repr__(self):
        return "<ClassStream %r>" % self.id

    def __str__(self):
        return "{} {}".format(self.Class, self.Stream)

class StudentParent(db.Model):
    """Relates student with parent M:M"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    parent_id = db.Column(db.Integer, db.ForeignKey("parents.id"))

    def __repr__(self):
        return "<StudentParent %r - %r>" % (self.student_id, self.parent_id)

    def __str__(self):
        return self.id


class StudentSubject(db.Model):
    """Relates student with a subject"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))

    def __repr__(self):
        return "<StudentSubject %r>" % self.id

    def __str__(self):
        return self.id

class Payment(db.Model):
	__tablename__="payments"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	transaction_code = db.Column(db.String(30),nullable=True)
	source = db.Column(db.String(40),nullable=False)
	amount = db.Column(db.Numeric(10,2),nullable=False)	
	mode = db.Column(db.String(8),nullable=False) # Bank or Cash
	incoming = db.Column(db.Boolean(),default=True)
	purpose = db.Column(db.String(20),default="School Fees")
	is_complete = db.Column(db.Boolean(),default=True)
	#received_by = To be done
	lastly_modified = db.Column(db.DateTime(),default=datetime.now,onupdate=datetime.now)
	created_at = db.Column(db.DateTime(),default=datetime.now)
	student_id = db.Column(db.Integer, db.ForeignKey("students.id",onupdate="CASCADE",ondelete="SET NULL",),autoincrement=True)
	
	def __repr__(self):
		return "<Payment %r>"%self.id
		
	def __str__(self):
		return "{}.{} - {}".format(self.id,self.source,self.amount)

class Exam(db.Model):
	__tablename__="exams"
	id = db.Column(db.Integer,autoincrement=True,primary_key=True)
	academic_period = db.relationship("AcademicYear",uselist=False,lazy=True)
	name = db.Column(db.String(30),nullable=True)
	student_id = db.Column(db.Integer,db.ForeignKey("students.id",onupdate="CASCADE",ondelete="SET NULL"),autoincrement=True)
	subject = db.relationship("Subject",uselist=False,lazy=True)
	#subject = db.Column(db.String(20),db.ForeignKey("students.subjects",onupdate="CADCADE",ondelete="SET NULL"))
	score = db.Column(db.Numeric(3,1),nullable=False)
	grade = db.Column(db.String(10),nullable=True)
	released = db.Column(db.Boolean(),default=False)
	lastly_modified = db.Column(db.DateTime(),default=datetime.utcnow,onupdate=datetime.utcnow)
	created_at = db.Column(db.DateTime(),default=datetime.utcnow)
	#subjects = 
	# To bee finished
	
	def __repr__(self):
		return "<Exam %r>"%self.id
		
	def __str__(self):
		return "{} {}".format(self.academic_period,self.name)
	
# Event listeners

class LocalEventListener:
	
	@staticmethod
	def update_fee_records(mapper, connection, target):
		"""Updates fee balance, """
		try:
			fees_to_pay = target.Class.Class.school_fees
		except Exception as e:
			raise Exception("Class cannot be null!")
		total_paid_current_year = 0
		current_year = datetime.now().year
		for payment in target.payments:
			if payment.created_at.year == current_year and payment.is_complete:
				total_paid_current_year += payment.amount
		target.fees_paid = total_paid_current_year
		target.fees_balance = fees_to_pay - total_paid_current_year
		
# db.event.listen(Student,"before_insert",event_listener.insert_admission_number)
db.event.listen(Student, "before_insert", event_listener.insert_age)
db.event.listen(Student, "before_insert", event_listener.insert_password)
db.event.listen(Student, "before_insert", LocalEventListener.update_fee_records)
db.event.listen(Student, "before_update", LocalEventListener.update_fee_records)