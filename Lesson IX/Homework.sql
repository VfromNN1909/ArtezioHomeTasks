# ----- задание 1 -----

# создаем БД
CREATE DATABASE IF NOT EXISTS employees;
# переходим в неё,дабы использовать
USE employees;
# создаем таблицу 
CREATE TABLE IF NOT EXISTS info(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
	second_name VARCHAR(30) NOT NULL,
	position VARCHAR(30) NOT NULL,
	salary DECIMAL(7,0) NOT NULL,
	boss INT UNSIGNED
);
# заполняем таблицу
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Oleg', 'Ivanov', 'Manager', 45000, 1);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Ivan', 'Minin', 'Manager', 43000, 2);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Artem', 'Belov', 'Manager', 50000, 3);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Alex', 'Petrov', 'Developer', 40000, 1);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Andrey', 'Sidorov', 'Developer', 50000, 3);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Vasily', 'Grunin', 'Developer', 30000, 2);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Vladimir', 'Vlasov', 'Developer', 55000, 2);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Alex', 'Guschin', 'Designer', 20000, 3);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Denis', 'Gerasimov', 'Designer', 25000, 3);
INSERT INTO info (first_name, second_name, position, salary, boss) VALUES ('Georgy', 'Zhukov', 'Designer', 40000, 1);

# ----- задание 2 -----

# два запроса
SELECT * FROM employees.info WHERE salary < 30000;
SELECT * FROM employees.info WHERE salary < 30000 AND position = 'Designer';

# ----- задание 3 -----

# создаем таблицу босов
CREATE TABLE IF NOT EXISTS bosses(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT primary key,
	first_name VARCHAR(30) NOT NULL,
	second_name VARCHAR(30) NOT NULL,
	position VARCHAR(30) NOT NULL,
	salary DECIMAL(7,0) NOT NULL,
	subordinate INT UNSIGNED	
);
# добавляем туда всех менеджеров
INSERT INTO bosses SELECT * FROM info WHERE position = 'Manager';

# связующая таблица
CREATE TABLE IF NOT EXISTS bosses_subordinates(
	boss INT UNSIGNED,
	subordinate INT UNSIGNED,
	PRIMARY KEY (boss, subordinate)
);
# выдает в 1ой строке босса(для наглядного понимания), а ниже подчиненных
SELECT first_name, second_name, position FROM info WHERE boss in (SELECT subordinate FROM bosses WHERE subordinate = 3);