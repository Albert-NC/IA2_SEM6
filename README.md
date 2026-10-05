# 🫁 LAB_IA_SEM6: Sistema Experto Médico en Neumología

Aplicación de Sistema Experto en Salud para el **Laboratorio de la Semana 6 (Punto 4)** del curso de **Inteligencia Artificial II**.

Designada para ser subida a **GitHub** y desplegada en **Vercel** o **Streamlit**.

---

## 📋 Características de la Solución (Punto 4 de la Guía)

1. **Delimitación de Especialidad Médica:**
   - **Neumología & Triaje Respiratorio Agudo** (Neumonía Adquirida en la Comunidad, Neumotórax Espontáneo, Tromboembolismo Pulmonar, Crisis de Asma Bronquial, EPOC Exacerbado, Bronquitis Aguda, TBC Pulmonar, etc.).

2. **Estructura Adaptativa:**
   - **Paso 1 (Perfil):** Edad, Hábito tabáquico / exposición a biomasa, Antecedentes de asma/EPOC.
   - **Paso 2 (Motivo Principal):** Selección del síntoma cardinal (Tos/Fiebre, Disnea, Sibilancias, Dolor Pleurítico).
   - **Paso 3 (Ramificación):** Casillas de verificación (todo para marcar) correspondientes al síntoma elegido.
   - **Paso 4 (Asociados):** Sintomatología sistémica concomitante.
   - **Paso 5 (Vitales):** Medición de $SpO_2\%$ y temperatura corporal.
   - **Paso 6 (Alarma):** Valoración de signos de compromiso hemodinámico.
   - **Paso 7 (Dictamen):** Diagnóstico presuntivo de mayor probabilidad, Factor de Certeza ($CF\%$), recomendación de triaje, exámenes auxiliares sugeridos y descargo médico.

---

## 🚀 Despliegue en Vercel (Web App)

```bash
cd Lab_IA_SEM6
git add .
git commit -m "feat: Sistema Experto Neumológico"
git push origin main
```
Luego importar en [vercel.com](https://vercel.com) para obtener tu link público al instante.

---

## 🐍 Ejecución Local en Streamlit (Python)

```bash
cd Lab_IA_SEM6
pip install streamlit
streamlit run app.py
```
