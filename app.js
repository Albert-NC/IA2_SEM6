/* ==================================================================== */
/* NEUMOEXPERT AI - SISTEMA EXPERTO EN NEUMOLOGÍA (7 NIVELES - BORDES)  */
/* Motor de Inferencia Multi-Casilla para Marcar (Checkboxes Engine)   */
/* ==================================================================== */

let selectedPathN2 = 'tos_fiebre';

document.addEventListener('DOMContentLoaded', () => {
    initThemeToggle();
    init7LevelSystem();
});

function initThemeToggle() {
    const themeBtn = document.getElementById('theme-toggle');
    const themeIcon = themeBtn ? themeBtn.querySelector('i') : null;
    const btnReset = document.getElementById('btn-reset-app');

    if (themeBtn) {
        themeBtn.addEventListener('click', () => {
            document.body.classList.toggle('light-theme');
            const isLight = document.body.classList.contains('light-theme');
            if (themeIcon) {
                themeIcon.className = isLight ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
            }
        });
    }

    if (btnReset) {
        btnReset.addEventListener('click', reiniciarApp);
    }
}

function init7LevelSystem() {
    // Selección de Camino en Nivel 2
    const pathCards = document.querySelectorAll('.path-option-card');
    pathCards.forEach(card => {
        card.addEventListener('click', () => {
            selectedPathN2 = card.getAttribute('data-path');
            configurarRamaNivel3(selectedPathN2);
            mostrarNivel(3);
        });
    });

    // Controles de botones de avance y retroceso
    const btnToN2 = document.getElementById('btn-to-n2');
    const btnBackN1 = document.getElementById('btn-back-n1');
    const btnBackN2 = document.getElementById('btn-back-n2');
    const btnToN4 = document.getElementById('btn-to-n4');
    const btnBackN3 = document.getElementById('btn-back-n3');
    const btnToN5 = document.getElementById('btn-to-n5');
    const btnBackN4 = document.getElementById('btn-back-n4');
    const btnToN6 = document.getElementById('btn-to-n6');
    const btnBackN5 = document.getElementById('btn-back-n5');
    const btnToN7 = document.getElementById('btn-to-n7');
    const btnRestartAll = document.getElementById('btn-restart-all');

    if (btnToN2) btnToN2.addEventListener('click', () => mostrarNivel(2));
    if (btnBackN1) btnBackN1.addEventListener('click', () => mostrarNivel(1));
    if (btnBackN2) btnBackN2.addEventListener('click', () => mostrarNivel(2));
    if (btnToN4) btnToN4.addEventListener('click', () => mostrarNivel(4));
    if (btnBackN3) btnBackN3.addEventListener('click', () => mostrarNivel(3));
    if (btnToN5) btnToN5.addEventListener('click', () => mostrarNivel(5));
    if (btnBackN4) btnBackN4.addEventListener('click', () => mostrarNivel(4));
    if (btnToN6) btnToN6.addEventListener('click', () => mostrarNivel(6));
    if (btnBackN5) btnBackN5.addEventListener('click', () => mostrarNivel(5));
    if (btnToN7) btnToN7.addEventListener('click', () => {
        mostrarNivel(7);
        calcularInferencia7Niveles();
    });
    if (btnRestartAll) btnRestartAll.addEventListener('click', reiniciarApp);
}

function mostrarNivel(numNivel) {
    const views = document.querySelectorAll('.level-view');
    const nodes = document.querySelectorAll('.step-node');

    views.forEach(v => v.classList.remove('active'));
    nodes.forEach(n => n.classList.remove('active', 'completed'));

    const activeView = document.getElementById(`level-${numNivel}`);
    if (activeView) activeView.classList.add('active');

    for (let i = 1; i <= 7; i++) {
        const node = document.getElementById(`step-node-${i}`);
        if (!node) continue;

        if (i === numNivel) {
            node.classList.add('active');
        } else if (i < numNivel) {
            node.classList.add('completed');
        }
    }
}

function configurarRamaNivel3(camino) {
    const branches = document.querySelectorAll('.branch-panel');
    const pathPill = document.getElementById('n3-branch-pill');
    const n3Title = document.getElementById('n3-main-title');

    branches.forEach(b => b.classList.add('hidden'));

    const activeBranch = document.getElementById(`branch-${camino}`);
    if (activeBranch) activeBranch.classList.remove('hidden');

    const titulos = {
        'tos_fiebre': 'Rama A: Evaluación de Cuadro Infeccioso (Tos y Fiebre)',
        'disnea': 'Rama B: Evaluación de Insuficiencia Respiratoria (Disnea Aguda)',
        'sibilancias': 'Rama C: Evaluación de Broncospasmo (Silbidos y Opresión)',
        'dolor_pleuritico': 'Rama D: Evaluación de Dolor Torácico Pleurítico'
    };

    if (pathPill) pathPill.innerHTML = `<i class="fa-solid fa-route"></i> RAMA: ${camino.toUpperCase()}`;
    if (n3Title) n3Title.innerHTML = `<i class="fa-solid fa-network-wired"></i> Nivel 3: ${titulos[camino] || 'Evaluación'}`;
}

