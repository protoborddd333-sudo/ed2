import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mapa Mental EDO - Mantenimiento Industrial",
    layout="wide"
)

html_code = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">

<style>
    * {
        box-sizing: border-box;
    }

    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        font-family: Arial, Helvetica, sans-serif;
        background: #FFFFFF;
        color: #000000;
    }

    .page {
        width: 100%;
        height: 850px;
        background: #FFFFFF;
        border: 1px solid #DCEFF8;
        border-radius: 22px;
        padding: 18px;
        overflow: hidden;
    }

    .title {
        text-align: center;
        font-size: 28px;
        font-weight: 800;
        color: #000000;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 14px;
        color: #333333;
        margin-bottom: 8px;
    }

    .map-viewport {
        position: relative;
        width: 100%;
        height: 735px;
        overflow: hidden;
    }

    .scale-wrap {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 1180px;
        height: 650px;
        transform: translate(-50%, -50%) scale(var(--fit-scale, 1));
        transform-origin: center center;
    }

    .node {
        background: #FFFFFF;
        border: 2px solid #01ACF1;
        color: #000000;
        border-radius: 17px;
        padding: 13px 14px;
        box-shadow: 0 7px 18px rgba(1, 172, 241, 0.12);
        transition: all 0.30s ease;
    }

    .node:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 22px rgba(1, 172, 241, 0.20);
    }

    .level-0 {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 285px;
        transform: translate(-50%, -50%);
        text-align: center;
        font-size: 17px;
        font-weight: 800;
        z-index: 10;
    }

    .level-0:hover {
        transform: translate(-50%, -52%);
    }

    .level-1 {
        width: 210px;
        min-height: 98px;
        font-size: 14px;
    }

    .level-2 {
        width: 185px;
        font-size: 12.4px;
        border-width: 1.6px;
        padding: 10px 11px;
    }

    body.deep-expanded .level-0 {
        width: 260px;
        font-size: 15.5px;
        padding: 11px 12px;
    }

    body.deep-expanded .level-1 {
        width: 195px;
        font-size: 13px;
        padding: 11px 12px;
    }

    body.deep-expanded .level-2 {
        width: 170px;
        font-size: 11.7px;
        padding: 9px 10px;
    }

    body.very-deep .level-0 {
        width: 245px;
        font-size: 14.5px;
    }

    body.very-deep .level-1 {
        width: 180px;
        font-size: 12px;
    }

    body.very-deep .level-2 {
        width: 158px;
        font-size: 11px;
    }

    .node-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
    }

    .node-title {
        font-weight: 800;
        line-height: 1.20;
    }

    .node-text {
        margin-top: 7px;
        font-size: 12.5px;
        line-height: 1.32;
        color: #222222;
        font-weight: 400;
    }

    body.deep-expanded .node-text {
        font-size: 11.4px;
        line-height: 1.28;
    }

    body.very-deep .node-text {
        font-size: 10.8px;
        line-height: 1.25;
    }

    .toggle {
        min-width: 27px;
        height: 27px;
        border-radius: 50%;
        border: 2px solid #01ACF1;
        background: #FFFFFF;
        color: #000000;
        cursor: pointer;
        font-weight: 900;
        font-size: 17px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.25s ease;
    }

    .toggle:hover {
        background: #EAF8FE;
        transform: scale(1.08);
    }

    .tag {
        display: inline-block;
        background: #F0FAFE;
        border: 1px solid #BDEBFC;
        border-radius: 50px;
        padding: 3px 8px;
        margin-top: 7px;
        font-size: 11px;
        font-weight: 700;
        color: #000000;
    }

    .formula {
        margin-top: 6px;
        padding: 6px 7px;
        background: #F8FCFE;
        border-left: 3px solid #01ACF1;
        font-size: 11.5px;
        border-radius: 7px;
    }

    body.very-deep .formula {
        font-size: 10.5px;
        padding: 5px 6px;
    }

    .line {
        height: 2px;
        background: #01ACF1;
        opacity: 0.75;
        border-radius: 20px;
        flex-shrink: 0;
    }

    .line-main {
        width: 42px;
    }

    .line-sub {
        width: 24px;
        opacity: 0.60;
        display: none;
    }

    .branch.sub-open .line-sub {
        display: block;
    }

    body.very-deep .line-main {
        width: 30px;
    }

    body.very-deep .line-sub {
        width: 18px;
    }

    .branch {
        position: absolute;
        display: none;
        align-items: center;
        gap: 8px;
        opacity: 0;
        transform: scale(0.92);
    }

    .branch.show {
        display: flex;
        opacity: 1;
        transform: scale(1);
        animation: expandir 0.35s ease forwards;
    }

    .rama1 {
        left: 18px;
        top: 30px;
    }

    .rama2 {
        left: 18px;
        top: 420px;
    }

    .rama3 {
        left: 730px;
        top: 55px;
    }

    .rama4 {
        left: 730px;
        top: 405px;
    }

    .subnodes {
        display: none;
        flex-direction: column;
        gap: 8px;
        opacity: 0;
        transform: scale(0.90);
    }

    .subnodes.show {
        display: flex;
        opacity: 1;
        transform: scale(1);
        animation: expandir 0.32s ease forwards;
    }

    @keyframes expandir {
        from {
            opacity: 0;
            transform: scale(0.88);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    .footer {
        text-align: center;
        font-size: 11px;
        color: #444444;
        margin-top: 2px;
    }
</style>
</head>

<body>

<div class="page">

    <div class="title">Mapa Mental Interactivo</div>
    <div class="subtitle">
        Ecuaciones Diferenciales Ordinarias aplicadas al mantenimiento industrial
    </div>

    <div class="map-viewport">
        <div class="scale-wrap">

            <!-- NÚCLEO CENTRAL -->
            <div class="node level-0">
                <div class="node-header">
                    <span class="node-title">
                        Ecuaciones Diferenciales en el Mantenimiento Industrial
                    </span>
                    <button class="toggle" onclick="toggleMain(this)">+</button>
                </div>

                <div class="node-text">
                    Modelan cambios de variables como temperatura, presión, nivel o velocidad. Ayudan al diagnóstico y predicción del estado de equipos.
                </div>
            </div>

            <!-- RAMA 1 IZQUIERDA SUPERIOR -->
            <div class="branch rama1 left-branch">
                <div id="rama1" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Definición</div>
                        <div class="node-text">
                            Relación entre una función desconocida y sus derivadas.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Orden</div>
                        <div class="node-text">
                            Lo define la derivada más alta: dy/dt es primer orden, d²y/dt² es segundo orden.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Linealidad</div>
                        <div class="node-text">
                            Es lineal si la variable dependiente y sus derivadas están al exponente 1.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Tipo</div>
                        <div class="node-text">
                            EDO: una variable independiente. EDP: dos o más variables independientes.
                        </div>
                    </div>
                </div>

                <div class="line line-sub"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">1. Fundamentos y Clasificación</span>
                        <button class="toggle" onclick="toggleSection('rama1', this)">+</button>
                    </div>
                    <div class="node-text">
                        Identifica la estructura básica de una ecuación diferencial.
                    </div>
                    <span class="tag">Base teórica</span>
                </div>

                <div class="line line-main"></div>
            </div>

            <!-- RAMA 2 IZQUIERDA INFERIOR -->
            <div class="branch rama2 left-branch">
                <div id="rama2" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Variables Separables</div>
                        <div class="node-text">
                            Se separan las variables en lados distintos y luego se integran.
                        </div>
                        <div class="formula">dy/dx = f(x)g(y)</div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Factor Integrante</div>
                        <div class="node-text">
                            Convierte una EDO lineal en una derivada de producto.
                        </div>
                        <div class="formula">y' + p(x)y = q(x)</div>
                    </div>
                </div>

                <div class="line line-sub"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">2. Herramientas de Resolución</span>
                        <button class="toggle" onclick="toggleSection('rama2', this)">+</button>
                    </div>
                    <div class="node-text">
                        Métodos básicos para resolver EDOs de primer orden.
                    </div>
                    <span class="tag">Métodos</span>
                </div>

                <div class="line line-main"></div>
            </div>

            <!-- RAMA 3 DERECHA SUPERIOR -->
            <div class="branch rama3 right-branch">
                <div class="line line-main"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">3. Modelos de Procesos</span>
                        <button class="toggle" onclick="toggleSection('rama3', this)">+</button>
                    </div>
                    <div class="node-text">
                        Aplican las EDO al análisis de procesos de planta.
                    </div>
                    <span class="tag">Aplicación</span>
                </div>

                <div class="line line-sub"></div>

                <div id="rama3" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Termicidad</div>
                        <div class="node-text">
                            Ley de Newton: enfriamiento de motores y rodamientos.
                        </div>
                        <div class="formula">dT/dt = -k(T - Ta)</div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Fluidos</div>
                        <div class="node-text">
                            Ley de Torricelli: vaciado de tanques según la altura del fluido.
                        </div>
                        <div class="formula">v = √(2gh)</div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Sistemas</div>
                        <div class="node-text">
                            Dinámica de actuadores hidráulicos: presión, velocidad y posición.
                        </div>
                    </div>
                </div>
            </div>

            <!-- RAMA 4 DERECHA INFERIOR -->
            <div class="branch rama4 right-branch">
                <div class="line line-main"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">4. Valor para el Mantenimiento</span>
                        <button class="toggle" onclick="toggleSection('rama4', this)">+</button>
                    </div>
                    <div class="node-text">
                        Usa modelos matemáticos para diagnosticar y prevenir fallas.
                    </div>
                    <span class="tag">Diagnóstico</span>
                </div>

                <div class="line line-sub"></div>

                <div id="rama4" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Constante de tiempo τ</div>
                        <div class="node-text">
                            Indica rapidez de respuesta. Si aumenta, puede existir fricción o degradación del fluido.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Predicción</div>
                        <div class="node-text">
                            Estima estados futuros de temperatura, presión, nivel o velocidad.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Decisiones preventivas</div>
                        <div class="node-text">
                            Permite programar inspección, lubricación, ajuste o reemplazo.
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="footer">
        Mapa mental: teoría de EDO aplicada al mantenimiento industrial y gestión de activos.
    </div>

</div>

<script>
    function toggleMain(button) {
        const branches = document.querySelectorAll(".branch");

        if (document.body.classList.contains("map-open")) {
            document.body.classList.remove("map-open");
            button.innerText = "+";

            branches.forEach(function(branch) {
                branch.classList.remove("show");
                branch.classList.remove("sub-open");
            });

            cerrarSubramas();

        } else {
            document.body.classList.add("map-open");
            button.innerText = "−";

            branches.forEach(function(branch) {
                branch.classList.add("show");
            });
        }

        updateBodyState();
    }

    function toggleSection(id, button) {
        const section = document.getElementById(id);
        const branch = button.closest(".branch");

        if (section.classList.contains("show")) {
            section.classList.remove("show");
            branch.classList.remove("sub-open");
            button.innerText = "+";
        } else {
            section.classList.add("show");
            branch.classList.add("sub-open");
            button.innerText = "−";
        }

        updateBodyState();
    }

    function cerrarSubramas() {
        const subnodes = document.querySelectorAll(".subnodes");
        const buttons = document.querySelectorAll(".level-1 .toggle");

        subnodes.forEach(function(item) {
            item.classList.remove("show");
        });

        buttons.forEach(function(btn) {
            btn.innerText = "+";
        });
    }

    function updateBodyState() {
        const openSubnodes = document.querySelectorAll(".subnodes.show").length;

        document.body.classList.remove("deep-expanded");
        document.body.classList.remove("very-deep");

        if (openSubnodes >= 1) {
            document.body.classList.add("deep-expanded");
        }

        if (openSubnodes >= 3) {
            document.body.classList.add("very-deep");
        }

        fitCanvas();
    }

    function fitCanvas() {
        const viewport = document.querySelector(".map-viewport");
        const wrap = document.querySelector(".scale-wrap");

        const canvasWidth = 1180;
        const canvasHeight = 650;

        const scaleX = viewport.clientWidth / canvasWidth;
        const scaleY = viewport.clientHeight / canvasHeight;

        let scale = Math.min(scaleX, scaleY, 1);

        const openSubnodes = document.querySelectorAll(".subnodes.show").length;

        if (openSubnodes >= 3) {
            scale = scale * 0.96;
        }

        wrap.style.setProperty("--fit-scale", scale);
    }

    window.addEventListener("resize", fitCanvas);
    window.addEventListener("load", fitCanvas);
    fitCanvas();
</script>

</body>
</html>
"""

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0.8rem;
            padding-bottom: 0.8rem;
        }

        iframe {
            overflow: hidden !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

components.html(html_code, height=870, scrolling=False)
