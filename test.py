class MicroBlogModelView(sqla.ModelView):

    def is_accessible(self):

    return login.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs): {comment : redirect to login page if user doesn't have access} return redirect(url_for('login', next=request.url))` You can replace the code under the is_accessible function with

    return current_user.is_admin 