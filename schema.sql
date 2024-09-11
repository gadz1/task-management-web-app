CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    pass TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pname TEXT NOT NULL,
    describtion TEXT NOT NULL,
    user_id INTEGER,  -- Foreign key column
    FOREIGN KEY (user_id) REFERENCES users(id)  -- Each project belongs to a user
);

CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Tname TEXT NOT NULL,
    tag_id INTEGER,  -- Foreign key column
    project_id INTEGER,  -- Foreign key column
    FOREIGN KEY (tag_id) REFERENCES tags(id),  -- Each task has one tag
    FOREIGN KEY (project_id) REFERENCES projects(id)  -- Each task belongs to a project
);

CREATE TABLE IF NOT EXISTS tags(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Tname TEXT NOT NULL,
    color TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS members(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Mname TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS member_task(
    member_id INTEGER,
    task_id INTEGER,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (task_id) REFERENCES tasks(id),
    PRIMARY KEY (member_id, task_id)
);