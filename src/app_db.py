import sqlite3

DB_NAME = "Movies.db"

def create_table():
    query = """
        CREATE TABLE IF NOT EXISTS movies (
            movie_id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title        TEXT NOT NULL,
            director     TEXT NOT NULL,
            imdb_rating  REAL NOT NULL
        )
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def insert_movie(title, director, imdb_rating):
    query = """
        INSERT INTO movies (title, director, imdb_rating)
        VALUES (?, ?, ?)
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (title, director, imdb_rating))
    conn.commit()
    conn.close()


def select_all_movies():
    query = "SELECT movie_id, title, director, imdb_rating FROM movies ORDER BY movie_id"
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result


def select_movie_by_id(movie_id):
    query = "SELECT movie_id, title, director, imdb_rating FROM movies WHERE movie_id = ?"
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (movie_id,))
    result = cursor.fetchall()
    conn.close()
    return result


def update_movie_by_id(movie_id, title, new_director, new_rating):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE movies SET title = ?, director = ?, imdb_rating = ? WHERE movie_id = ?",
        (title ,new_director, new_rating, movie_id)
    )
    conn.commit()
    conn.close()



def delete_movie_by_id(movie_id):
    query = "DELETE FROM movies WHERE movie_id = ?"
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (movie_id,))
    conn.commit()
    conn.close()


def search_movie_by_name(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT title, director, imdb_rating FROM movies WHERE title = ?", (title,))
    movie = cursor.fetchone()  
    conn.close()
    return movie


def update_movie_by_name(title, new_director, new_rating):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE movies SET director = ?, imdb_rating = ? WHERE title = ?",
        (new_director, new_rating, title)
    )
    conn.commit()
    conn.close()


def delete_movie_by_name(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE title = ?", (title,))
    conn.commit()
    conn.close()

# if __name__=="__main__":
#     create_table()

#     insert_movie("Inception", "Christopher Nolan", 8.8)
#     insert_movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 8.7)
#     insert_movie("Interstellar", "Christopher Nolan", 8.7)
#     insert_movie("Pulp Fiction", "Quentin Tarantino", 8.9)

