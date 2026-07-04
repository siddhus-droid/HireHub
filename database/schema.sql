CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('employer', 'seeker'))
);

CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    category TEXT NOT NULL,
    skills TEXT NOT NULL,
    experience TEXT NOT NULL,
    salary TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT NOT NULL,
    last_date TEXT NOT NULL,
    employer_id INTEGER NOT NULL,
    FOREIGN KEY(employer_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    seeker_id INTEGER NOT NULL,
    resume TEXT NOT NULL, -- Path to resume file
    status TEXT NOT NULL DEFAULT 'Pending' CHECK(status IN ('Pending', 'Accepted', 'Rejected')),
    applied_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(job_id) REFERENCES jobs(id),
    FOREIGN KEY(seeker_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS seeker_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    phone TEXT,
    address TEXT,
    skills TEXT,
    education TEXT,
    experience TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
