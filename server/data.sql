CREATE TABLE drills (
	drill_id   INTEGER PRIMARY KEY,
    api        TEXT       NOT NULL,
    question   TEXT       NOT NULL,
    answer     BIGINT     NOT NULL,
    start_time TEXT       NOT NULL,
    stop_time  TEXT,
    elapsed    BIGINT
);
