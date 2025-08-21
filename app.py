%%writefile app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Título de la aplicación
st.title('Dashboard de Marketing Digital 📈')
st.write('Analizando métricas clave para la optimización de la estrategia.')

# Carga de los datos (simulada)
df = pd.read_csv('fake_data.csv')
df['date'] = pd.to_datetime(df['date'])
tipos_de_contenido = ['Video', 'Imagen', 'Carrusel']
df['content_type'] = np.random.choice(tipos_de_contenido, size=len(df), p=[0.4, 0.4, 0.2])
df['day_of_week'] = df['date'].dt.day_name()
df['engagement_rate (%)'] = (df['likes'] + df['comments'] + df['shares']) / df['views'] * 100

# Gráfico 1: Evolución de Seguidores
st.subheader('1. Evolución de Seguidores')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='date', y='followers', data=df)
plt.title('Evolución del Número de Seguidores a lo largo del Tiempo')
st.pyplot(fig1)

# Gráfico 2: Distribución de Métricas
st.subheader('2. Distribución de Métricas')
fig2, ax2 = plt.subplots(figsize=(15, 8))
plt.subplot(2, 2, 1)
sns.histplot(df['likes'], kde=True)
plt.title('Distribución de Likes')
plt.subplot(2, 2, 2)
sns.histplot(df['comments'], kde=True)
plt.title('Distribución de Comentarios')
plt.subplot(2, 2, 3)
sns.histplot(df['shares'], kde=True)
plt.title('Distribución de Compartidos')
plt.tight_layout()
st.pyplot(fig2)

# Gráfico 3: Relación entre Vistas y Likes
st.subheader('3. Relación entre Vistas y Likes')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='views', y='likes', data=df)
plt.title('Relación entre Vistas y Likes')
st.pyplot(fig3)

# Gráfico 4: Comparación de Métricas
st.subheader('4. Comparación de Métricas')
fig4, ax4 = plt.subplots(figsize=(12, 6))
metricas_df = df[['likes', 'comments', 'shares', 'views', 'impressions', 'reach']]
metricas_df.sum().plot(kind='bar', color=sns.color_palette('viridis'))
plt.title('Comparación de Métricas Totales')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
st.pyplot(fig4)

# Gráfico 5: Top 10 Publicaciones
st.subheader('5. Top 10 Publicaciones')
top_posts = df.sort_values(by='likes', ascending=False).head(10)
fig5, ax5 = plt.subplots(figsize=(12, 6))
sns.barplot(x='likes', y='date', data=top_posts, palette='magma')
plt.title('Top 10 Publicaciones por Likes')
st.pyplot(fig5)


# Gráfico 6: Rendimiento del Engagement por Tipo de Contenido
st.subheader('6. Rendimiento del Engagement por Tipo de Contenido')
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='content_type', y='engagement_rate (%)', data=df, palette='pastel')
plt.title('Rendimiento del Engagement por Tipo de Contenido')
plt.xlabel('Tipo de Contenido')
plt.ylabel('Tasa de Engagement (%)')
st.pyplot(fig6)

# Gráfico 7: Engagement Promedio por Día de la Semana
st.subheader('7. Engagement Promedio por Día de la Semana')
dias_ordenados = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fig7, ax7 = plt.subplots(figsize=(12, 6))
sns.barplot(
    x='day_of_week',
    y='engagement_rate (%)',
    data=df,
    order=dias_ordenados,
    palette='coolwarm',
    estimator=np.mean,
    errorbar=None
)
plt.title('Engagement Promedio por Día de la Semana')
plt.xlabel('Día de la Semana')
plt.ylabel('Tasa de Engagement Promedio (%)')
plt.xticks(rotation=45)
st.pyplot(fig7)

# Gráfico 8: Matriz de Correlación General
st.subheader('8. Matriz de Correlación General')
df_numerico = df.select_dtypes(include=['number'])
correlation_matrix = df_numerico.corr()
fig8, ax8 = plt.subplots(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor de Correlación entre Métricas')
st.pyplot(fig8)

# Sección de conclusiones
st.subheader('Conclusiones')
st.write('---')
st.write('Este dashboard es un ejemplo de cómo transformar un análisis técnico en una herramienta de negocio funcional. La metodología utilizada demuestra mi capacidad para generar **insights accionables** que impulsan el crecimiento empresarial.')
