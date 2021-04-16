CREATE TABLE `Journal_Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`topic`	TEXT NOT NULL,
	`journal_entry`	TEXT NOT NULL,
	`mood_id`	TEXT NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);


CREATE TABLE `Moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`mood`	TEXT NOT NULL
);


INSERT INTO `Journal_Entries` VALUES (null, '01/10/2021', 'death', 'journal1', 1);
INSERT INTO `Journal_Entries` VALUES (null, '01/12/2021', 'milk', 'journal2', 2);
INSERT INTO `Journal_Entries` VALUES (null, '01/14/2021', 'meat', 'journal3', 3);
INSERT INTO `Journal_Entries` VALUES (null, '01/16/2021', 'feelings', 'journal4', 4);

INSERT INTO `Moods` VALUES (null, 'Sad');
INSERT INTO `Moods` VALUES (null, 'Elated');
INSERT INTO `Moods` VALUES (null, 'Excited');
INSERT INTO `Moods` VALUES (null, 'Contemplative');

