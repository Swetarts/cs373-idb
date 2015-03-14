CREATE TABLE "COMIC_SERIES" (
"ID" int4 NOT NULL,
"TITLE" varchar(255) NOT NULL,
"IMAGE" varchar(255),
"LAUNCH_DATE" date,
"PUBLISHER" int4,
PRIMARY KEY ("ID") 
);

CREATE TABLE "CHARACTER" (
"ID" int4 NOT NULL,
"NAME" varchar(255) NOT NULL,
"ALIAS" varchar(255),
"IMAGE" varchar(255),
"DESCRIPTION" varchar(4000),
"GENDER" varchar(255),
"ORIGIN" varchar(255),
"POWERS" int4,
"TEAMS" int4,
PRIMARY KEY ("ID") 
);

CREATE TABLE "PEOPLE" (
"ID" int4 NOT NULL,
"NAME" varchar(255),
"IMAGE" varchar(255),
"BIRTH_DATE" date,
"COUNTRY" varchar(255),
"JOB_TITLE" varchar(255),
"WEBSITE" varchar(255),
"GENDER" varchar(255),
PRIMARY KEY ("ID") 
);

CREATE TABLE "PUBLISHER" (
"ID" int4 NOT NULL,
"NAME" varchar(255) NOT NULL,
PRIMARY KEY ("ID") 
);

CREATE TABLE "GENDER" (
"ID" int4 NOT NULL,
"NAME" varchar(255),
PRIMARY KEY ("ID") 
);

CREATE TABLE " COMIC_PEOPLE" (
"COMIC_ID" int4 NOT NULL,
"PEOPLE_ID" int4 NOT NULL
);

CREATE TABLE "CHARACTER_CREATOR" (
"CHARACTER_ID" int4 NOT NULL,
"CREATOR_ID" int4 NOT NULL
);

CREATE TABLE "CHARACTER_ENEMY" (
"CHARACTER_ID" int4 NOT NULL,
"ENEMY_ID" int4 NOT NULL
);

CREATE TABLE "CHARACTER_ALLY" (
"CHARACTER_ID" int4 NOT NULL,
"ALLY_ID" int4 NOT NULL
);

CREATE TABLE "COMIC_CHARACTERS" (
"COMIC_ID" int4 NOT NULL,
"CHARACTER_ID" int4 NOT NULL
);

CREATE TABLE "POWER" (
"ID" int4 NOT NULL,
"NAME" varchar(255) NOT NULL,
PRIMARY KEY ("ID") 
);

CREATE TABLE "CHARACTER_POWER" (
"CHARACTER_ID" int4 NOT NULL,
"POWER_ID" int4 NOT NULL
);

CREATE TABLE "TEAM" (
"ID" int4 NOT NULL,
"NAME" varchar(255) NOT NULL,
PRIMARY KEY ("ID") 
);

CREATE TABLE "CHARACTER_TEAM" (
"CHARACTER_ID" int4 NOT NULL,
"TEAM_ID" int4 NOT NULL
);


ALTER TABLE "PEOPLE" ADD CONSTRAINT "fk_PEOPLE_GENDER" FOREIGN KEY ("GENDER") REFERENCES "GENDER" ("ID");
ALTER TABLE " COMIC_PEOPLE" ADD CONSTRAINT "fk_COMIC_CREDIT_COMIC_SEREIS" FOREIGN KEY ("COMIC_ID") REFERENCES "COMIC_SERIES" ("ID");
ALTER TABLE "COMIC_SERIES" ADD CONSTRAINT "fk_PUBLISHER" FOREIGN KEY ("PUBLISHER") REFERENCES "PUBLISHER" ("ID");
ALTER TABLE " COMIC_PEOPLE" ADD CONSTRAINT "fk_COMIC_PEOPLE" FOREIGN KEY ("PEOPLE_ID") REFERENCES "PEOPLE" ("ID");
ALTER TABLE "CHARACTER_CREATOR" ADD CONSTRAINT "fk_CHARACTER" FOREIGN KEY ("CHARACTER_ID") REFERENCES "CHARACTER" ("ID");
ALTER TABLE "CHARACTER_CREATOR" ADD CONSTRAINT "fk_CREATOR" FOREIGN KEY ("CREATOR_ID") REFERENCES "PEOPLE" ("ID");
ALTER TABLE "CHARACTER_ENEMY" ADD CONSTRAINT "FK_ENEMY_ID" FOREIGN KEY ("ENEMY_ID") REFERENCES "CHARACTER" ("ID");
ALTER TABLE "CHARACTER_ENEMY" ADD CONSTRAINT "FK_CHARACTER_ID" FOREIGN KEY ("CHARACTER_ID") REFERENCES "CHARACTER" ("ID");
ALTER TABLE "CHARACTER_ALLY" ADD CONSTRAINT "fk_ALLY_ID" FOREIGN KEY ("ALLY_ID") REFERENCES "CHARACTER" ("ID");
ALTER TABLE "CHARACTER_ALLY" ADD CONSTRAINT "fk_CHARACTER_ID" FOREIGN KEY ("CHARACTER_ID") REFERENCES "CHARACTER" ("ID");
ALTER TABLE "COMIC_CHARACTERS" ADD CONSTRAINT "fk_CHAR_ID" FOREIGN KEY ("CHARACTER_ID") REFERENCES "CHARACTER" ("ID");
ALTER TABLE "COMIC_CHARACTERS" ADD CONSTRAINT "fk_COMIC_ID" FOREIGN KEY ("COMIC_ID") REFERENCES "COMIC_SERIES" ("ID");
ALTER TABLE "CHARACTER_POWER" ADD CONSTRAINT "fk_CHAR" FOREIGN KEY ("CHARACTER_ID") REFERENCES "CHARACTER" ();
ALTER TABLE "CHARACTER_POWER" ADD CONSTRAINT "fk_POWER" FOREIGN KEY ("POWER_ID") REFERENCES "POWER" ();
ALTER TABLE "CHARACTER_TEAM" ADD CONSTRAINT "FK_CHAR" FOREIGN KEY ("CHARACTER_ID") REFERENCES "CHARACTER" ("ID");
ALTER TABLE "CHARACTER_TEAM" ADD CONSTRAINT "FK_POWER" FOREIGN KEY ("TEAM_ID") REFERENCES "TEAM" ("ID");

