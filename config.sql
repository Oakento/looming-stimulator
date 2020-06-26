BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "history" (
	"last_id"	INTEGER
);
CREATE TABLE IF NOT EXISTS "config" (
	"config_id"	INTEGER,
	"description"	TEXT,
	"min_degree"	NUMERIC,
	"max_degree"	NUMERIC,
	"chamber_height"	NUMERIC,
	"time_expand"	NUMERIC,
	"time_hold"	NUMERIC,
	"time_pause"	NUMERIC,
	"repeat"	INTEGER,
	PRIMARY KEY("config_id")
);
INSERT INTO "config" ("config_id","description","min_degree","max_degree","chamber_height","time_expand","time_hold","time_pause","repeat") VALUES (1,'',2,20,40,0.25,0.25,0.5,5);
COMMIT;
