import streamlit as st

st.set_page_config(
    
    page_title= "Saudi Arabia Used Cars",
    page_icon= "🚗",
)

st.image("car3.gif", caption="Welcome to this interactive storytelling app", use_column_width=True, width= 200)

st.title("What to Buy? Uncovering the Best common cars in Saudi Arabia 🚘.")
st.markdown("""In a country known for its vast deserts, and luxurious lifestyles, the quest for the best car is a journey many embark upon. But with many choices available, how does one determine the top car brand and the best city to purchase in Saudi Arabia?""")
st.markdown("""We have analyzed a comprehensive dataset that includes various parameters such as car sales figures, model availability, regions of the Kingdom, year of manufacture, etc. By delving into this data, we aim to provide a 
            clear and practical guide for anyone looking to make a car purchase in Saudi Arabia.""")
st.markdown("---")

###############333
# Uploading and displaying the image

st.subheader("First Chart (Car Brand)")
st.image("carBrands.png", caption="most commun used car brands", use_column_width=True)
st.write("""
         If you're planning to buy a car and are curious about 
         the most sought-after brands in the Saudi market, you're in the
         right place. Based on user preferences and market data, we’ve identified
        the top car brands that are capturing the hearts of drivers across the Kingdom. We’ll recommend the best
        brands for you, highlighting what makes them the preferred choice for car buyers in Saudi Arabia.""")

st.write(
    """
According to the data we analyzed, we will review the top 3 companies. 
As you can see here in the chart, most users in Saudi Arabia prefer Toyota cars at 26%, followed by Hyundai at 12%, then Ford at 9%. As you can see, there is a huge difference between Toyota and Hyundai, and this may be due to their high quality,
 affordable prices, and the availability of spare parts easily and everywhere.
"""
)
##################################

st.subheader("Second Chart (Regions)")
st.image("Region.png", caption="Saudi Regions", use_column_width=True)
st.write("""
         Now that you know the most popular car brands in Saudi Arabia, 
         the next question is: where should you go to find them? The answer is both 
         simple and complex, as the Kingdom boasts numerous cities, each with its own unique market dynamics. With so many options, 
         it's easy to feel overwhelmed when trying to pinpoint the best destination to purchase the car of your dreams.
         But don't worry—we’re here to guide you. We'll uncover the best places to buy a car in Saudi Arabia. We'll delve into the data to 
         explore where the best deals can be found and explain why certain cities emerge as the top choices for car buyers
.""")
st.write("""
The Saudi car market is primarily concentrated in three major cities: Riyadh, Dammam, and Jeddah. Riyadh, as the largest market, accounts for a substantial '40%' of the entire Saudi market. Following Riyadh is Dammam, which holds '17%' of the market share. Due to their close geographical proximity, we recommend starting your car search in these two cities, as together they represent a significant '57%' of the market.
Jeddah comes in as the third largest car market, comprising '13%' of the Saudi market. While it may be smaller than Riyadh and Dammam, Jeddah still offers a variety of options worth considering.
The remaining regions of the Kingdom collectively make up just '30%' of the market. Given this distribution, focusing your car search in Riyadh, Dammam, and Jeddah will provide you with the best opportunities in terms of variety and price differences
""")

################################3

st.markdown("---")

st.subheader("Third Chart (Options)")
st.image("options.png", caption="Car types", use_column_width=True)
st.write("""
         The data indicates that the vast majority of buyers in Saudi Arabia prefer the "Standard" category at a rate of 46%. This is because it is the lowest priced option compared to the other categories.
         After that, the "FULL" category comes in second place with '32%' of sales. It is the highest in specifications, but also the highest in price.
         The "semi full" category is the least sold at 22%. It is not recommended to suggest buying it, as '78%' of buyers do not prefer it.
         Based on this, it is recommended to focus on the "Standard" and "FULL" categories as they are the most in-demand in the Saudi market
.""")

st.markdown("---")

st.write("Thank you for your time, See you again 👋")

#st.title('Where and What to Buy? The Best Cars in Saudi Arabia')
#st.markdown("")
#url = "https://www.kaggle.com/datasets/raihanmuhith/saudi-arabia-used-car/data"
#st.write("DataSorce [link](%s)" % url)
#st.image("11.png",caption="ajhju")

#st.markdown('We’ve created a user-friendly interface using Streamlit. Users can input their preferences: make, maximum price, maximum mileage, and minimum year. Our system then searches through the data store to find matching cars')
#st.image("11.png", width=250)
