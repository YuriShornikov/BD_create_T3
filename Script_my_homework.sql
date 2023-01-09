CREATE TABLE IF NOT EXISTS musical_genres 
(
	musical_genre_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS musicians
(
	musician_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS musical_genres_musicias
(
	musical_genres_musicias_id SERIAL PRIMARY KEY,
	musician_id SERIAL NOT NULL references musicians(musician_id),
	musical_genre_id SERIAL NOT NULL references musical_genres(musical_genre_id)
);

CREATE TABLE IF NOT EXISTS albums
(
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	album_release INT NOT NULL 
);

CREATE TABLE IF NOT EXISTS musicians_albums
(
	musicians_albums_id SERIAL PRIMARY KEY,
	musician_id SERIAL NOT NULL references musicians(musician_id),
	album_id SERIAL NOT NULL references albums(album_id)
);

CREATE TABLE IF NOT EXISTS digests
(
	digests_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	digests_release INT NOT NULL 
);

CREATE TABLE IF NOT EXISTS tracks
(
	track_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	time INT NOT NULL,
	album_id SERIAL NOT NULL references albums(album_id)
);

CREATE TABLE IF NOT EXISTS digests_tracks
(
	digests_tracks_id SERIAL PRIMARY KEY,
	digests_id SERIAL NOT NULL references digests(digests_id),
	track_id SERIAL NOT NULL references tracks(track_id)
);

INSERT INTO musicians(name)
VALUES('������ �������'), ('������ ���'), ('��������� ��������'), ('������� �������'), ('���� ��������'), ('������'), ('����� ���������'), ('������� �������');

SELECT * FROM musicians;

INSERT INTO musical_genres(name)
VALUES('Art pank'), ('Rock'), ('Folk metal'), ('Drum n bass'), ('Indastrisl metal');

SELECT * FROM musical_genres;

insert into musical_genres_musicias(musician_id, musical_genre_id)
values(1, 1), (2, 2), (3, 2), (4, 2), (5, 3), (6, 4), (7, 5), (8, 2);

INSERT INTO albums(name, album_release)
VALUES('����� �������', 2010), ('������ �����', 1988), ('��������� ������', 2018), ('������', 2016), ('����', 2018), ('������������� ����', 2021), ('Zeit', 2022), ('����� � ������', 2020);

SELECT * FROM albums;

INSERT INTO tracks(name, time, album_id)
VALUES('��������', 213, 1), ('������ �������', 276, 1), ('������ �����', 286, 2), ('� ����� ������', 215, 2), ('��������� ������', 268, 3), ('�� ����', 244, 3), 
('������', 232, 4), ('�����', 242, 4), ('��� ����', 590, 5), ('������ (�����)', 231, 5), ('������������� ����', 220, 6), ('�� ����', 214, 6), ('Zeit', 322, 7), ('Giffig', 189, 7), ('����� � ������', 254, 8), ('����', 225, 8);

SELECT * FROM tracks;

INSERT INTO digests(name, digests_release)
VALUES('���� � ������. ��� II', 2022), ('��������� �����', 1989), ('������ ����� 90�', 1993), ('��� ����', 2010), ('������ ���� �����', 2019), ('Das Modell', 1997), ('Rock hits 150', 2021), ('Hold Your Colour', 2005);

SELECT * FROM digests;


SELECT name, album_release FROM albums
where album_release = 2018;

select name, time from tracks
order by time desc
limit 1;

select name, time from tracks
where time >= 210;

select name, digests_release from digests
where digests_release between 2018 and 2020;

select name from musicians
where name not like '% %';

update tracks set name = replace (name, '���', 'My')
where name like '%���%';

select * from tracks;


--�� �3

select mg.name, count(mgm.musician_id) from musical_genres_musicias mgm
join musical_genres mg on mg.musical_genre_id = mgm.musical_genre_id
group by mg.name
order by count(mgm.musician_id) desc;

--3.1
SELECT mg.name, COUNT(m.name) FROM musicians m 
left JOIN musical_genres_musicias mgm ON m.musician_id = mgm.musician_id 
left JOIN musical_genres mg ON mgm.musical_genre_id  = mg.musical_genre_id
GROUP BY mg.name
ORDER BY COUNT(m.name) DESC;

select * from musicians;
select * from musical_genres;

--3.2
select a.name, count(t.name) from albums a
join tracks t on t.album_id = a.album_id 
where album_release between 2019 and 2020
group by a.name;

--3.3
select a.name, avg(t.time) from albums a 
join tracks t on t.album_id = t.album_id 
group by a.name
order by avg(t.time); 
