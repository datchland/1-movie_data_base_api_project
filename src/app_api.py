import requests
def get_movie_by_id(movie_id):
    url =f"https://moviesapi.ir/api/v1/movies/{movie_id}"
    response = requests.get(url)
    if response.status_code!=200:
        return"erorr"
    else:
        response = response.json()
        title = response['title']
        director = response['director']
        imdb_rate = response['imdb_rating']
        return(title,director,imdb_rate)
    
if __name__=="__main__":
    movie_id = input("enter movie id: ")
    result = get_movie_by_id(movie_id)
    print('title:',result[0])
    print("director : ", result[1])
    print("imbd_rating : ", result[2])