function reiniciarApp() {
    selectedPathN2 = 'tos_fiebre';
    mostrarNivel(1);
}

function calcularInferencia7Niveles() {
    // Nivel 1: Perfil
    const edad = parseInt(document.getElementById('n1-edad').value) || 45;
    const fumador = document.getElementById('n1-fumador').value;
    const asmaPrevio = document.getElementById('chk-asma-previo').checked;
    const epocPrevio = document.getElementById('chk-epoc-previo').checked;

    // Nivel 3: Casillas marcadas en la rama activa
    const branchActive = document.querySelector('.branch-panel:not(.hidden)');
    const checkedBoxes = branchActive ? Array.from(branchActive.querySelectorAll('input[type="checkbox"]:checked')).map(c => c.name) : [];

    // Nivel 4: Síntomas asociados
    const sudorNoct = document.getElementById('chk-sudor-noct').checked;
    const mialgias = document.getElementById('chk-mialgias').checked;

    // Nivel 5: Vitales
    const spo2 = parseFloat(document.getElementById('n5-spo2').value) || 95;
    const temp = parseFloat(document.getElementById('n5-temp').value) || 38.2;

    // Nivel 6: Alarma
    const cianosis = document.getElementById('chk-cianosis').checked;
    const usoMusculos = document.getElementById('chk-uso-musc').checked;
    const taquipnea = document.getElementById('chk-taquipnea').checked;
    const confusion = document.getElementById('chk-confusion').checked;

    let cf = 74;
    if (fumador === 'intenso') cf += 6;
    if (spo2 < 92) cf += 10;
    if (temp >= 38.5) cf += 8;
    if (cianosis || usoMusculos) cf += 6;
    cf = Math.min(98, cf);

    let diagnostico = '';
    let descripcion = '';
    let triaje = '🟡 MODERADO';
    let examenes = [];
    let reglasDisparadas = [];
    let conducta = '';

    // Evaluación por casillas marcadas
    if (checkedBoxes.includes('chk-tos-neumonia')) {
        diagnostico = 'Neumonía Adquirida en la Comunidad (NAC)';
        descripcion = 'Infección bacteriana aguda del parénquima pulmonar con presencia de exudado alveolar purulento.';
        triaje = (spo2 < 92 || confusion || edad > 65) ? '🚨 EMERGENCIA CRÍTICA' : '⚠️ URGENTE';
        examenes = ['Radiografía de Tórax AP y Lat', 'Hemograma + PCR / VSG', 'Cultivo de esputo y Gram', 'Gasometría Arterial'];
        reglasDisparadas = ['R-NEUMO-01: Expectoración purulenta', 'R-NEUMO-02: Fiebre alta con escalofríos', 'R-VITAL-01: Marcador infeccioso'];
        conducta = 'Evaluación prioritaria para inicio de cobertura antibiótica empírica. Valorar oxigenoterapia si SpO2 < 92%.';
    } else if (checkedBoxes.includes('chk-tos-absceso')) {
        diagnostico = 'Absceso Pulmonar / Neumonía Necrosante';
        descripcion = 'Lesión cavitada necrosante en el parénquima pulmonar por infección fétida de bacterias anaerobias.';
        triaje = '🚨 EMERGENCIA CRÍTICA';
        examenes = ['Tomografía Computarizada de Tórax', 'Cultivo de expectoración para Anaerobios', 'Broncoscopía diagnóstica'];
        reglasDisparadas = ['R-ABSC-01: Expectoración fétida vómica', 'R-ABSC-02: Picos febriles continuos'];
        conducta = 'Hospitalización e inicio de antibióticoterapia EV de amplio espectro para anaerobios.';
    } else if (checkedBoxes.includes('chk-tos-viral')) {
        diagnostico = 'Infección Respiratoria Aguda Viral (SRA / COVID-19 / Influenza)';
        descripcion = 'Compromiso mucoso inflamatorio autolimitado de vías aéreas superiores e inferiores de origen viral.';
        triaje = spo2 < 92 ? '⚠️ URGENTE' : '🟢 LEVE / MODERADO';
        examenes = ['Panel Viral Respiratorio (RT-PCR)', 'Hemograma completo', 'Oximetría de pulso continua'];
        reglasDisparadas = ['R-VIRAL-01: Tos seca con coriza', 'R-VIRAL-02: Síntomas sistémicos mialgias'];
        conducta = 'Manejo sintomático con analgésicos, hidratación adecuada, aislamiento preventivo y monitoreo de SpO2.';
    } else if (checkedBoxes.includes('chk-tos-tbc') || sudorNoct) {
        diagnostico = 'Tuberculosis Pulmonar / Proceso Granulomatoso Crónico';
        descripcion = 'Infección bacilar crónica por Mycobacterium tuberculosis con compromiso parenquimatoso cavitario.';
        triaje = '⚠️ URGENTE (Prioridad de Aislamiento)';
        examenes = ['Baciloscopía seriada de esputo (BK x3)', 'Prueba molecular GeneXpert MTB/RIF', 'Radiografía de Tórax AP'];
        reglasDisparadas = ['R-TBC-01: Tos de más de 15 días', 'R-TBC-02: BASS / Sudoración nocturna'];
        conducta = 'Aislamiento respiratorio estricto con mascarilla N95 e inicio de Esquema Único Antituberculoso.';
    } else if (checkedBoxes.includes('chk-disnea-pneumo') || checkedBoxes.includes('chk-dolor-neumotorax')) {
        diagnostico = 'Neumotórax Espontáneo Agudo';
        descripcion = 'Presencia de aire en el espacio pleural que produce colapso parcial o total del tejido pulmonar.';
        triaje = '🚨 EMERGENCIA CRÍTICA';
        examenes = ['Radiografía de Tórax en Espiración Forzada', 'Gasometría Arterial', 'Tomografía de Tórax'];
        reglasDisparadas = ['R-PLEURA-01: Disnea súbita e instantánea', 'R-PLEURA-02: Dolor torácico unilateral agudo'];
        conducta = 'Transferencia inmediata a trauma-shock para descompresión pleural urgente y tubo de drenaje.';
    } else if (checkedBoxes.includes('chk-disnea-tep') || checkedBoxes.includes('chk-dolor-tep')) {
        diagnostico = 'Tromboembolismo Pulmonar Agudo (TEP)';
        descripcion = 'Oclusión del árbol arterial pulmonar por un trombo originado en la circulación venosa profunda.';
        triaje = '🚨 EMERGENCIA CRÍTICA';
        examenes = ['Angio-TAC de Arterias Pulmonares', 'Dímero D en sangre', 'Electrocardiograma'];
        reglasDisparadas = ['R-TEP-01: Disnea súbita post-reposo', 'R-TEP-02: Taquicardia + Dolor pleurítico'];
        conducta = 'Atención médica de emergencia inmediata. Anticoagulación parenteral o trombólisis en UCI.';
    } else if (checkedBoxes.includes('chk-disnea-epoc') || checkedBoxes.includes('chk-sib-epoc') || epocPrevio) {
        diagnostico = 'Exacerbación de Enfermedad Pulmonar Obstructiva Crónica (EPOC)';
        descripcion = 'Empeoramiento agudo e inestable de la limitación al flujo aéreo bronquial en paciente tabáquico.';
        triaje = spo2 < 88 ? '🚨 EMERGENCIA CRÍTICA' : '⚠️ URGENTE';
        examenes = ['Gasometría Arterial', 'Radiografía de Tórax AP', 'Cultivo de esputo'];
        reglasDisparadas = ['R-EPOC-01: Disnea en fumador crónico', 'R-EPOC-02: Expectoración aumentada'];
        conducta = 'Broncodilatadores nebulizados (Salbutamol + Ipratropio) y oxigenoterapia Venturi.';
    } else if (checkedBoxes.includes('chk-disnea-epid')) {
        diagnostico = 'Exacerbación de Fibrosis Pulmonar / Enfermedad Intersticial (EPID)';
        descripcion = 'Compromiso inflamatorio y fibroso del intersticio pulmonar con estertores crepitantes secos tipo Velcro.';
        triaje = spo2 < 90 ? '🚨 EMERGENCIA CRÍTICA' : '⚠️ URGENTE';
        examenes = ['Tomografía Computarizada de Alta Resolución (TACAR)', 'Gasometría Arterial'];
        reglasDisparadas = ['R-EPID-01: Crepitantes secos Velcro', 'R-EPID-02: Disnea progresiva restrictiva'];
        conducta = 'Evaluación especializada en neumología para pulsos de corticoides y oxigenoterapia suplementaria.';
    } else if (checkedBoxes.includes('chk-sib-asma') || asmaPrevio) {
        diagnostico = 'Crisis de Asma Bronquial (Exacerbación Aguda de Asma)';
        descripcion = 'Hiperreactividad inflamatoria bronquial reversible caracterizada por broncoconstricción e hipersecreción.';
        triaje = (spo2 < 92 || usoMusculos) ? '🚨 EMERGENCIA' : '⚠️ URGENTE';
        examenes = ['Flujometría (Peak Flow)', 'Gasometría Arterial', 'Radiografía de Tórax'];
        reglasDisparadas = ['R-ASMA-01: Sibilancias recurrentes', 'R-ASMA-02: Respuesta favorable a beta-2 agonistas'];
        conducta = 'Inhalación de β2-agonistas de acción corta (Salbutamol) cada 20 min + corticoides sistémicos.';
    } else if (checkedBoxes.includes('chk-sib-estridor')) {
        diagnostico = 'Edema Laríngeo / Obstrucción de Vía Aérea Superior (Estridor)';
        descripcion = 'Estrechamiento agudo subglótico o laringospasmo crítico que compromete el paso de aire alto.';
        triaje = '🚨 EMERGENCIA CRÍTICA DE VÍA AÉREA';
        examenes = ['Laringoscopía directa', 'Oximetría continua'];
        reglasDisparadas = ['R-ESTRIDOR-01: Estridor inspiratorio', 'R-ESTRIDOR-02: Obstrucción alta'];
        conducta = 'Asegurar vía aérea de inmediato. Nebulización con Adrenalina racémica + Dexametasona EV.';
    } else if (checkedBoxes.includes('chk-dolor-pleuritis')) {
        diagnostico = 'Pleuresía Fibrinosa / Derrame Pleural Inflamatorio';
        descripcion = 'Inflamación de las hojas pleurales parietal y visceral con fricción dolorosa pleurítica al inspirar.';
        triaje = '⚠️ URGENTE';
        examenes = ['Ecografía Pleural', 'Radiografía de Tórax', 'Toracocentesis diagnóstica'];
        reglasDisparadas = ['R-PLEUR-01: Dolor pleurítico en puntada', 'R-PLEUR-02: Roce pleural auscultatorio'];
        conducta = 'Analgesia antiinflamatoria (AINEs), descarte de neumonía subyacente y toracocentesis.';
    } else if (checkedBoxes.includes('chk-dolor-pericarditis')) {
        diagnostico = 'Pericarditis Aguda con Compromiso Pleuropericárdico';
        descripcion = 'Inflamación del saco pericárdico que genera dolor torácico pleurítico sensible al cambio postural.';
        triaje = '🚨 EMERGENCIA';
        examenes = ['Electrocardiograma', 'Ecocardiograma', 'Enzimas cardíacas (Troponinas)'];
        reglasDisparadas = ['R-PERI-01: Dolor post-inclinación', 'R-PERI-02: Frote pericárdico'];
        conducta = 'Atención cardiológica urgente, ECG de 12 derivaciones, analgesia con AINEs y ecocardiograma.';
    } else {
        diagnostico = 'Bronquitis Aguda / Síndrome Bronquial Obstructivo (SBO)';
        descripcion = 'Inflamación agudo-progresiva del árbol bronquial principal de evolución autolimitada.';
        triaje = '🟢 LEVE / MODERADO';
        examenes = ['Auscultación pulmonar clínica', 'Oximetría de pulso'];
        reglasDisparadas = ['R-BRONQ-01: Broncospasmo post-viral'];
        conducta = 'Manejo ambulatorio con hidratación, antipiréticos e inhaladores de rescate si hay espasmo.';
    }

    // Renderizar resultados con lenguaje de probabilidad presuntiva
    document.getElementById('res-diag-title').textContent = `Es probable que presente: ${diagnostico}`;
    document.getElementById('res-cf-val').textContent = `${cf}%`;
    document.getElementById('res-triage-text').textContent = triaje;
    document.getElementById('res-diag-desc').textContent = descripcion;

    const listExams = document.getElementById('res-exams-list');
    listExams.innerHTML = '';
    examenes.forEach(ex => {
        const li = document.createElement('li');
        li.textContent = ex;
        listExams.appendChild(li);
    });

    const ruleContainer = document.getElementById('res-rules-list');
    ruleContainer.innerHTML = '';
    reglasDisparadas.forEach(r => {
        const span = document.createElement('span');
        span.className = 'rule-chip';
        span.textContent = r;
        ruleContainer.appendChild(span);
    });

    document.getElementById('res-conduct-box').textContent = conducta;

    // Actualizar trazabilidad de 7 niveles
    const traceDisplay = document.getElementById('trace-path-display');
    traceDisplay.innerHTML = `
        <span class="chip-step">N1: Edad ${edad} (${fumador})</span>
        <i class="fa-solid fa-chevron-right"></i>
        <span class="chip-step">N2: Rama ${selectedPathN2.toUpperCase()}</span>
        <i class="fa-solid fa-chevron-right"></i>
        <span class="chip-step">N3: ${checkedBoxes.length} hallazgos marcados</span>
        <i class="fa-solid fa-chevron-right"></i>
        <span class="chip-step">N5: SpO2 ${spo2}% (${temp}°C)</span>
    `;

    if (typeof confetti === 'function') {
        confetti({ particleCount: 65, spread: 75, origin: { y: 0.6 } });
    }
}
