

#header / subheader
st.header("This is a header")
st.subheader("This is a subheader")


#UNUTMA CALISTIRMAK ISTEDIGIN HER CODU CTRL+S ILE KAYDET ZATEN STREAMLIT TE RERUN OTOMATIK CIKAR

#write tetx  bilgilendirme texti
st.write("Writing example text with write write function")  #bu text olarak yazdi

#importing image
from PIL import Image
img = Image.open("single.jpeg")
st.image(img,width = 400, caption = "Car Prediction")

#checkbox

if st.checkbox("Hide/Seek"): #burda if le yazdigimiz icin tick atinca altida You checked i show yazisi cikar bu if mesela bazi sayfa tasarimlarinda RUN tusu ekeyeceksin bazi kodlarin claismasi icin o zaman cok guzel olur
    st.text("You check i show")

    




#radio button

#radio butonu ya o ya digeri mantiginda secenek imkani sunar

status = st.radio("Select your status", ("Graduate", "Student"))
if status == "Graduate":
    st.success("Congrats") #yesil bantli yazi alani olusturur
else:
    st.info("Keep working") #info mavi bandli yazi ayzmani saglar
    
    
    
    
#markdown 

st.markdown("This is a markdown") #bu markdown cift yildizla kullanildiginda streamlit te bold yazmani saglar

st.markdown("**This is a markdown** bu yildizli olan bold yapar") #bu markdown cift yildizla kullanildiginda streamlit te bold yazmani saglar


#colorful text

#classification ile cancer li hucere  tahmini yapiyorsun dusun  ozaman kullanilabilir hoca birazdan kirmizisini da gosterecegim dedi

st.success("Succesfull")
st.info("This is information")




#hwarning-error

st.warning("This is a warning ")
st.error("Stop... That give a error") #genelde neagtif bir durumu yazraken kullanilir



#get help

st.help(range)



#video dosyasi nasil cagirilir

#importing video

# my_video = open("intro-1.mp4","rb") #once dosyayi cagiriyorsun

# st.video("my_video") #bununla da 

#ya da direk youtube vs yerden linkle alabilirisn

#st.video("http://www.youtube.com") #olmazsa tirnagi tek yap



#select box

#bunun multi selectiondan farki 1 tane seciyorsun radio dan farki ise radio 

path = st.selectbox("Your path is ", ["DS", "FS", "AWS/DevOps"])
st.write("Your path is", path)

#meslea arab sitesi sinde adam diyeceksinizki arabani sec


#multiselect   dropdown olusturur ve secenekleri ekler  ve select  islemini de yapar coklu secim de yapabilioyorsun


profession = st.multiselect("Select your profession",["Engineer", "Teacher", "Nurse", "IT"])
st.write("Your profession is ", profession)


#slider

count = st.slider("How many years of experience in IT", 1,10)

count = st.slider("How many years of experience in IT", 1,10,2,(2))


#button

# st.button("Press this button") #bunu mesela adama butun featurelari giridikten sonra prediction yaparken kullanabilirisin



#st.button("Press this button")


if st.button("About Program"):
    st.text("Streamlit is easy and fun")
else: 
    st.text("Nothing to say")
    
#biz bunu programi run et demek icin kullanacagiz





#text input

firstname = st.text_input("Enter your namet:")

if st.button("Submit"):
    st.success(firstname.title()) #title sayesinde ilk harfi buyuk yazdi inputu kucuk harfle girsen bile
    

    
    
#text area metin alani olusturma

#message = st.text_area("Enter your message:","type right here..")
#if st.button("Submit"):  #buradki submit buyuk olursa hata verir cunku yukarda da ayni birebir ayni submit var
#    st.info(message.title())
    
message = st.text_area("Enter your message:","type right here..")
if st.button("submit"):  
    st.info(message.title())
    
    

    
    
#date input
import datetime
today = st.date_input("Today is",datetime.datetime.now())


#metin ve rakam seklinde input 

st.text_input("First name")
st.number_input("pick a number",0,10)


#raw data 

#bu da code seklinde yazdirmak ici kullnilir

#tek satir ayzdiri

st.text("display text")
st.code("import pandas as pd")

#ust sute birkac satir coode yazdirmak icn 

#multiple line code
#mesela makalelerde boyle yazilir

with st.echo():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    
    
    
    
# sidebar

st.sidebar.title("This is a sidebar")
    
    
    
#Latex formatinda matematiksle ifadeler ekler    
st.latex("E = mc^2")



#Dosya yukleme
import pandas as pd

    
    
    
#Dosya yukleme widgetini yukleyin


upload_file = st.file_uploader("Advertising.csv", type = ["csv"])


#Eger bir dosya yuklendiysa bu dosyayi pandas ile okuyun 



#if uploaded_file is not None:
#    data = pd.read_csv(uploaded_file)
#    st.write(data) #Dataframe i ekrana yazdir hoca bu bir metod dedi ama ekndisi 2 inic metodu da gosterdi

    

#-------------------------------------------------------

#Burda dosyayi dogrudan pandas la okuyacagiz dosya ayni dizinde olmali

data = pd.read_csv("Advertising.csv")

#DataFrame i ekrana yazdir

st.write(data)




#Plotly ile bir sactter plot olusturalim orengin TV reklam butcesi ile staislari karsiasiralim 


import plotly.express as px


fig = px.scatter(data, x= "TV",y = "sales",title = "TV Reklamlari vs. Satislar")
st.plotly_chart(fig)



#Vega Lite ile bir bar cahrt olusturalim Ornegin radyo reklam butcesinin ortalmasini gosterelim 


bar_chart = {
    "mark":"bar",
    "encoding":{
        "x":{"field":"radio", "bin":True,
             "type":"quantitative"},
        "y":{"aggregate":"average",
             "field":"sales","type":"quantitative"}
    }
}

st.vega_lite_chart(data, bar_chart)




#st.pyplot(): Bu fonksiyon, Matplotlib ile oluşturulan grafikleri göstermek için kullanılır. Örneğin, TV reklam bütçesi ile satışları bir scatter plot ile gösterelim:


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.scatter(data['TV'], data['sales'], color='blue')
plt.title('TV Reklamları vs. Satışlar')
plt.xlabel('TV Reklam Bütçesi')
plt.ylabel('Satışlar')
st.pyplot(plt)




st.markdown(
   """
   <div style='background-color: orange; padding: 10px;'>
   <h1 style='color: white; text-align: center;'>Streamlit Arayüzü</h1>
   </div>
   """,
   unsafe_allow_html=True
)
    
    