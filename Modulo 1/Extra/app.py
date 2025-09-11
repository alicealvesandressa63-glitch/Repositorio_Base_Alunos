import streamlit as st

# ---------------------------------------------- SIDEBAR

st.sidebar.image('logo.png')
st.sidebar.title('Cálculo de IMC')


# ---------------------------------------------- PRINCIPAL
st.title('Cálculo de IMC')

peso = st.text_input('Informe seu peso')
altura = st.text_input('Informe sua altura')

if st.button('Calcular'):


    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)


    if imc <= 18.5:
        classific = 'Você está abaixo do peso, procure um profissional.'

    elif imc <= 24.9:
        classific = 'Você está com o peso normal.'    
    elif imc <= 29.9:
        classific = 'Você está acima do peso, procure um profissional se for necessário.'
    elif imc <= 34.9:
        classific = ' Você está com Obesidade Grau 1, procure um profissional.'
    elif imc <= 39.9:
        classific = 'Você está com Obesidade Grau 2, ptocure um profissional.'
    else:
        classific = 'Você está com Obesidade Grau 3 procure um profissional.'
    
    
    st.warning(f'Seu IMC é: {imc:.2f}. {classific}')