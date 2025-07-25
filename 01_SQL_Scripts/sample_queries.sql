
SELECT Name FROM artists LIMIT 5;

SELECT Title 
FROM albums 
JOIN artists ON albums.ArtistId = artists.ArtistId
WHERE artists.Name = 'AC/DC';

SELECT Name, UnitPrice 
FROM tracks 
ORDER BY UnitPrice DESC LIMIT 5;
