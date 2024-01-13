SELECT name FROM people WHERE id = (SELECT ALL person_id FROM stars WHERE movie_id = (SELECT ALL id FROM movies WHERE year=2004));
