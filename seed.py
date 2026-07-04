from database import get_db_connection, init_db
from werkzeug.security import generate_password_hash
import os

if not os.path.exists('recruitment.db'):
    init_db()

conn = get_db_connection()

# Clear existing tables for a fresh start
conn.executescript('''
    DELETE FROM applications;
    DELETE FROM jobs;
    DELETE FROM seeker_profiles;
    DELETE FROM users;
''')
conn.commit()

# Create Employer
employer_pass = generate_password_hash('password123')
conn.execute('INSERT INTO users (id, name, email, password, role) VALUES (?, ?, ?, ?, ?)',
             (1, 'TechCorp Inc', 'hr@techcorp.com', employer_pass, 'employer'))
conn.execute('INSERT INTO users (id, name, email, password, role) VALUES (?, ?, ?, ?, ?)',
             (5, 'DataWorks Analytics', 'careers@dataworks.com', employer_pass, 'employer'))
conn.execute('INSERT INTO users (id, name, email, password, role) VALUES (?, ?, ?, ?, ?)',
             (6, 'Global Finance Solutions', 'recruiting@globalfinance.com', employer_pass, 'employer'))

# Create Seeker
seeker_pass = generate_password_hash('password123')
conn.execute('INSERT INTO users (id, name, email, password, role) VALUES (?, ?, ?, ?, ?)',
             (2, 'Sarah Jenkins', 'sarah@example.com', seeker_pass, 'seeker'))
conn.execute('INSERT INTO users (id, name, email, password, role) VALUES (?, ?, ?, ?, ?)',
             (3, 'Ravi Kumar', 'ravi@example.com', seeker_pass, 'seeker'))
conn.execute('INSERT INTO users (id, name, email, password, role) VALUES (?, ?, ?, ?, ?)',
             (4, 'Priya Sharma', 'priya@example.com', seeker_pass, 'seeker'))


# Add Seeker Profile
conn.execute('''
    INSERT INTO seeker_profiles (user_id, phone, address, skills, education, experience) 
    VALUES (?, ?, ?, ?, ?, ?)
''', (2, '+91 98765 43210', 'Mumbai, Maharashtra', 'Python, Flask, JavaScript, SQL', 'BSc Computer Science', '2 years of backend web development.'))

# Post Jobs for TechCorp Inc (Employer 1)
conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (1, 'Junior Python Developer', 'TechCorp Inc', 'IT / Software', 'Python, Flask, SQL', '1-2 Years', '₹6,00,000 - ₹8,00,000', 'Remote', 'We are looking for a Junior Python developer to join our backend team to build scalable APIs.', '2025-12-31', 1))

conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (2, 'Frontend React Engineer', 'TechCorp Inc', 'IT / Software', 'React, JavaScript, CSS', '3+ Years', '₹12,00,000 - ₹15,00,000', 'Bengaluru, Karnataka', 'Looking for an experienced React developer to build modern and responsive UI components.', '2025-11-15', 1))

conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (5, 'Cloud Architect', 'TechCorp Inc', 'IT / Software', 'AWS, Azure, Kubernetes', '7+ Years', '₹20,00,000 - ₹30,00,000', 'Hybrid', 'Architect cloud infrastructure for high-traffic applications.', '2025-10-15', 1))

conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (6, 'QA Engineer', 'TechCorp Inc', 'IT / Software', 'Selenium, Cypress, Python', '2-4 Years', '₹8,00,000 - ₹12,00,000', 'Pune, Maharashtra', 'Ensure the quality of software releases through automated testing.', '2025-09-30', 1))

# Post Jobs for DataWorks Analytics (Employer 5)
conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (3, 'Data Scientist', 'DataWorks Analytics', 'IT / Software', 'Python, Machine Learning, SQL', '2-5 Years', '₹10,00,000 - ₹18,00,000', 'Remote', 'Looking for an innovative data scientist to build predictive models.', '2025-10-01', 5))

conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (7, 'Data Engineer', 'DataWorks Analytics', 'IT / Software', 'Spark, Hadoop, Python', '3-5 Years', '₹15,00,000 - ₹22,00,000', 'Bengaluru, Karnataka', 'Develop and maintain data pipelines for large scale analytics.', '2025-11-20', 5))

conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (8, 'BI Analyst', 'DataWorks Analytics', 'Analytics', 'Tableau, PowerBI, SQL', '1-3 Years', '₹6,00,000 - ₹10,00,000', 'Hyderabad, Telangana', 'Create insightful dashboards for business stakeholders.', '2025-12-10', 5))

# Post Jobs for Global Finance Solutions (Employer 6)
conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (4, 'Financial Analyst', 'Global Finance Solutions', 'Finance', 'Excel, Financial Modeling, Accounting', '1-3 Years', '₹8,00,000 - ₹12,00,000', 'Mumbai, Maharashtra', 'We need a detail-oriented financial analyst to join our expanding team.', '2025-12-01', 6))

conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (9, 'Risk Manager', 'Global Finance Solutions', 'Finance', 'Risk Management, Compliance', '5-8 Years', '₹18,00,000 - ₹25,00,000', 'Mumbai, Maharashtra', 'Oversee enterprise risk and ensure regulatory compliance.', '2025-11-05', 6))

conn.execute('''
    INSERT INTO jobs (id, title, company, category, skills, experience, salary, location, description, last_date, employer_id) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (10, 'Quantitative Analyst', 'Global Finance Solutions', 'Finance', 'Python, C++, Statistics', '2-4 Years', '₹15,00,000 - ₹20,00,000', 'Remote', 'Develop algorithmic trading models.', '2025-10-31', 6))


# Create dummy PDF files in static/uploads
upload_dir = os.path.join('static', 'uploads')
os.makedirs(upload_dir, exist_ok=True)

def create_dummy_pdf(filename, name):
    pdf_content = f"""%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>
endobj
4 0 obj
<< /Length 100 >>
stream
BT /F1 24 Tf 100 700 Td (Sample Resume for {name}) Tj ET
endstream
endobj
5 0 obj
<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
endobj
xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000246 00000 n 
0000000350 00000 n 
trailer
<< /Size 6 /Root 1 0 R >>
startxref
437
%%EOF"""
    with open(os.path.join(upload_dir, filename), 'wb') as f:
        f.write(pdf_content.encode('utf-8'))

create_dummy_pdf('dummy_resume_sarah.pdf', 'Sarah Jenkins')
create_dummy_pdf('dummy_resume_ravi.pdf', 'Ravi Kumar')
create_dummy_pdf('dummy_resume_priya.pdf', 'Priya Sharma')


# Seed Applications
# Sarah applied to Junior Python (Pending)
conn.execute('''
    INSERT INTO applications (job_id, seeker_id, resume, status) 
    VALUES (?, ?, ?, ?)
''', (1, 2, 'dummy_resume_sarah.pdf', 'Pending'))

# Ravi applied to Junior Python (Accepted)
conn.execute('''
    INSERT INTO applications (job_id, seeker_id, resume, status) 
    VALUES (?, ?, ?, ?)
''', (1, 3, 'dummy_resume_ravi.pdf', 'Accepted'))

# Priya applied to Frontend React (Rejected)
conn.execute('''
    INSERT INTO applications (job_id, seeker_id, resume, status) 
    VALUES (?, ?, ?, ?)
''', (2, 4, 'dummy_resume_priya.pdf', 'Rejected'))

# Sarah applied to Data Scientist (Pending)
conn.execute('''
    INSERT INTO applications (job_id, seeker_id, resume, status) 
    VALUES (?, ?, ?, ?)
''', (3, 2, 'dummy_resume_sarah.pdf', 'Pending'))

# Ravi applied to Data Engineer (Accepted)
conn.execute('''
    INSERT INTO applications (job_id, seeker_id, resume, status) 
    VALUES (?, ?, ?, ?)
''', (7, 3, 'dummy_resume_ravi.pdf', 'Accepted'))

# Priya applied to Financial Analyst (Pending)
conn.execute('''
    INSERT INTO applications (job_id, seeker_id, resume, status) 
    VALUES (?, ?, ?, ?)
''', (4, 4, 'dummy_resume_priya.pdf', 'Pending'))

conn.commit()
conn.close()

print("Dummy data seeded successfully!")
print("Employer Logins: hr@techcorp.com, careers@dataworks.com, recruiting@globalfinance.com / password123")
print("Seeker Logins: sarah@example.com, ravi@example.com, priya@example.com / password123")
