import streamlit as st

# ====================================================================
# NEUMOEXPERT AI - STREAMLIT APP
# Especialidad: Neumología & Triaje Respiratorio
# ====================================================================

st.set_page_config(
    page_title="NeumoExpert - Sistema Experto Médico",
    page_icon="🫁",
    layout="wide"
)

# Estilos CSS de Neumología con Contraste a Prueba de Errores (Dark/Light Mode)
st.markdown("""
<style>
    * {
        border-radius: 0px !important;
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 900;
        color: #0284C7 !important;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #64748B !important;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }
    .level-box {
        background-color: #0F172A !important;
        border: 1px solid #0284C7 !important;
        border-left: 6px solid #0284C7 !important;
        padding: 1.3rem 1.6rem;
        margin-bottom: 1.5rem;
        color: #F8FAFC !important;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2);
    }
    .level-box h3 {
        color: #38BDF8 !important;
        font-weight: 900;
        font-size: 1.4rem;
        margin-bottom: 0.4rem;
    }
    .level-box p {
        color: #CBD5E1 !important;
        font-size: 0.95rem;
        margin: 0;
    }
    .result-card {
        background-color: #0F172A !important;
        border: 2px solid #F59E0B !important; /* BORDE DORADO AMBER */
        padding: 1.75rem;
        color: #F8FAFC !important;
        box-shadow: 0 0 30px rgba(245, 158, 11, 0.25);
    }
    .disease-title-highlight {
        color: #FBBF24 !important; /* COLOR AMBER NEÓN LLAMATIVO */
        font-weight: 900 !important;
        font-size: 2.1rem !important;
        text-shadow: 0 0 15px rgba(251, 191, 36, 0.4);
    }
    .cf-badge-lg {
        background: linear-gradient(135deg, #F59E0B, #D97706);
        color: #FFFFFF !important;
        padding: 8px 20px;
        font-weight: 900;
        font-size: 1.5rem;
        border: 1px solid #FBBF24;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.5);
        display: inline-block;
    }
    .disclaimer-box {
        background-color: #78350F !important;
        border: 1.5px solid #F59E0B !important;
        padding: 14px 18px;
        font-size: 0.9rem;
        color: #FEF3C7 !important;
        margin-top: 1.5rem;
        font-weight: 600;
    }
    .exam-tag {
        background-color: #1E293B;
        color: #38BDF8;
        border: 1px solid #0284C7;
        padding: 4px 10px;
        font-size: 0.85rem;
        display: inline-block;
        margin-top: 4px;
        margin-right: 4px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🫁 NeumoExpert AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Sistema Experto Médico | Especialidad: <strong>Neumología &amp; Triaje Respiratorio</strong></div>', unsafe_allow_html=True)

st.sidebar.image("https://img.icons8.com/color/96/lungs.png", width=70)
if st.sidebar.button("🔄 Reiniciar Diagnóstico"):
    st.session_state.clear()
    st.rerun()

if "nivel" not in st.session_state:
    st.session_state.nivel = 1

# --------------------------------------------------------------------
# NIVEL 1: PERFIL DEMOGRÁFICO
# --------------------------------------------------------------------
if st.session_state.nivel == 1:
    st.markdown('<div class="level-box"><h3>📍 Paso 1: Perfil Demográfico y Riesgos</h3><p>Ingrese los antecedentes epidemiológicos fundamentales.</p></div>', unsafe_allow_html=True)
    edad = st.number_input("Edad del paciente", min_value=1, max_value=110, value=45)
    fumador = st.selectbox("Hábito tabáquico / exposición a biomasa", ["No fumador / Sin exposición", "Fumador moderado / Exposición ocasional", "Fumador pesado (>10 cig/día / Leña)"])
    antecedente = st.selectbox("Antecedente patológico principal", ["Ninguno", "Asma Bronquial previa", "EPOC / Bronquitis Crónica", "Enfermedad Cardiovascular / Trombosis"])
    
    if st.button("Siguiente Paso ➡️", type="primary"):
        st.session_state.edad = edad
        st.session_state.fumador = fumador
        st.session_state.antecedente = antecedente
        st.session_state.nivel = 2
        st.rerun()

# --------------------------------------------------------------------
# NIVEL 2: MOTIVO PRINCIPAL
# --------------------------------------------------------------------
elif st.session_state.nivel == 2:
    st.markdown('<div class="level-box"><h3>📍 Paso 2: Motivo Principal de Consulta Respiratoria</h3><p>Seleccione el síntoma cardinal que predomina en el paciente.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌡️ Rama A: Tos con Flema y Fiebre", use_container_width=True):
            st.session_state.camino = "tos_fiebre"
            st.session_state.nivel = 3
            st.rerun()
        if st.button("🌬️ Rama B: Dificultad para Respirar (Disnea)", use_container_width=True):
            st.session_state.camino = "disnea"
            st.session_state.nivel = 3
            st.rerun()
    with col2:
        if st.button("🔊 Rama C: Silbidos en el Pecho (Sibilancias)", use_container_width=True):
            st.session_state.camino = "sibilancias"
            st.session_state.nivel = 3
            st.rerun()
        if st.button("🫁 Rama D: Dolor Torácico Pleurítico", use_container_width=True):
            st.session_state.camino = "dolor_pleuritico"
            st.session_state.nivel = 3
            st.rerun()

# --------------------------------------------------------------------
# NIVEL 3: DETALLE DE RAMA
# --------------------------------------------------------------------
elif st.session_state.nivel == 3:
    camino = st.session_state.get("camino", "tos_fiebre")
    st.markdown(f'<div class="level-box"><h3>🌿 Paso 3: Detalle Semiológico Específico ({camino.upper()})</h3><p>Marque las casillas de los hallazgos observados.</p></div>', unsafe_allow_html=True)
    
    if camino == "tos_fiebre":
        chk1 = st.checkbox("Esputo purulento (amarillento/verdoso) + inicio brusco con escalofríos intensos")
        chk2 = st.checkbox("Tos seca o con flema transparente + congestión nasal, coriza y mialgias")
        chk3 = st.checkbox("Tos continua >2-3 semanas + sudoración nocturna y esputo con estrías de sangre")
        chk4 = st.checkbox("Tos productiva con esputo fétido abundante + picos febriles continuos")
    elif camino == "disnea":
        chk1 = st.checkbox("Aparición súbita e instantánea (segundos/minutos) con dolor punzante en un lado del tórax")
        chk2 = st.checkbox("Inicio súbito post-reposo prolongado / viaje largo / cirugía reciente + taquicardia")
        chk3 = st.checkbox("Dificultad progresiva en días/semanas en paciente fumador habitual")
        chk4 = st.checkbox("Dificultad progresiva con tos seca en crepitantes tipo Velcro al auscultar")
    elif camino == "sibilancias":
        chk1 = st.checkbox("Crisis recurrentes por alérgenos/ejercicio/frío que mejoran con Salbutamol")
        chk2 = st.checkbox("Silbidos constantes con tos matutina diaria y expectoración en fumador mayor de 40 años")
        chk3 = st.checkbox("Primer episodio de silbidos en el pecho posterior a resfrío/cuadro viral reciente")
        chk4 = st.checkbox("Silbidos inspiratorios y espiratorios con estridor alto")
    else: # dolor_pleuritico
        chk1 = st.checkbox("Dolor en puntada de costado que empeora al inspirar profundo o toser + fiebre")
        chk2 = st.checkbox("Dolor agudo unilateral con asimetría al expandir tórax y ausencia de ruidos")
        chk3 = st.checkbox("Dolor pleurítico repentino + hemoptisis (tos con sangre) o mareo postural")
        chk4 = st.checkbox("Dolor torácico subesternal opresivo/pleurítico que alivia al inclinarse hacia adelante")
        
    if st.button("Siguiente Paso ➡️", type="primary"):
        st.session_state.opcion_chk1 = chk1
        st.session_state.opcion_chk2 = chk2
        st.session_state.opcion_chk3 = chk3
        st.session_state.opcion_chk4 = chk4
        st.session_state.nivel = 4
        st.rerun()

# --------------------------------------------------------------------
# NIVEL 4: SÍNTOMAS ASOCIADOS
# --------------------------------------------------------------------
elif st.session_state.nivel == 4:
    st.markdown('<div class="level-box"><h3>📋 Paso 4: Sintomatología Sistémica Concomitante</h3><p>Marque las manifestaciones clínicas adicionales presentes.</p></div>', unsafe_allow_html=True)
    sudor = st.checkbox("Sudoración nocturna profusa (empapa la ropa)")
    mialgias = st.checkbox("Mialgias / Artralgias (dolores musculares y articulares)")
    cefalea = st.checkbox("Cefalea intensa u holocraneal")
    perdidapeso = st.checkbox("Pérdida de peso progresiva no intencionada")
    hemoptisis = st.checkbox("Hemoptisis (flema con estrías o rasgos de sangre)")
    
    if st.button("Siguiente Paso ➡️", type="primary"):
        st.session_state.sudor = sudor
        st.session_state.mialgias = mialgias
        st.session_state.perdidapeso = perdidapeso
        st.session_state.hemoptisis = hemoptisis
        st.session_state.nivel = 5
        st.rerun()

# --------------------------------------------------------------------
# NIVEL 5: VITALES
# --------------------------------------------------------------------
elif st.session_state.nivel == 5:
    st.markdown('<div class="level-box"><h3>📊 Paso 5: Constantes Fisiológicas y Parámetros Vitales</h3><p>Ingrese los valores numéricos de oximetría y temperatura.</p></div>', unsafe_allow_html=True)
    spo2 = st.number_input("Saturación de Oxígeno (SpO2 %)", min_value=50, max_value=100, value=95)
    temp = st.number_input("Temperatura Corporal (°C)", min_value=35.0, max_value=42.0, value=38.2, step=0.1)
    
    if st.button("Siguiente Paso ➡️", type="primary"):
        st.session_state.spo2 = spo2
        st.session_state.temp = temp
        st.session_state.nivel = 6
        st.rerun()

# --------------------------------------------------------------------
# NIVEL 6: ALARMA
# --------------------------------------------------------------------
elif st.session_state.nivel == 6:
    st.markdown('<div class="level-box"><h3>🚨 Paso 6: Valoración de Signos de Alarma y Severidad</h3><p>Verifique la presencia de signos de compromiso hemodinámico.</p></div>', unsafe_allow_html=True)
    cianosis = st.checkbox("Cianosis (Coloración azulada en labios o uñas)")
    tiraje = st.checkbox("Tiraje intercostal (Uso activo de músculos accesorios)")
    taquipnea = st.checkbox("Taquipnea severa (>24 respiraciones/minuto)")
    confusion = st.checkbox("Desorientación / Confusión / Letargia")
    
    if st.button("Calcular Dictamen Presuntivo ⚙️", type="primary"):
        st.session_state.cianosis = cianosis
        st.session_state.tiraje = tiraje
        st.session_state.taquipnea = taquipnea
        st.session_state.confusion = confusion
        st.session_state.nivel = 7
        st.rerun()

# --------------------------------------------------------------------
# NIVEL 7: DICTAMEN PRESUNTIVO
# --------------------------------------------------------------------
elif st.session_state.nivel == 7:
    st.markdown('<div class="level-box"><h3>🏁 Dictamen Presuntivo del Motor de Inferencia</h3><p>Resultado generado mediante encadenamiento lógico por reglas.</p></div>', unsafe_allow_html=True)
    
    camino = st.session_state.get("camino", "tos_fiebre")
    chk1 = st.session_state.get("opcion_chk1", False)
    chk2 = st.session_state.get("opcion_chk2", False)
    chk3 = st.session_state.get("opcion_chk3", False)
    chk4 = st.session_state.get("opcion_chk4", False)
    
    spo2 = st.session_state.get("spo2", 95)
    temp = st.session_state.get("temp", 38.2)
    fumador = st.session_state.get("fumador", "No fumador")
    antecedente = st.session_state.get("antecedente", "Ninguno")
    sudor = st.session_state.get("sudor", False)
    perdidapeso = st.session_state.get("perdidapeso", False)
    cianosis = st.session_state.get("cianosis", False)
    tiraje = st.session_state.get("tiraje", False)
    confusion = st.session_state.get("confusion", False)
    
    cf = 74
    if spo2 < 92: cf += 12
    if temp >= 38.5: cf += 8
    if cianosis or tiraje: cf += 4
    cf = min(98, cf)
    
    # Inferencia por casillas marcadas
    if chk1 and camino == "tos_fiebre":
        diag = "Neumonía Adquirida en la Comunidad (NAC)"
        desc = "Cuadro infeccioso e inflamatorio agudo del parénquima pulmonar caracterizado por exudado alveolar bacteriano."
        triaje = "🚨 EMERGENCIA CRÍTICA" if (spo2 < 92 or confusion) else "⚠️ URGENTE"
        exams = ["Radiografía de Tórax AP y Lat", "Hemograma + PCR / VSG", "Cultivo de expectoración y Gram", "Gasometría Arterial"]
        rules = ["R-NEUMO-01: Expectoración purulenta", "R-NEUMO-02: Fiebre con escalofríos"]
        conducta = "Evaluación prioritaria para inicio de cobertura antibiótica empírica. Oxigenoterapia si SpO2 < 92%."

    elif chk4 and camino == "tos_fiebre":
        diag = "Absceso Pulmonar / Neumonía Necrosante"
        desc = "Lesión cavitada necrosante en el parénquima pulmonar causada por aspiración de anaerobios."
        triaje = "🚨 EMERGENCIA CRÍTICA"
        exams = ["Tomografía Computarizada de Tórax", "Cultivo de expectoración para Anaerobios", "Broncoscopía diagnóstica"]
        rules = ["R-ABSC-01: Expectoración fétida vómica", "R-ABSC-02: Picos febriles continuos"]
        conducta = "Hospitalización e inicio inmediato de antibióticoterapia EV de amplio espectro para anaerobios."

    elif chk2 and camino == "tos_fiebre":
        diag = "Infección Respiratoria Aguda Viral (SRA / COVID-19 / Influenza)"
        desc = "Compromiso mucoso inflamatorio autolimitado de vías aéreas superiores e inferiores de origen viral."
        triaje = "⚠️ URGENTE" if spo2 < 92 else "🟢 LEVE / MODERADO"
        exams = ["Panel Viral Respiratorio (RT-PCR)", "Hemograma completo", "Oximetría de pulso continua"]
        rules = ["R-VIRAL-01: Tos seca con coriza", "R-VIRAL-02: Síntomas sistémicos mialgias"]
        conducta = "Manejo sintomático con analgésicos, hidratación adecuada, aislamiento preventivo y monitoreo de SpO2."

    elif chk3 and camino == "tos_fiebre" or (sudor and perdidapeso):
        diag = "Tuberculosis Pulmonar / Proceso Granulomatoso Crónico"
        desc = "Infección bacilar crónica por Mycobacterium tuberculosis con compromiso parenquimatoso cavitario."
        triaje = "⚠️ URGENTE (Prioridad de Aislamiento)"
        exams = ["Baciloscopía seriada de esputo (BK x3)", "Prueba molecular GeneXpert MTB/RIF", "Radiografía de Tórax AP"]
        rules = ["R-TBC-01: Tos de más de 15 días", "R-TBC-02: BASS / Sudoración nocturna"]
        conducta = "Aislamiento respiratorio estricto con mascarilla N95 e inicio de Esquema Único Antituberculoso."

    elif chk1 and camino == "disnea":
        diag = "Neumotórax Espontáneo Agudo"
        desc = "Presencia de aire en el espacio pleural que genera colapso parcial o total del hemitórax pulmonar afectado."
        triaje = "🚨 EMERGENCIA CRÍTICA"
        exams = ["Radiografía de Tórax en Espiración Forzada", "Gasometría Arterial", "Tomografía de Tórax"]
        rules = ["R-PLEURA-01: Disnea súbita e instantánea", "R-PLEURA-02: Dolor torácico unilateral agudo"]
        conducta = "Transferencia inmediata a trauma-shock para descompresión pleural urgente y tubo de drenaje."

    elif chk2 and camino == "disnea":
        diag = "Tromboembolismo Pulmonar Agudo (TEP)"
        desc = "Oclusión del árbol arterial pulmonar por un trombo desplazado desde el sistema venoso profundo."
        triaje = "🚨 EMERGENCIA CRÍTICA"
        exams = ["Angio-TAC de Arterias Pulmonares", "Dímero D en sangre", "Electrocardiograma (Patrón S1Q3T3)"]
        rules = ["R-TEP-01: Disnea súbita post-reposo", "R-TEP-02: Taquicardia + Dolor pleurítico"]
        conducta = "Atención médica de emergencia inmediata. Anticoagulación parenteral con Heparina / Trombólisis en UCI."

    elif chk3 and camino == "disnea" or antecedente == "EPOC / Bronquitis Crónica":
        diag = "Exacerbación de Enfermedad Pulmonar Obstructiva Crónica (EPOC)"
        desc = "Empeoramiento agudo e inestable de la limitación al flujo aéreo bronquial en paciente tabáquico."
        triaje = "🚨 EMERGENCIA CRÍTICA" if spo2 < 88 else "⚠️ URGENTE"
        exams = ["Gasometría Arterial", "Radiografía de Tórax AP", "Cultivo de expectoración"]
        rules = ["R-EPOC-01: Disnea en fumador crónico", "R-EPOC-02: Expectoración aumentada"]
        conducta = "Broncodilatadores nebulizados (Salbutamol + Ipratropio), corticoides sistémicos y oxigenoterapia Venturi."

    elif chk4 and camino == "disnea":
        diag = "Exacerbación de Fibrosis Pulmonar / Enfermedad Intersticial (EPID)"
        desc = "Compromiso inflamatorio y fibroso del intersticio pulmonar con estertores crepitantes secos tipo Velcro."
        triaje = "🚨 EMERGENCIA CRÍTICA" if spo2 < 90 else "⚠️ URGENTE"
        exams = ["Tomografía Computarizada de Alta Resolución (TACAR)", "Gasometría Arterial"]
        rules = ["R-EPID-01: Crepitantes secos Velcro", "R-EPID-02: Disnea progresiva restrictiva"]
        conducta = "Evaluación especializada en neumología para pulsos de corticoides y oxigenoterapia suplementaria."

    elif chk1 and camino == "sibilancias" or antecedente == "Asma Bronquial previa":
        diag = "Crisis de Asma Bronquial (Exacerbación Aguda de Asma)"
        desc = "Hiperreactividad inflamatoria bronquial reversible caracterizada por broncoconstricción e hipersecreción."
        triaje = "🚨 EMERGENCIA" if (spo2 < 92 or tiraje) else "⚠️ URGENTE"
        exams = ["Flujometría (Peak Flow)", "Gasometría Arterial", "Radiografía de Tórax"]
        rules = ["R-ASMA-01: Sibilancias recurrentes", "R-ASMA-02: Respuesta favorable a beta-2 agonistas"]
        conducta = "Inhalación de β2-agonistas de acción corta (Salbutamol) cada 20 min + corticoides sistémicos."

    elif chk4 and camino == "sibilancias":
        diag = "Edema Laríngeo / Obstrucción de Vía Aérea Superior (Estridor)"
        desc = "Estrechamiento agudo subglótico o laringospasmo crítico que compromete el paso de aire alto."
        triaje = "🚨 EMERGENCIA CRÍTICA DE VÍA AÉREA"
        exams = ["Laringoscopía directa", "Oximetría continua"]
        rules = ["R-ESTRIDOR-01: Estridor inspiratorio", "R-ESTRIDOR-02: Obstrucción alta"]
        conducta = "Asegurar vía aérea de inmediato. Nebulización con Adrenalina racémica + Dexametasona EV."

    elif chk1 and camino == "dolor_pleuritico":
        diag = "Pleuresía Fibrinosa / Derrame Pleural Inflamatorio"
        desc = "Inflamación de las hojas pleurales parietal y visceral con fricción dolorosa pleurítica al inspirar."
        triaje = "⚠️ URGENTE"
        exams = ["Ecografía Pleural", "Radiografía de Tórax", "Toracocentesis diagnóstica"]
        rules = ["R-PLEUR-01: Dolor pleurítico en puntada", "R-PLEUR-02: Roce pleural auscultatorio"]
        conducta = "Analgesia antiinflamatoria (AINEs), descarte de neumonía subyacente y toracocentesis."

    elif chk4 and camino == "dolor_pleuritico":
        diag = "Pericarditis Aguda con Compromiso Pleuropericárdico"
        desc = "Inflamación del saco pericárdico que genera dolor torácico pleurítico sensible al cambio postural."
        triaje = "🚨 EMERGENCIA"
        exams = ["Electrocardiograma", "Ecocardiograma", "Enzimas cardíacas (Troponinas)"]
        rules = ["R-PERI-01: Dolor post-inclinación", "R-PERI-02: Frote pericárdico"]
        conducta = "Atención cardiológica urgente, ECG de 12 derivaciones, analgesia con AINEs y ecocardiograma."

    else:
        diag = "Bronquitis Aguda / Síndrome Bronquial Obstructivo (SBO)"
        desc = "Inflamación agudo-progresiva del árbol bronquial principal de evolución autolimitada."
        triaje = "🟢 LEVE / MODERADO"
        exams = ["Auscultación pulmonar clínica", "Oximetría de pulso"]
        rules = ["R-BRONQ-01: Broncospasmo post-viral"]
        conducta = "Manejo ambulatorio con hidratación, antipiréticos e inhaladores de rescate si hay espasmo."

    st.markdown(f"""
    <div class="result-card">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:1.5rem;">
            <div>
                <span style="color:#F59E0B; font-weight:900; font-size:0.85rem; text-transform:uppercase;">DIAGNÓSTICO PRESUNTIVO DE MAYOR PROBABILIDAD</span>
                <h2 class="disease-title-highlight" style="margin-top:4px;">Es probable que presente: {diag}</h2>
            </div>
            <div style="text-align:right; flex-shrink:0;">
                <span style="color:#CBD5E1; font-size:0.75rem; font-weight:800; display:block; margin-bottom:4px; text-transform:uppercase;">CERTEZA DIAGNÓSTICA (CF)</span>
                <div class="cf-badge-lg">{cf}%</div>
            </div>
        </div>
        <hr style="border-color:#F59E0B; margin: 1.2rem 0;"/>
        <p><strong>Nivel de Triaje Recomendado:</strong> {triaje}</p>
        <p><strong>Descripción Fisiopatológica:</strong> {desc}</p>
        <p><strong>Exámenes Auxiliares Recomendados:</strong></p>
        <div>{" ".join([f'<span class="exam-tag">{e}</span>' for e in exams])}</div>
        <p style="margin-top:1rem;"><strong>Reglas Disparadas:</strong></p>
        <div>{" ".join([f'<span class="exam-tag" style="border-color:#818CF8; color:#C084FC;">{r}</span>' for r in rules])}</div>
        <p style="margin-top:1rem;"><strong>Conducta Médica Sugerida:</strong> {conducta}</p>
    </div>
    <div class="disclaimer-box">
        🩺 <strong>Nota médica informativa:</strong> Los resultados emitidos por este sistema experto representan únicamente una recomendación presuntiva y probabilística. Por favor, <strong>visite a su médico de preferencia</strong> para un diagnóstico presencial definitivo.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🔄 Nuevo Diagnóstico"):
        st.session_state.nivel = 1
        st.rerun()
