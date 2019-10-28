from . import main
from flask import render_template,redirect,url_for,request
from ..requests import get_random_quote
from ..models import User,Post,Comment
from flask_login import login_required,current_user
from ..import db
from .forms import BlogForm


@main.route('/')
def index():
    quote = get_random_quote()
    
    return render_template('index.html',quote=quote)

@main.route('/blogs')
def blogs():
    posts = Post.query.all()
    
    return render_template('blogs.html',posts=posts)
    
@main.route('/blogs/new', methods=["GET","POST"])
@login_required
def new_blog():
    '''
    view function that returns the blog form
    '''
    form = BlogForm()
    if form.validate_on_submit():
        post = form.post.data
        title = form.title.data
        
        new_post = Post(title=title,body=post,user=current_user)
        new_post.save_post()
        return redirect(url_for('.blogs'))
    
    title='blogs'
    return render_template('new_blog.html',title=title,blog_form=form)

@main.route('/comments/new', methods=["GET","POST"])

    