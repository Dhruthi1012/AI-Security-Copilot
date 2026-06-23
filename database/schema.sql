CREATE TABLE IF NOT EXISTS targets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    target_name TEXT NOT NULL,

    target_type TEXT NOT NULL

);



CREATE TABLE IF NOT EXISTS scans (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    target_id INTEGER NOT NULL,

    scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(target_id)
    REFERENCES targets(id)

);



CREATE TABLE IF NOT EXISTS scan_results (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    scan_id INTEGER NOT NULL,

    port INTEGER NOT NULL,

    protocol TEXT NOT NULL,

    service TEXT,

    state TEXT,

    FOREIGN KEY(scan_id)
    REFERENCES scans(id)

);