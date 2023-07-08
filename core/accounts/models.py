from core.models import db, add_user_variables, event_listener
		
@add_user_variables()
class SchoolAdmin(db.Model):
	"""App admins"""
	__tablename__="admins"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	fname = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(30), nullable=False, unique=True)
	is_admin = db.Column(db.Boolean(),default=True)
	
	def __repr__(self):
		return "<Admin %r>"%self.id
	
	def __str__(self):
		return "{}. {}".format(self.id, self.fname)	
		
db.event.listen(SchoolAdmin, "before_insert", event_listener.rename_user_profile)
db.event.listen(SchoolAdmin, "before_update", event_listener.rename_user_profile)

db.event.listen(SchoolAdmin, "before_insert", event_listener.hash_password)
db.event.listen(SchoolAdmin, "before_update", event_listener.hash_password)

db.event.listen(SchoolAdmin, "before_delete", event_listener.delete_user_profile)