from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import smtplib
from email.mime.text import MIMEText
from database import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = 'super_secret_dev_key'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max limit

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize DB if it doesn't exist
if not os.path.exists('recruitment.db'):
    init_db()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_email(to_email, subject, body):
    # Simulated email sending for development
    print(f"--- EMAIL SIMULATION ---")
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print(f"Message:\n{body}")
    print(f"------------------------")

# --- Authentication Helpers ---
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in first.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        role = request.form['role']

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)',
                         (name, email, hashed_password, role))
            conn.commit()
            flash("Registration successful! Please login.", "success")
            return redirect(url_for('login'))
        except conn.IntegrityError:
            flash("Email already registered.", "danger")
        finally:
            conn.close()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['role'] = user['role']
            session['name'] = user['name']
            
            flash(f"Welcome back, {user['name']}!", "success")
            if user['role'] == 'employer':
                return redirect(url_for('employer_dashboard'))
            else:
                return redirect(url_for('seeker_dashboard'))
        else:
            flash("Invalid email or password.", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('index'))

# ================= EMPLOYER ROUTES =================

@app.route('/employer/dashboard')
@login_required
def employer_dashboard():
    if session.get('role') != 'employer':
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    jobs = conn.execute('SELECT * FROM jobs WHERE employer_id = ? ORDER BY id DESC', (session['user_id'],)).fetchall()
    conn.close()
    return render_template('employer/dashboard.html', jobs=jobs)

@app.route('/employer/post_job', methods=['GET', 'POST'])
@login_required
def post_job():
    if session.get('role') != 'employer':
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        title = request.form['title']
        company = request.form['company']
        category = request.form['category']
        skills = request.form['skills']
        experience = request.form['experience']
        salary = request.form['salary']
        location = request.form['location']
        description = request.form['description']
        last_date = request.form['last_date']
        
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO jobs (title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, company, category, skills, experience, salary, location, description, last_date, session['user_id']))
        conn.commit()
        conn.close()
        
        flash("Job posted successfully!", "success")
        return redirect(url_for('employer_dashboard'))
        
    return render_template('employer/post_job.html')

@app.route('/employer/job/<int:job_id>/applicants')
@login_required
def view_applicants(job_id):
    if session.get('role') != 'employer':
        return redirect(url_for('index'))
        
    conn = get_db_connection()
    # verify job belongs to this employer
    job = conn.execute('SELECT * FROM jobs WHERE id = ? AND employer_id = ?', (job_id, session['user_id'])).fetchone()
    if not job:
        conn.close()
        flash("Job not found or unauthorized.", "danger")
        return redirect(url_for('employer_dashboard'))
        
    apps = conn.execute('''
        SELECT a.id as app_id, u.name, u.email, sp.skills, sp.education, a.resume, a.status, a.applied_date
        FROM applications a
        JOIN users u ON a.seeker_id = u.id
        LEFT JOIN seeker_profiles sp ON u.id = sp.user_id
        WHERE a.job_id = ?
        ORDER BY a.applied_date DESC
    ''', (job_id,)).fetchall()
    conn.close()
    
    return render_template('employer/view_applicants.html', applicants=apps, job=job)

@app.route('/employer/application/<int:app_id>/update', methods=['POST'])
@login_required
def update_application(app_id):
    if session.get('role') != 'employer':
        return redirect(url_for('index'))
        
    status = request.form.get('status')
    if status not in ['Accepted', 'Rejected']:
        flash("Invalid status update.", "danger")
        return redirect(request.referrer)
        
    conn = get_db_connection()
    app_data = conn.execute('''
        SELECT a.*, u.email, u.name as seeker_name, j.title as job_title, j.company 
        FROM applications a 
        JOIN users u ON a.seeker_id = u.id 
        JOIN jobs j ON a.job_id = j.id
        WHERE a.id = ? AND j.employer_id = ?
    ''', (app_id, session['user_id'])).fetchone()
    
    if app_data:
        conn.execute('UPDATE applications SET status = ? WHERE id = ?', (status, app_id))
        conn.commit()
        
        # Send Email Notification
        subject = f"Application Update: {app_data['job_title']} at {app_data['company']}"
        if status == 'Accepted':
            body = f"Dear {app_data['seeker_name']},\n\nCongratulations! You have been selected for the interview for the {app_data['job_title']} position at {app_data['company']}."
        else:
            body = f"Dear {app_data['seeker_name']},\n\nThank you for applying for the {app_data['job_title']} position at {app_data['company']}. We regret to inform you that you were not selected for this position."
            
        send_email(app_data['email'], subject, body)
        flash(f"Application {status.lower()} and email sent to applicant.", "success")
    
    conn.close()
    return redirect(request.referrer)


