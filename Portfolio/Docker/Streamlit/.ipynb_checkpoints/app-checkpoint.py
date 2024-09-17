import streamlit as st


#text/file
st.title("Streamlit Tutorial") #correspond to H1 heading
st.text("Hello Streamlit")   


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

st.text("display text")
st.code("import pandas as pd")
    
    