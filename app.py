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

    body {
        margin: 0;
        padding: 18px;
        font-family: Arial, Helvetica, sans-serif;
        background: #FFFFFF;
        color: #000000;
    }

    .page {
        width: 100%;
        min-height: 900px;
        background: #FFFFFF;
        border-radius: 24px;
        padding: 26px;
        border: 1px solid #DCEFF8;
        overflow-x: auto;
    }

    .title {
        text-align: center;
        font-size: 30px;
        font-weight: 800;
        color: #000000;
        margin-bottom: 8px;
    }

    .subtitle {
        text-align: center;
        font-size: 15px;
        color: #333333;
        margin-bottom: 35px;
    }

    .spider-body {
        display: grid;
        grid-template-columns: 1fr 340px 1fr;
        align-items: center;
        gap: 22px;
        width: 100%;
        min-width: 1100px;
    }

    .center-zone {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .side {
        display: none;
        flex-direction: column;
        gap: 42px;
    }

    .side.show {
        display: flex;
        animation: expandir 0.45s ease forwards;
    }

    .left-side {
        align-items: flex-end;
    }

    .right-side {
        align-items: flex-start;
    }

    .branch-row {
        display: flex;
        align-items: center;
        gap: 10px;
        width: 100%;
    }

    .left-row {
        justify-content: flex-end;
    }

    .right-row {
        justify-content: flex-start;
    }

    .node {
        background: #FFFFFF;
        border: 2px solid #01ACF1;
        color: #000000;
        border-radius: 18px;
        padding: 15px 17px;
        box-shadow: 0 8px 20px rgba(1, 172, 241, 0.12);
        transition: all 0.35s ease;
    }

    .node:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(1, 172, 241, 0.20);
    }

    .level-0 {
        width: 335px;
        text-align: center;
        font-size: 19px;
        font-weight: 800;
    }

    .level-1 {
        width: 255px;
        min-height: 112px;
        font-size: 15px;
    }

    .level-2 {
        width: 230px;
        font-size: 13.2px;
        border-width: 1.7px;
        padding: 12px 13px;
    }

    body.is-expanded .level-0 {
        width: 305px;
        font-size: 17px;
        padding: 13px 15px;
    }

    body.deep-expanded .level-1 {
        width: 235px;
        font-size: 13.5px;
        padding: 12px 13px;
    }

    body.deep-expanded .level-2 {
        width: 215px;
        font-size: 12.5px;
    }

    .node-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
    }

    .node-title {
        font-weight: 800;
        line-height: 1.25;
    }

    .node-text {
        margin-top: 8px;
        font-size: 13px;
        line-height: 1.38;
        color: #222222;
        font-weight: 400;
    }

    .toggle {
        min-width: 30px;
        height: 30px;
        border-radius: 50%;
        border: 2px solid #01ACF1;
        background: #FFFFFF;
        color: #000000;
        cursor: pointer;
        font-weight: 900;
        font-size: 18px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.25s ease;
    }

    .toggle:hover {
        background: #EAF8FE;
        transform: scale(1.10);
    }

    .line {
        height: 2px;
        background: #01ACF1;
        opacity: 0.75;
        border-radius: 20px;
        flex-shrink: 0;
    }

    .line-main {
        width: 65px;
    }

    .line-small {
        width: 32px;
        opacity: 0.60;
    }

    .subnodes {
        display: none;
        flex-direction: column;
        gap: 10px;
        opacity: 0;
        transform: scale(0.92);
        transition: all 0.35s ease;
    }

    .subnodes.show {
        display: flex;
        opacity: 1;
        transform: scale(1);
        animation: expandir 0.35s ease forwards;
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

    .tag {
        display: inline-block;
        background: #F0FAFE;
        border: 1px solid #BDEBFC;
        border-radius: 50px;
        padding: 4px 9px;
        margin-top: 8px;
        font-size: 12px;
        font-weight: 700;
        color: #000000;
    }

    .formula {
        margin-top: 8px;
        padding: 7px 9px;
        background: #F8FCFE;
        border-left: 3px solid #01ACF1;
        font-size: 12.3px;
        border-radius: 8px;
    }

    .footer {
        margin-top: 38px;
        text-align: center;
        font-size: 12px;
        color: #444444;
    }

    @media (max-width: 1200px) {
        .page {
            overflow-x: auto;
        }
    }
</style>
</head>

<body>

<div class="page">

    <div class="title">Mapa Mental Interactivo</div>
    <div class="subtitle">
        Ecuaciones Diferenciales Ordinarias aplicadas al mantenimiento industrial
    </div>

    <div class="spider-body">

        <div id="leftBranches" class="side left-side">

            <div class="branch-row left-row">

                <div id="rama1" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Definición</div>
                        <div class="node-text">
                            Relaciona una función desconocida con sus derivadas. Sirve para representar cambios de una variable respecto al tiempo.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Orden</div>
                        <div class="node-text">
                            Se define por la derivada más alta. Si aparece dy/dt es de primer orden; si aparece d²y/dt² es de segundo orden.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Linealidad</div>
                        <div class="node-text">
                            Es lineal cuando la variable dependiente y sus derivadas están al exponente 1 y no se multiplican entre sí.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Tipo: EDO vs EDP</div>
                        <div class="node-text">
                            La EDO depende de una sola variable independiente. La EDP depende de dos o más variables independientes.
                        </div>
                    </div>
                </div>

                <div class="line line-small"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">1. Fundamentos y Clasificación</span>
                        <button class="toggle" onclick="toggleSection('rama1', this)">+</button>
                    </div>
                    <div class="node-text">
                        Permite identificar la estructura básica de una ecuación diferencial.
                    </div>
                    <span class="tag">Base teórica</span>
                </div>

                <div class="line line-main"></div>
            </div>

            <div class="branch-row left-row">

                <div id="rama2" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Variables Separables</div>
                        <div class="node-text">
                            Método que separa las variables en lados distintos de la ecuación para luego integrar.
                        </div>
                        <div class="formula">
                            dy/dx = f(x)g(y)
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Factor Integrante</div>
                        <div class="node-text">
                            Se aplica a EDOs lineales de primer orden para convertir la ecuación en una derivada de producto.
                        </div>
                        <div class="formula">
                            y' + p(x)y = q(x)
                        </div>
                    </div>
                </div>

                <div class="line line-small"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">2. Herramientas de Resolución</span>
                        <button class="toggle" onclick="toggleSection('rama2', this)">+</button>
                    </div>
                    <div class="node-text">
                        Son métodos usados para resolver ecuaciones diferenciales de primer orden.
                    </div>
                    <span class="tag">Métodos</span>
                </div>

                <div class="line line-main"></div>
            </div>

        </div>

        <div class="center-zone">
            <div class="node level-0">
                <div class="node-header">
                    <span class="node-title">
                        Ecuaciones Diferenciales en el Mantenimiento Industrial
                    </span>
                    <button class="toggle" onclick="toggleMain(this)">+</button>
                </div>

                <div class="node-text">
                    Modelan el cambio de variables como temperatura, presión, nivel o velocidad. Ayudan a diagnosticar y predecir el comportamiento de equipos.
                </div>
            </div>
        </div>

        <div id="rightBranches" class="side right-side">

            <div class="branch-row right-row">

                <div class="line line-main"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">3. Modelos de Procesos</span>
                        <button class="toggle" onclick="toggleSection('rama3', this)">+</button>
                    </div>
                    <div class="node-text">
                        Aplican las EDO al análisis de procesos reales en planta.
                    </div>
                    <span class="tag">Aplicación</span>
                </div>

                <div class="line line-small"></div>

                <div id="rama3" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Termicidad: Ley de Newton</div>
                        <div class="node-text">
                            Describe el enfriamiento o calentamiento según la diferencia entre la temperatura del cuerpo y el ambiente.
                        </div>
                        <div class="formula">
                            dT/dt = -k(T - Ta)
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Fluidos: Ley de Torricelli</div>
                        <div class="node-text">
                            Modela la velocidad de salida de un fluido y el vaciado de tanques según la altura del líquido.
                        </div>
                        <div class="formula">
                            v = √(2gh)
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Sistemas: Actuadores Hidráulicos</div>
                        <div class="node-text">
                            Representa la respuesta de posición, presión o velocidad de un actuador frente a una entrada del sistema.
                        </div>
                    </div>
                </div>
            </div>

            <div class="branch-row right-row">

                <div class="line line-main"></div>

                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">4. Valor para el Mantenimiento</span>
                        <button class="toggle" onclick="toggleSection('rama4', this)">+</button>
                    </div>
                    <div class="node-text">
                        Convierte los modelos matemáticos en criterios de diagnóstico y prevención.
                    </div>
                    <span class="tag">Diagnóstico</span>
                </div>

                <div class="line line-small"></div>

                <div id="rama4" class="subnodes">
                    <div class="node level-2">
                        <div class="node-title">Constante de tiempo τ</div>
                        <div class="node-text">
                            Indica la rapidez de respuesta del sistema. Si aumenta, puede señalar fricción, desgaste o degradación del fluido.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Predicción de estados futuros</div>
                        <div class="node-text">
                            Permite estimar el comportamiento posterior de una variable, como temperatura, presión o nivel.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Decisiones preventivas</div>
                        <div class="node-text">
                            Ayuda a definir cuándo inspeccionar, lubricar, ajustar o reemplazar antes de que ocurra una falla.
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
        const left = document.getElementById("leftBranches");
        const right = document.getElementById("rightBranches");

        if (left.classList.contains("show")) {
            left.classList.remove("show");
            right.classList.remove("show");
            button.innerText = "+";
            cerrarRamas();
        } else {
            left.classList.add("show");
            right.classList.add("show");
            button.innerText = "−";
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

    function cerrarRamas() {
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
        const left = document.getElementById("leftBranches");
        const openSubnodes = document.querySelectorAll(".subnodes.show");

        if (left.classList.contains("show")) {
            document.body.classList.add("is-expanded");
        } else {
            document.body.classList.remove("is-expanded");
        }

        if (openSubnodes.length > 0) {
            document.body.classList.add("deep-expanded");
        } else {
            document.body.classList.remove("deep-expanded");
        }
    }
</script>

</body>
</html>
"""

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

components.html(html_code, height=980, scrolling=True)
