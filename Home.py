import streamlit as st
import streamlit.components.v1 as com

st.set_page_config(
    page_title= "Usecase 5",
    page_icon= "📊",
)

st.write("Musab Alsobhi")


com.iframe("https://lottie.host/embed/8282b0f3-b32c-471e-ab86-31450ad9e82e/t9siwwhkSN.json", width= 750, height=450)


st.title("Understanding the direction of jobs in Saudi Arabia")
st.write("welcome to this interactive story telling app")
st.subheader("Introduction:")
st.markdown("""
            Understanding the changes in the employment market is crucial for both job seekers and employers in today's dynamic environment. 
            We may learn more about career openings, their locations, preferences for men or women, the salary that recent graduates will earn, 
            and the level of experience required for various positions in Saudi Arabia by examining data from the Jadarat platform.
            """)
st.markdown("---")

#######################

st.subheader("Part 1: Where Are the Jobs?")
st.markdown("""
            First, let’s check out where the jobs are in Saudi Arabia. We’ll see how many job postings there are in each region. 
            This helps us figure out which areas have lots of jobs and which ones don’t. 
            This is helpful for anyone thinking about moving for a job or for leaders who want to make sure all regions are developing evenly.
            """)
st.image("JobRe.png", caption="chart #1", use_column_width=True)
st.markdown("---")

######################

st.subheader("Part 2: Are most Jobs for Men, Women, or Both?")
st.markdown("""
            Next, let’s see if there’s a preference for hiring men or women. Are more jobs aimed at one gender,
            or are they open to everyone? This can tell us a lot about gender equality in the workplace and 
            help companies see how they’re doing with diversity..
            """)
st.image("gender.png", caption="chart #2", use_column_width=True)
st.markdown("---")

######################

st.subheader("Part 3: What Can Fresh Graduates Expect to Earn?")
st.markdown("""
            If you’re a fresh graduate, you’re probably wondering what kind of salary you can expect. 
            We’ll look at jobs that don’t require much experience to see what the typical salary range is. 
            This gives new graduates a better idea of what to expect as they start their careers.
            """)
st.image("fresh.png", caption="chart #3", use_column_width=True)
st.markdown("---")

######################

st.subheader("Part 4: Do You Need Experience to Get a Job?")
st.markdown("""
            Finally, let’s find out how much experience you need for the jobs out there. 
            Are most jobs looking for experienced people, or is there a good mix that includes fresh graduates too? 
            This helps us understand if there are opportunities for everyone, 
            no matter their experience level.
            """)
st.image("years.png", caption="chart #4", use_column_width=True)
st.markdown("---")

######################

st.subheader("Conclusion:")
st.markdown("""
            We’ve walked through some key job trends in Saudi Arabia. 
            Whether you’re just starting out or have been in the workforce for a while, 
            understanding these trends can help you make better decisions about your career or hiring needs.
            """)

######################

st.subheader("Call to Action:")
st.markdown("""
            If you’re looking for a job or hiring, check out the Jadarat platform. (I have provided the link in the Dataset📊 page)
            It has lots of opportunities that could be a perfect match for your skills or your company’s needs.
            """)
st.markdown("---")

#######################


st.write("Thank you for your time, See you again 👋")


