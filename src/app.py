import streamlit as st
import app_api
import app_db



st.title('MOVIE (API/DATABASE) PROJECT ')
st.sidebar.title("FILTER SECTION")
option = st.sidebar.selectbox("choose your option",
                     ("SERACH MOVIES BY API","INSERT DATA","SELECT ALL DATA","SELECT BY ID","UPDATE BY ID","DELETE BY ID","SEARCH MOVIE BY NAME","UPDATE MOVIE BY NAME","DELETE MOVIE BY NAME"))


if option == "SERACH MOVIES BY API":
    st.title("ENTER THE ID OF ANY MOVIE TO GET MOVIE'S INFO")

    movie_id = st.text_input("enter movie id: ")
    
    if st.button("showmovie info: "):
        result = app_api.get_movie_by_id(movie_id)
        st.metric("title", value=result[0])
        st.metric("director", value=result[1])
        st.metric("imbd_rating", value=result[2])
        
    if st.button("save_the_movie_info"):
        result = app_api.get_movie_by_id(movie_id)
        app_db.insert_movie(title=result[0], director=result[1], imdb_rating=result[2])
        st.success(" DATA Saved Successfully")


elif option=="INSERT DATA":
    title = st.text_input("enter movie's name: ")
    director = st.text_input("enter director's of the movie: ") 
    imdb_rating = st.number_input("enter IMBD rating: ", min_value=0)
    if st.button("ADD DATA"):
        app_db.insert_movie(title, director, imdb_rating)
        st.success("INSERT DATA Successfully")


elif option == "SELECT ALL DATA":
    result = app_db.select_all_movies()
    for item in result:
        st.metric("title", value= item[1])
        st.metric("Director", value= item[2])
        st.metric("Rating", value=item[3])
        st.write("=" * 80)


elif option == "SELECT BY ID":
    id = st.number_input("enter id : ", min_value=0)
    selected_by_id =app_db.select_movie_by_id(id)
    if st.button("SELECT DATA"):
        st.success("SELECTED Successfully")
    for item in selected_by_id:
        st.metric("title", value= item[0])
        st.metric("Director", value= item[1])
        st.metric("Rating", value=item[2])



elif option == "UPDATE BY ID":
    st.title("Delete by id")
    movie_id = st.number_input("enter movie id:", min_value=0)
    new_title = st.text_input("New title: ")
    new_director = st.text_input("New director:")
    new_rating = st.text_input("New rating:")

    if st.button("Update"):
        app_db.update_movie_by_id(movie_id ,new_title , new_director, new_rating)
        st.success("Done")



elif option == "DELETE BY ID":
    id = st.number_input("enter id : ", min_value=0)
    delet_by_id =app_db.delete_movie_by_id(id)
    if st.button("DELETE DATA"):
        st.success("DATA DELETED Successfully")


elif option == "SEARCH MOVIE BY NAME":
    st.title("Search by name")
    name = st.text_input("Movie name:")
    if st.button("Search"):
        movie = app_db.search_movie_by_name(name)
        if movie:
            st.metric("title", movie[0])
            st.metric("Director", movie[1])
            st.metric("Rating", movie[2])


elif option == "UPDATE MOVIE BY NAME":
    st.title("Update by name")
    name = st.text_input("Movie name:")
    new_director = st.text_input("New director:")
    new_rating = st.text_input("New rating:")
    
    if st.button("Update"):
        app_db.update_movie_by_name(name, new_director, new_rating)
        st.success("Done")

        
elif option == "DELETE MOVIE BY NAME":
    st.title("Delete by name")
    name = st.text_input("Movie name to delete:")
    if st.button("Delete"):
        app_db.delete_movie_by_name(name)
        st.success("Deleted")
        




