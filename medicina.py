import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulados
np.random.seed(42)
n_samples = 100

data = {
    'age': np.random.randint(20, 80, size=n_samples),
    'blood_sugar': np.random.uniform(70, 180, size=n_samples),
    'cholesterol': np.random.uniform(150, 300, size=n_samples),
    'genotype': np.random.choice(['AA', 'AG', 'GG'], size=n_samples)
}

df = pd.DataFrame(data)

# Lógica de recomendaciones
def get_health_recommendation(age, blood_sugar, cholesterol, genotype):
    recommendations = []

    # Recomendaciones basadas en la edad
    if age < 30:
        recommendations.append("Realiza ejercicio regularmente y mantén una dieta equilibrada.")
    elif age < 50:
        recommendations.append("Controla tu presión arterial y revisa tus niveles de colesterol.")
    else:
        recommendations.append("Consulta a tu médico regularmente y realiza chequeos de salud frecuentes.")

    # Recomendaciones basadas en el nivel de azúcar en sangre
    if blood_sugar > 140:
        recommendations.append("Reduce la ingesta de azúcares y carbohidratos refinados.")
    else:
        recommendations.append("Mantén una dieta equilibrada y monitorea tu nivel de azúcar regularmente.")

    # Recomendaciones basadas en el colesterol
    if cholesterol > 200:
        recommendations.append("Evita alimentos ricos en grasas saturadas y colesterol.")
    else:
        recommendations.append("Mantén una dieta rica en fibra y grasas saludables.")

    # Recomendaciones basadas en el genotipo
    if genotype == 'AA':
        recommendations.append("Considera realizar pruebas genéticas adicionales.")
    elif genotype == 'AG':
        recommendations.append("Mantén un estilo de vida saludable y consulta a un genetista si tienes dudas.")
    else:
        recommendations.append("No se requieren acciones adicionales basadas en el genotipo.")

    return recommendations

# Interfaz de usuario con Streamlit
st.title("Recomendaciones de Salud Personalizadas")

st.sidebar.header("Ingrese sus datos")
# Formularios para la entrada de datos del usuario
age = st.sidebar.slider("Edad", 20, 80, 30)
blood_sugar = st.sidebar.slider("Nivel de Azúcar en Sangre (mg/dL)", 70, 180, 100)
cholesterol = st.sidebar.slider("Colesterol (mg/dL)", 150, 300, 200)
genotype = st.sidebar.selectbox("Genotipo", ["AA", "AG", "GG"])

# Botón para generar recomendaciones
if st.sidebar.button("Obtener Recomendaciones"):
    recommendations = get_health_recommendation(age, blood_sugar, cholesterol, genotype)
    st.subheader("Recomendaciones de Salud")
    for rec in recommendations:
        st.write(f"- {rec}")

# Mostrar gráficos de distribución de datos simulados
st.subheader("Distribución de Datos Simulados")

fig, ax = plt.subplots(3, 1, figsize=(10, 15))
ax[0].hist(df['age'], bins=20, color='skyblue')
ax[0].set_title('Distribución de la Edad')
ax[0].set_xlabel('Edad')
ax[0].set_ylabel('Frecuencia')

ax[1].hist(df['blood_sugar'], bins=20, color='lightgreen')
ax[1].set_title('Distribución del Nivel de Azúcar en Sangre')
ax[1].set_xlabel('Nivel de Azúcar en Sangre (mg/dL)')
ax[1].set_ylabel('Frecuencia')

ax[2].hist(df['cholesterol'], bins=20, color='salmon')
ax[2].set_title('Distribución del Colesterol')
ax[2].set_xlabel('Colesterol (mg/dL)')
ax[2].set_ylabel('Frecuencia')

st.pyplot(fig)

# Mostrar una tabla de los datos simulados
st.subheader("Datos Simulados")
st.dataframe(df)
