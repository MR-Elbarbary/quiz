CREATE TABLE "quiz"(
    "id" INTEGER,
    "question" TEXT NOT NULL,
    "a" TEXT NOT NULL,
    "b" TEXT NOT NULL,
    "c" TEXT NOT NULL,
    "d" TEXT NOT NULL,
    "answer" TEXT NOT NULL,
    PRIMARY KEY("id")
);

INSERT INTO "quiz" ("question", "a", "b", "c", "d", "answer")
SELECT "question", " choice a", " choice b", " choice c", " choice d", " answer" FROM temp;

UPDATE quiz SET  "answer"= TRIM(answer);