from core.models import db
from core.app import application
from flask import url_for
from datetime import datetime
from os import remove, path, getcwd
import logging


class UserImage(db.Model):
    __tablename__ = "user_images"
    id = db.Column(db.Integer, primary_key=True, default="users.id")
    name = db.Column(db.String(30), default="default")
    path = db.Column(db.String(80), default="default_profile.png")
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", onupdate="CASCADE", ondelete="SET NULL"),
        primary_key=True,
    )
    profile = db.relationship(
        "User", backref=db.backref("profile", passive_deletes=True), lazy=True
    )

    def __repr__(self):
        return "%r" % self.id

    def __unicode__(self):
        return self.name


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(40), nullable=False)
    sname = db.Column(db.String(40), default="")
    email = db.Column(db.String(40), nullable=False, unique=True)
    gender = db.Column(
        db.String(10),
        nullable=False,
    )
    index_no = db.Column(db.Integer, unique=True, nullable=True)
    phone_no = db.Column(
        db.String(13), unique=True, nullable=True, name="unique_users_phone_no"
    )
    password = db.Column(db.String(64), nullable=False)
    is_student = db.Column(db.Boolean(), default=False)
    is_teacher = db.Column(db.Boolean(), default=False)
    is_parent = db.Column(db.Boolean(), default=False)
    is_stakeholder = db.Column(db.Boolean(), default=False)
    is_admin = db.Column(db.Boolean(), default=False)
    is_authenticated = db.Column(db.Boolean(), default=False)
    is_anonymous = db.Column(db.Boolean(), default=True)
    is_active = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    last_updated = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow
    )
    token = db.Column(db.String(8), nullable=True)

    def __repr__(self):
        return "%s" % self.fullname

    def __unicode__(self):
        return self.fullname

    def get_id(self):
        return "%r" % self.id

    @property
    def fullname(self):
        return "%s %s" % (self.fname, self.sname)


class UserProfileManager:
    @staticmethod
    def delete_user_image(mapper, connection, user):
        try:
            remove(path.join(getcwd(), url_for("static", filename=user.path)))
        except Exception as e:
            logging.error(f"Failed to delete user profile {user.path} - {e.args}")

    @staticmethod
    def update_user_image(mapper, connection, user):
        # Not necessay currently:
        # Let the fullpath handled at upload
        # user.path = path.join("image/profiles",user.path)
        # db.session.commit()
        pass


# db.event.listen(UserImage,"after_update",UserProfileManager.update_user_image)
# db.event.listen(UserImage,"after_insert",UserProfileManager.update_user_image)
db.event.listen(UserImage, "before_delete", UserProfileManager.delete_user_image)
"""
	new_user = User(fname="Caleb",email="email@gmail.com",)
	new_image = UserImage(id=1)
	new_user.profile.insert(0,new_image)
	db.session.add(new_user)
	db.session.commit()
	user = User.query.filter_by(id=1).first()
	print(user.profile[0].path)
"""
