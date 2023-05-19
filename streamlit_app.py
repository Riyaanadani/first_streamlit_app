import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents New healthy diner')

streamlit.header(' Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


streamlit.header("Fruityvice Fruit Advice!")


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected =  streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.header('fruityvice fruit advice!')

except URLError as e:
  streamlit.error()



#take the json version of response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it the screen as a table 
streamlit.dataframe(fruityvice_normalized)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding " + new_fruit

# Adding fruits to the list
insert_row_snowflake("jackfruit")
insert_row_snowflake("papaya")
insert_row_snowflake("guava")
insert_row_snowflake("kiwi")




