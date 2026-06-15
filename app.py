import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mapa Mental EDO",
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
        height: 760px;
        background: #FFFFFF;
        overflow: hidden;
        position: relative;
    }

    .map-viewport {
        position: relative;
        width: 100%;
        height: 760px;
        overflow: hidden;
    }

    .scale-wrap {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 1120px;
        height: 650px;
        transform: translate(-50%, -50%) scale(var(--fit-scale, 1));
        transform-origin: center center;
    }

    .node {
        background: #FFFFFF;
        border: 2px solid #01ACF1;
        color: #000000;
        border-radius: 15px;
        padding: 10px 11px;
        box-shadow: 0 6px 16px rgba(1, 172, 241, 0.10);
        transition: all 0.25s ease;
    }

    .node:hover {
        transform: translateY(-2px);
        box-shadow: 0 9px 20px rgba(1, 172, 241, 0.18);
    }

    .center-node {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 245px;
        transform: translate(-50%, -50%);
        text-align: center;
        font-size: 14px;
        font-weight: 800;
        z-index: 10;
    }

    .center-node:hover {
        transform: translate(-50%, -52%);
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
        animation: expandir 0.35s ease forwards;
    }

    .rama1 {
        left: 70px;
        top: 45px;
    }

    .rama2 {
        left: 105px;
        top: 420px;
    }

    .rama3 {
        left: 705px;
        top: 55px;
    }

    .rama4 {
        left: 690px;
        top: 405px;
    }

    .branch-main {
        width: 205px;
        min-height: 82px;
        font-size: 12px;
    }

    .subnodes {
        display: none;
        flex-direction: column;
        gap: 7px;
        opacity: 0;
        transform: scale(0.92);
    }

    .subnodes.show {
        display: flex;
        opacity: 1;
        animation: expandir 0.30s ease forwards;
    }

    .mini-node {
        width: 170px;
        font-size: 11px;
        padding: 8px 9px;
        border-width: 1.6px;
    }

    .mini-detail {
        display: none;
        margin-top: 6px;
        font-size: 10.5px;
        line-height: 1.25;
        color: #222222;
        animation: expandir 0.25s ease forwards;
    }

    .mini-detail.show {
        display: block;
    }

    .node-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 6px;
    }

    .node-title {
        font-weight: 800;
        line-height: 1.18;
    }

    .node-text {
        margin-top: 6px;
        font-size: 10.8px;
        line-height: 1.25;
        color: #222222;
        font-weight: 400;
    }

    .toggle {
        min-width: 24px;
        height: 24px;
        border-radius: 50%;
        border: 2px solid #01ACF1;
        background: #FFFFFF;
        color: #000000;
        cursor: pointer;
        font-weight: 900;
        font-size: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.20s ease;
    }

    .toggle:hover {
        background: #EAF8FE;
        transform: scale(1.08);
    }

    .mini-toggle {
        min-width: 20px;
        height: 20px;
        font-size: 12px;
        border-width: 1.6px;
    }

    .tag {
        display: inline-block;
        background: #F0FAFE;
        border: 1px solid #BDEBFC;
        border-radius: 50px;
        padding: 3px 7px;
        margin-top: 6px;
        font-size: 9.5px;
        font-weight: 700;
        color: #000000;
    }

    .formula {
        margin-top: 5px;
        padding: 5px 6px;
        background: #F8FCFE;
        border-left: 3px solid #01ACF1;
        font-size: 10px;
        border-radius: 6px;
    }

    body.deep-expanded .center-node {
        width: 225px;
        font-size: 12.8px;
        padding: 9px 10px;
    }

    body.deep-expanded .branch-main {
        width: 185px;
        font-size: 11px;
        min-height: 74px;
    }

    body.deep-expanded .mini-node {
        width: 155px;
        font-size: 10px;
        padding: 7px 8px;
    }

    body.deep-expanded .node-text {
        font-size: 9.8px;
    }

    body.very-deep .center-node {
        width: 210px;
        font-size: 12px;
    }

    body.very-deep .branch-main {
        width: 172px;
        font-size: 10px;
    }

    body.very-deep .mini-node {
        width: 145px;
        font-size: 9.4px;
    }

    body.very-deep .mini-detail {
        font-size: 9.2px;
    }

    @keyframes expandir {
        from {
            opacity: 0;
            transform: scale(0.90);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
</style>
</head>

<body>

<div class="page">
    <div class="map-viewport">
        <div class="scale-wrap">

            <!-- NÚCLEO CENTRAL -->
            <div class="node center-node">
                <div class="node-header">
                    <span class="node-title">
                        Ecuaciones Diferenciales en el Mantenimiento Industrial
                    </span>
                    <button class="toggle" onclick="toggleMain(this)">+</button>
                </div>

                <div class="node-text">
                    Modelan cambios de temperatura, presión, nivel o velocidad para diagnosticar y predecir el comportamiento de equipos.
                </div>
            </div>

            <!-- RAMA 1 -->
            <div class="branch rama1 left-branch">

                <div id="rama1" class="subnodes">

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Definición</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('definicion', this)">+</button>
                        </div>
                        <div id="definicion" class="mini-detail">
                            Relación entre una función desconocida y sus derivadas.
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Orden</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('orden', this)">+</button>
                        </div>
                        <div id="orden" class="mini-detail">
                            Lo define la derivada más alta: dy/dt es primer orden y d²y/dt² es segundo orden.
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Linealidad</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('linealidad', this)">+</button>
                        </div>
                        <div id="linealidad" class="mini-detail">
                            Es lineal si la variable dependiente y sus derivadas están al exponente 1.
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Tipo</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('tipo', this)">+</button>
                        </div>
                        <div id="tipo" class="mini-detail">
                            EDO: una variable independiente. EDP: dos o más variables independientes.
                        </div>
                    </div>

                </div>

                <div class="node branch-main">
                    <div class="node-header">
                        <span class="node-title">1. Fundamentos y Clasificación</span>
                        <button class="toggle" onclick="toggleSection('rama1', this)">+</button>
                    </div>
                    <div class="node-text">
                        Identifica la estructura básica de una ecuación diferencial.
                    </div>
                    <span class="tag">Base teórica</span>
                </div>
            </div>

            <!-- RAMA 2 -->
            <div class="branch rama2 left-branch">

                <div id="rama2" class="subnodes">

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Variables Separables</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('separables', this)">+</button>
                        </div>
                        <div id="separables" class="mini-detail">
                            Se separan las variables en lados distintos y luego se integran.
                            <div class="formula">dy/dx = f(x)g(y)</div>
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Factor Integrante</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('factor', this)">+</button>
                        </div>
                        <div id="factor" class="mini-detail">
                            Se aplica a EDOs lineales de primer orden para facilitar la integración del producto.
                            <div class="formula">y' + p(x)y = q(x)</div>
                        </div>
                    </div>

                </div>

                <div class="node branch-main">
                    <div class="node-header">
                        <span class="node-title">2. Herramientas de Resolución</span>
                        <button class="toggle" onclick="toggleSection('rama2', this)">+</button>
                    </div>
                    <div class="node-text">
                        Métodos básicos para resolver EDOs de primer orden.
                    </div>
                    <span class="tag">Métodos</span>
                </div>
            </div>

            <!-- RAMA 3 -->
            <div class="branch rama3 right-branch">

                <div class="node branch-main">
                    <div class="node-header">
                        <span class="node-title">3. Modelos de Procesos</span>
                        <button class="toggle" onclick="toggleSection('rama3', this)">+</button>
                    </div>
                    <div class="node-text">
                        Aplican las EDO al análisis de procesos reales en planta.
                    </div>
                    <span class="tag">Aplicación</span>
                </div>

                <div id="rama3" class="subnodes">

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Termicidad</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('termicidad', this)">+</button>
                        </div>
                        <div id="termicidad" class="mini-detail">
                            Ley de Newton: enfriamiento de motores y rodamientos.
                            <div class="formula">dT/dt = -k(T - Ta)</div>
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Fluidos</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('fluidos', this)">+</button>
                        </div>
                        <div id="fluidos" class="mini-detail">
                            Ley de Torricelli: vaciado de tanques de lubricante o químicos.
                            <div class="formula">v = √(2gh)</div>
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Sistemas</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('sistemas', this)">+</button>
                        </div>
                        <div id="sistemas" class="mini-detail">
                            Dinámica de actuadores hidráulicos: presión, velocidad y posición.
                        </div>
                    </div>

                </div>
            </div>

            <!-- RAMA 4 -->
            <div class="branch rama4 right-branch">

                <div class="node branch-main">
                    <div class="node-header">
                        <span class="node-title">4. Valor para el Mantenimiento</span>
                        <button class="toggle" onclick="toggleSection('rama4', this)">+</button>
                    </div>
                    <div class="node-text">
                        Convierte modelos matemáticos en diagnóstico y prevención.
                    </div>
                    <span class="tag">Diagnóstico</span>
                </div>

                <div id="rama4" class="subnodes">

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Constante de tiempo τ</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('tau', this)">+</button>
                        </div>
                        <div id="tau" class="mini-detail">
                            Indica rapidez de respuesta. Si aumenta, puede existir fricción o degradación del fluido.
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Predicción</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('prediccion', this)">+</button>
                        </div>
                        <div id="prediccion" class="mini-detail">
                            Estima estados futuros de temperatura, presión, nivel o velocidad.
                        </div>
                    </div>

                    <div class="node mini-node">
                        <div class="node-header">
                            <span class="node-title">Decisiones preventivas</span>
                            <button class="toggle mini-toggle" onclick="toggleMini('decisiones', this)">+</button>
                        </div>
                        <div id="decisiones" class="mini-detail">
                            Permite programar inspección, lubricación, ajuste o reemplazo antes de la falla.
                        </div>
                    </div>

                </div>
            </div>

        </div>
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
            });

            cerrarTodo();

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

        if (section.classList.contains("show")) {
            section.classList.remove("show");
            button.innerText = "+";
        } else {
            section.classList.add("show");
            button.innerText = "−";
        }

        updateBodyState();
    }

    function toggleMini(id, button) {
        const detail = document.getElementById(id);

        if (detail.classList.contains("show")) {
            detail.classList.remove("show");
            button.innerText = "+";
        } else {
            detail.classList.add("show");
            button.innerText = "−";
        }

        updateBodyState();
    }

    function cerrarTodo() {
        const subnodes = document.querySelectorAll(".subnodes");
        const details = document.querySelectorAll(".mini-detail");
        const buttons = document.querySelectorAll(".branch-main .toggle, .mini-toggle");

        subnodes.forEach(function(item) {
            item.classList.remove("show");
        });

        details.forEach(function(item) {
            item.classList.remove("show");
        });

        buttons.forEach(function(btn) {
            btn.innerText = "+";
        });
    }

    function updateBodyState() {
        const openSubnodes = document.querySelectorAll(".subnodes.show").length;
        const openDetails = document.querySelectorAll(".mini-detail.show").length;

        document.body.classList.remove("deep-expanded");
        document.body.classList.remove("very-deep");

        if (openSubnodes >= 1 || openDetails >= 2) {
            document.body.classList.add("deep-expanded");
        }

        if (openSubnodes >= 3 || openDetails >= 5) {
            document.body.classList.add("very-deep");
        }

        fitCanvas();
    }

    function fitCanvas() {
        const viewport = document.querySelector(".map-viewport");
        const wrap = document.querySelector(".scale-wrap");

        const canvasWidth = 1120;
        const canvasHeight = 650;

        const scaleX = viewport.clientWidth / canvasWidth;
        const scaleY = viewport.clientHeight / canvasHeight;

        let scale = Math.min(scaleX, scaleY, 1);

        const openDetails = document.querySelectorAll(".mini-detail.show").length;

        if (openDetails >= 4) {
            scale = scale * 0.96;
        }

        if (openDetails >= 7) {
            scale = scale * 0.92;
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
            padding-top: 0rem;
            padding-bottom: 0rem;
        }

        header {
            visibility: hidden;
        }

        iframe {
            overflow: hidden !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

components.html(html_code, height=770, scrolling=False)
