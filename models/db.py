# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

db = DAL("sqlite://storage.sqlite")

db.define_table("image",
    Field("title", unique=True),
    Field("file", "upload"),
    format = "%(title)s")

db.define_table("username",
    Field("user_name", unique=True))

db.define_table("comment",
    Field("author"),
    Field("body"),
    Field("date", "datetime"))

db.define_table("post",
    Field("title"),
    Field("body", "text"),
    Field("author", "reference username"),
    Field("date", "datetime"),
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
    Field("post", "list:reference post"),
    Field("club", "reference club"))

db.user.photo_id.requires = IS_IN_DB(db, db.image.id, "%(title)s")
db.user.photo_id.writable = db.user.photo_id.readable = False
