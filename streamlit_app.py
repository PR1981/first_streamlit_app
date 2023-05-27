import streamlit, pandas, requests

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣Omega 3')

streamlit.text('🥗kale, Spinach')

streamlit.text('🐔Hard Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Banana'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json())

# take the json verions of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output the dataframe to the screen as a table
streamlit.dataframe(fruityvice_normalized)
