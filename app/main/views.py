from . import main
from flask import render_template
from ..requests import get_random_quote
from ..models import User,Post,Comment

@main.route('/')
def index():
    quote = get_random_quote()
    
    return render_template('index.html',quote=quote)

@main.route('/blogs')
def blogs():
    posts = Post.query.all()
    
    return render_template('blogs.html',posts=posts)
    
    