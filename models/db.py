# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

db = DAL("sqlite://storage.sqlite")

from gluon.tools import *
auth = Auth(db)
auth.define_tables(username=True)

db.define_table("image",
    Field("title", unique=True),
    Field("file", "upload"),
    format = "%(title)s")

db.define_table("username",
    Field("user_name", unique=True))

db.define_table("comment",
    Field("post_id", "reference blogpost"),
    Field("body"),
    Field("created_on", "datetime", default=request.now),
    Field("created_by", "reference auth_user", default=auth.user_id))

db.define_table("blogpost",
    Field("title"),
    Field("body", "text"),
    Field("created_by", "reference username"),
    Field("created_on", "datetime", default=request.now),
    Field("comments", "list:reference comment"),
    Field("tags", "list:string"))

db.define_table("club",
    Field("name", unique=True),
    Field("city", unique=True),
    Field("state"))

db.define_table("user",
    Field("first_name"),
    Field("last_name"),
    Field("username", "reference username"),
    Field("email", unique=True),
    Field("photo_id", "reference image"),
    Field("blogpost", "list:reference blogpost"),
    Field("club", "reference club"))

db.define_table('document',
    Field('blogpost_id', 'reference blogpost'),
    Field('name'),
    Field('file', 'upload'),
    Field('created_on', 'datetime', default=request.now),
    Field('created_by', 'reference auth_user', default=auth.user_id),
    format='%(name)s')

db.user.first_name.requires = IS_NOT_EMPTY()
db.user.last_name.requires = IS_NOT_EMPTY()
db.user.email.requires = IS_NOT_EMPTY()
db.user.photo_id.requires = IS_IN_DB(db, db.image.id, "%(title)s")
db.user.photo_id.writable = db.user.photo_id.readable = False

db.blogpost.title.requires = IS_NOT_IN_DB(db, 'page.title')
db.blogpost.body.requires = IS_NOT_EMPTY()
db.blogpost.created_by.readable = db.blogpost.created_by.writable = False
db.blogpost.created_on.readable = db.blogpost.created_on.writable = False

db.comment.body.requires = IS_NOT_EMPTY()
db.comment.post_id.readable = db.comment.post_id.writable = False
db.comment.created_by.readable = db.comment.created_by.writable = False
db.comment.created_on.readable = db.comment.created_on.writable = False

db.document.name.requires = IS_NOT_IN_DB(db, 'document.name')
db.document.page_id.readable = db.document.page_id.writable = False
db.document.created_by.readable = db.document.created_by.writable = False
db.document.created_on.readable = db.document.created_on.writable = False
