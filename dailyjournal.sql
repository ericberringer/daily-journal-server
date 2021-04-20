CREATE TABLE `Journal_Entry` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`topic`	TEXT NOT NULL,
	`journal_entry`	TEXT NOT NULL,
	`mood_id`	TEXT NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);


CREATE TABLE `Mood` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`mood`	TEXT NOT NULL
);


INSERT INTO `Journal_Entry` VALUES (null, '01/10/2021', 'death', 'journal1', 1);
INSERT INTO `Journal_Entry` VALUES (null, '01/12/2021', 'milk', 'journal2', 2);
INSERT INTO `Journal_Entry` VALUES (null, '01/14/2021', 'meat', 'journal3', 3);
INSERT INTO `Journal_Entry` VALUES (null, '01/16/2021', 'feelings', 'journal4', 4);

INSERT INTO `Mood` VALUES (null, 'Sad');
INSERT INTO `Mood` VALUES (null, 'Elated');
INSERT INTO `Mood` VALUES (null, 'Excited');
INSERT INTO `Mood` VALUES (null, 'Contemplative');


SELECT
	e.id,
	e.date,
	e.topic,
	e.journal_entry,
	e.mood_id
FROM Journal_Entry e
WHERE e.id = 3