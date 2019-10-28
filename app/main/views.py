from . import main
from flask import render_template,redirect,url_for,request
from ..requests import get_random_quote
from ..models import User,Post,Comment
from flask_login import login_required,current_user
from ..import db
from .forms import BlogForm,CommentsForm


@main.route('/')
def index():
    quote = get_random_quote()
    
    return render_template('index.html',quote=quote)

@main.route('/blogs')
def blogs():
    posts = Post.query.all()
    
    return render_template('blogs.html',posts=posts)
    
@main.route('/blogs/new/', methods=["GET","POST"])
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

@main.route('/comments/new/<int:id>', methods=["GET","POST"])
@login_required
def comment(id):
    '''
    view function that returns a form to insert a comment on a post
    '''
    
    form = CommentsForm()
    post = Post.query.filter_by(id=id).first()
     
    if form.validate_on_submit():
        comment =  form.comment.data
        new_comment = Comment(post_id = post.id, comment_post=comment,user=current_user)
        new_comment.save_comments()
        
        return redirect(url_for('.comments'))
    
    return render_template('new_comment.html',comment_form=form,post=post)


@main.route('/comments/<int:id>')
def comments(id):
    post = Post.query.get(id)
    comment = Comment.get_comments(post.id)
    return render_template('comments.html', comment = comment,post=post)