# ================= JOB SEEKER ROUTES =================

@app.route('/seeker/dashboard')
@login_required
def seeker_dashboard():
    if session.get('role') != 'seeker':
        return redirect(url_for('index'))
        
    query = request.args.get('q', '')
    location = request.args.get('location', '')
    
    conn = get_db_connection()
    sql = 'SELECT * FROM jobs WHERE 1=1'
    params = []
    
    if query:
        sql += ' AND (title LIKE ? OR company LIKE ? OR category LIKE ? OR skills LIKE ?)'
        like_query = f'%{query}%'
        params.extend([like_query, like_query, like_query, like_query])
    if location:
        sql += ' AND location LIKE ?'
        params.append(f'%{location}%')
        
    sql += ' ORDER BY id DESC'
    jobs = conn.execute(sql, params).fetchall()
    conn.close()
    
    return render_template('seeker/dashboard.html', jobs=jobs, query=query, location=location)

@app.route('/seeker/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if session.get('role') != 'seeker':
        return redirect(url_for('index'))
        
    conn = get_db_connection()
    
    if request.method == 'POST':
        phone = request.form.get('phone', '')
        address = request.form.get('address', '')
        skills = request.form.get('skills', '')
        education = request.form.get('education', '')
        experience = request.form.get('experience', '')
        
        existing = conn.execute('SELECT id FROM seeker_profiles WHERE user_id = ?', (session['user_id'],)).fetchone()
        if existing:
            conn.execute('''
                UPDATE seeker_profiles 
                SET phone=?, address=?, skills=?, education=?, experience=? 
                WHERE user_id=?
            ''', (phone, address, skills, education, experience, session['user_id']))
        else:
            conn.execute('''
                INSERT INTO seeker_profiles (user_id, phone, address, skills, education, experience)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (session['user_id'], phone, address, skills, education, experience))
            
        conn.commit()
        flash("Profile updated successfully!", "success")
        
    profile = conn.execute('SELECT * FROM seeker_profiles WHERE user_id = ?', (session['user_id'],)).fetchone()
    my_applications = conn.execute('''
        SELECT a.id, j.title, j.company, a.status, a.applied_date 
        FROM applications a JOIN jobs j ON a.job_id = j.id
        WHERE a.seeker_id = ? ORDER BY a.applied_date DESC
    ''', (session['user_id'],)).fetchall()
    
    conn.close()
    return render_template('seeker/profile.html', profile=profile, apps=my_applications)

@app.route('/job/<int:job_id>', methods=['GET', 'POST'])
@login_required
def job_details(job_id):
    conn = get_db_connection()
    job = conn.execute('SELECT * FROM jobs WHERE id = ?', (job_id,)).fetchone()
    
    if not job:
        conn.close()
        flash("Job not found.", "danger")
        return redirect(url_for('index'))
        
    if request.method == 'POST' and session.get('role') == 'seeker':
        if 'resume' not in request.files:
            flash('No resume part in request', 'danger')
            return redirect(request.url)
            
        file = request.files['resume']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            # check if already applied
            already_applied = conn.execute('SELECT id FROM applications WHERE job_id = ? AND seeker_id = ?', 
                                           (job_id, session['user_id'])).fetchone()
            if already_applied:
                flash("You have already applied for this job.", "warning")
            else:
                filename = secure_filename(f"user_{session['user_id']}_job_{job_id}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
                conn.execute('''
                    INSERT INTO applications (job_id, seeker_id, resume) 
                    VALUES (?, ?, ?)
                ''', (job_id, session['user_id'], filename))
                conn.commit()
                flash("Application submitted successfully!", "success")
                
                return redirect(url_for('profile'))
        else:
            flash('Invalid file format. Allowed: .pdf, .doc, .docx', 'danger')
            
    conn.close()
    return render_template('seeker/job_details.html', job=job)


if __name__ == '__main__':
    app.run(debug=True)
