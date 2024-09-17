import streamlit as st


#text/file
st.title("Streamlit Tutorial")
st.text("Hello Streamlit")

#header / subheader 
st.header("This is a header")
st.subheader("This is a subheader")

#writing text  bilgilendirme text'i
st.write("Writing example text with write function")

#importing image
from PIL import Image
img=Image.open("car.jpg")
st.image(img, width=600, caption="Car Prediction")

#chekbox

if st.checkbox("Hide/Seek"):
    st.text("You checked i show")
    

#radio button  
status=st.radio("Select your status", ("Graduate", "Student"))
if status == "Graduate" :
    st.success("Congrats")
    
else:
    st.info("Keep working") 
    
    
#markdown
st.markdown("**This is a markdown**")   

#colorfull text   
st.success('Succesfull')
st.info("This is information")


#warning-eror   
st.warning('This is a warning')
st.error('Stop...That give a error')


#get help
st.help(range)

#select box  
path=st.selectbox("Your path is ", ["DS", "FS", "AWS/DevOps"])
st.write("Your path is", path)


#multiselect 
profession = st.multiselect("Select your profession", ["Engineer", "Teacher", "Nurse", "IT"])
st.write("Your profession is", profession)

#slider  
count=st.slider("How many years of experience in IT" ,1,10)                              
count=st.slider("How many years of experience in IT" ,1,10,2,(2))                
#button 
st.button("Press this button")
if st.button("About Program"):
    st.text("Streamlit is easy and fun")
else:
    st.text("Nothing to say")

    
# text input  ()
firstname= st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(firstname.title())   
    

# text area  ()
message= st.text_area("Enter your message:", "type right here..")
if st.button("submit"):
    st.info(message.title())

    
    #date input
import datetime   
today=st.date_input("Today is" , datetime.datetime.now())

# metin ve rakam şeklinde input
st.text_input('First name')
st.number_input('Pick a number', 0, 10)

# raw data   
st.text("display text")
st.code("import pandas as pd")


# multiple line  code
with st.echo():
    import pandas as pd
    import numpy as np
    import seaborn as sns


# sidebar  
st.sidebar.title("This is a sidebar")
# -----------------------------
st.latex(r'E = mc^2')  #LaTeX formatında matematiksel ifadeler ekler.

# -----------------------------

## Dosya Yükleme
import pandas as pd

# Dosya yükleme widget'ını ekleyin
#uploaded_file = st.file_uploader("Advertising.csv", type=["csv"])

# Eğer bir dosya yüklendiyse, bu dosyayı pandas ile okuyun
#if uploaded_file is not None:
    #data = pd.read_csv(uploaded_file)
    #st.write(data)  # DataFrame'i ekrana yazdır
    
    # ------------------------
    
# Dosyayı doğrudan pandas ile okuyun..dpsya aynı dizinde olmalı
data = pd.read_csv('Advertising.csv')

# DataFrame'i ekrana yazdır
st.write(data)
# st.dataframe(data)   aynı şeyi yapar (df i ekrana yazdırır
# -----------------------------

# Plotly ile bir scatter plot oluşturalım. rneğin, TV reklam bütçesi ile satışları karşılaştıralım.

import plotly.express as px

fig = px.scatter(data, x='TV', y='sales', title='TV Reklamları vs. Satışlar')
st.plotly_chart(fig)

# -----------------------------
#Vega-Lite ile bir bar chart oluşturalım.Örneğin, radyo reklam bütçesinin ortalamasını gösterelim.

bar_chart = {
    "mark": "bar",
    "encoding": {
        "x": {"field": "radio", "bin": True, "type": "quantitative"},
        "y": {"aggregate": "average", "field": "sales", "type": "quantitative"}
    }
}
st.vega_lite_chart(data, bar_chart)
# -----------------------------

#st.pyplot(): Bu fonksiyon, Matplotlib ile oluşturulan grafikleri göstermek için kullanılır. Örneğin, TV reklam bütçesi ile satışları bir scatter plot ile gösterelim:

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(data['TV'], data['sales'], color='blue')
plt.title('TV Reklamları vs. Satışlar')
plt.xlabel('TV Reklam Bütçesi')
plt.ylabel('Satışlar')
st.pyplot(plt)

# -----------------------------

st.markdown(
    """
    <div style='background-color: orange; padding: 10px;'>
    <h1 style='color: white; text-align: center;'>Streamlit Arayüzü</h1>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------

## --------------------------------------------
#st.map():Bu fonksiyon, coğrafi veri görselleştirmesi için kullanılır. Advertising.csv bu tür verilere sahip olmadığı için bu fonksiyonun kullanımı bu veri seti için uygun değil. Ancak, genel bir örnek vermek gerekirse:

# Örnek veri
map_data = pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.5, -122.6]
})

st.map(map_data)

## --------------------------------------------
# st.line_chart():Bu fonksiyon, çizgi grafikleri göstermek için kullanılır. Örneğin, veri setindeki satışları bir çizgi grafiği ile gösterelim:

st.line_chart(data['sales'])
## --------------------------------------------
#st.altair_chart():Altair ile bir bar chart oluşturalım. Örneğin, radyo reklam bütçesi ile satışları karşılaştıralım:
import altair as alt

chart = alt.Chart(data).mark_bar().encode(
    x='radio',
    y='sales',
    color='sales'
).properties(
    title='Radyo Reklamları vs. Satışlar'
)
st.altair_chart(chart, use_container_width=True)



## --------------------------------------------

#st.code()
import pandas as pd

# Veri çerçevesini görüntüler
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
st.code(
    df.to_markdown(),
    #lang="markdown",
    #linenumbers=True,
)

## --------------------------------------------
#st.checkbox()
if st.checkbox('Onayla'): st.write('Onaylandı!')

# --------------------------------
