# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    # index should list all of the available users
  images = db(db.image).select()
  posts = db(db.post).select()
  users = db(db.user).select()
  comments = db(db.comment).select()
  form = SQLFORM(db.image).process()
  return dict(images=images, users=users, posts=posts, comments=comments)

def create():
    #add a new blog post

def show():
    #show a users blog and its comments, and add new comments

def edit():
    #edit an existing blog

def documents():
    #manage the blog entries attached to the page

def search():
    #display a search box and, via an ajax callback, return all matching titles as the user types

def callback():
    # this is the ajax callback function. It returns the html that gets embeded in the search page
    # while the visitor types

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

@auth.requires_membership('manager')
def manage():
    grid = SQLFORM.smartgrid(db.image, linked_tables=["user"])
    return dict(grid=grid)
