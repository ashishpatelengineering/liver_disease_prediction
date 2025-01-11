 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache_data()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio):   
 
    # Pre-processing user input    
    if Gender == "Female":
        Gender = 0
    else:
        Gender = 1
 
    
      
    # Making predictions 
    prediction = classifier.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
        
     
    if prediction == 0:
        pred = 'Liver disease not detected'
    else:
        pred = 'Liver disease detected'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       

    # display the front end aspect
    st.title(":orange[Liver Disease Prediction]") 

    st.markdown("""
                Liver disease is becoming increasingly common due to factors such as excessive alcohol consumption, inhalation of harmful gases, consumption of contaminated food, pickles, and drug use. 

                To address this, we have developed a prediction model using a **random forest classifier** to assess the potential risk of liver disease in patients based on specific parameters.

                The dataset used in this application includes records collected from the **North East region of Andhra Pradesh, India**. It comprises **583 records of patients with liver disease** and **167 records of patients without liver disease**.

                Explore this app to understand liver disease risk factors and make informed predictions.
                """)
    # following lines create boxes in which user can enter data required to make prediction 
    
    Gender = st.selectbox(':orange[Gender]',("Female","Male")) 
    Age = st.number_input( ":orange[Age (5.00 - 90.00)]" )
    Total_Bilirubin = st.number_input( ":orange[Total Bilirubin (0.50 - 75.00)]" )
    Direct_Bilirubin = st.number_input( ":orange[Direct Bilirubin (0.10 - 20.00)]" )
    Alkaline_Phosphotase = st.number_input( ":orange[Alkaline Phosphotase (50 - 2000)]" )
    Alamine_Aminotransferase = st.number_input( ":orange[Alamine Aminotransferase (10 - 2000)]" )
    Aspartate_Aminotransferase = st.number_input( ":orange[Aspartate Aminotransferase (10 - 5000)]" )
    Total_Protiens = st.number_input( ":orange[Total Protiens (1.00 to 10.00)]")
    Albumin = st.number_input( ":orange[Albumin (0.50 to 5.50)]" )
    Albumin_and_Globulin_Ratio = st.number_input( ":orange[Albumin and Globulin_Ratio (0.1 - 3.0)]" )

    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio) 
        st.success('Report Results: {}'.format(result))
        
     
if __name__=='__main__': 
    main()
