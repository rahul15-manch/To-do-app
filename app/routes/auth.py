from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

# Dummy credentials (for testing)
USER_CREDENTIALS = {
    'username': 'admin',
    'password': '1234'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username.strip() == USER_CREDENTIALS['username'] and password.strip() == USER_CREDENTIALS['password']:
            session['user_id'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('task_bp.view_tasks'))  # ✅ This should match your route function name
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
