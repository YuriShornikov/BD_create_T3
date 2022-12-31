INSERT INTO musicians(name)
VALUES('Михаил Горшенёв'), ('Виктор Цой'), ('Александр Васильев'), ('Алексей Горшенёв'), ('Маша Архипова'), ('Феофан'), ('Тилль Линдеманн'), ('Алексей Юзленко');

SELECT * FROM musicians;

INSERT INTO musical_genres(name)
VALUES('Art pank'), ('Rock'), ('Folk metal'), ('Drum n bass'), ('Indastrisl metal');

SELECT * FROM musical_genres;

INSERT INTO albums(name, album_release)
VALUES('Театр демонов', 2010), ('Группа крови', 1988), ('Встречная полоса', 2018), ('Артист', 2016), ('Храм', 2018), ('Древнерусский рейв', 2021), ('Zeit', 2022), ('Жизнь и Смерть', 2021);

SELECT * FROM albums;

INSERT INTO tracks(name, time, album_id)
VALUES('Фокусник', 213, 1), ('Темный учитель', 276, 1), ('Группа крови', 286, 2), ('В наших глазах', 215, 2), ('Встречная полоса', 268, 3), ('На утро', 244, 3), 
('Артист', 232, 4), ('Шторм', 242, 4), ('Мой храм', 590, 5), ('Мантра (Интро)', 231, 5), ('Древнерусский рейв', 220, 6), ('На заре', 214, 6), ('Zeit', 322, 7), ('Giffig', 189, 7), ('Жизнь и Смерть', 254, 8), ('Душа', 225, 8);

SELECT * FROM tracks;

INSERT INTO digests(name, digests_release)
VALUES('Быль и Небыль. Том II', 2022), ('Последний герой', 1989), ('Лучшие песни 90х', 1993), ('Рок хиты', 2010), ('Лучшие фолк треки', 2019), ('Das Modell', 1997), ('Rock hits 150', 2021), ('Hold Your Colour', 2005);

SELECT * FROM digests;