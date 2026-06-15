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
        padding: 20px;
        font-family: Arial, Helvetica, sans-serif;
        background: #FFFFFF;
        color: #000000;
    }

    .page {
        width: 100%;
        min-height: 860px;
        background: #FFFFFF;
        border-radius: 24px;
        padding: 28px;
        border: 1px solid #DCEFF8;
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

    .mindmap {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 18px;
    }

    .node {
        background: #FFFFFF;
        border: 2px solid #01ACF1;
        color: #000000;
        border-radius: 18px;
        padding: 18px 20px;
        box-shadow: 0 8px 20px rgba(1, 172, 241, 0.12);
        transition: all 0.35s ease;
    }

    .node:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(1, 172, 241, 0.20);
    }

    .level-0 {
        width: 570px;
        text-align: center;
        font-size: 21px;
        font-weight: 800;
    }

    .level-1 {
        width: 280px;
        min-height: 130px;
        font-size: 16px;
    }

    .level-2 {
        width: 245px;
        font-size: 14px;
        border-width: 1.7px;
    }

    body.is-expanded .level-0 {
        width: 480px;
        font-size: 18px;
        padding: 14px 18px;
    }

    body.deep-expanded .level-1 {
        width: 250px;
        font-size: 14px;
        padding: 14px 15px;
    }

    body.deep-expanded .level-2 {
        width: 230px;
        font-size: 13px;
        padding: 13px 14px;
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
        margin-top: 9px;
        font-size: 13.5px;
        line-height: 1.45;
        color: #222222;
        font-weight: 400;
    }

    .toggle {
        min-width: 31px;
        height: 31px;
        border-radius: 50%;
        border: 2px solid #01ACF1;
        background: #FFFFFF;
        color: #000000;
        cursor: pointer;
        font-weight: 900;
        font-size: 19px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.25s ease;
    }

    .toggle:hover {
        background: #EAF8FE;
        transform: scale(1.10);
    }

    .branches {
        width: 100%;
        display: none;
        justify-content: center;
        gap: 22px;
        align-items: flex-start;
        opacity: 0;
        transform: scale(0.92);
        transition: all 0.40s ease;
        margin-top: 5px;
    }

    .branches.show {
        display: flex;
        opacity: 1;
        transform: scale(1);
        animation: expandir 0.45s ease forwards;
    }

    @keyframes expandir {
        from {
            opacity: 0;
            transform: scale(0.90) translateY(-8px);
        }
        to {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }

    .branch-column {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 13px;
    }

    .subnodes {
        display: none;
        flex-direction: column;
        align-items: center;
        gap: 11px;
        margin-top: 5px;
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

    .connector-main {
        width: 2px;
        height: 25px;
        background: #01ACF1;
        opacity: 0.75;
        margin-top: -6px;
        margin-bottom: -4px;
    }

    .connector-small {
        width: 2px;
        height: 15px;
        background: #01ACF1;
        opacity: 0.65;
        margin-top: -3px;
        margin-bottom: -3px;
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
        font-size: 13px;
        border-radius: 8px;
    }

    .footer {
        margin-top: 35px;
        text-align: center;
        font-size: 12px;
        color: #444444;
    }

    @media (max-width: 1150px) {
        .branches.show {
            flex-wrap: wrap;
        }

        .level-0 {
            width: 90%;
        }
    }
</style>
</head>

<body>

<div class="page">

    <div class="title">Mapa Mental Interactivo</div>
    <div class="subtitle">
        Ecuaciones Diferenciales Ordinarias aplicadas a la gestión de activos en una planta industrial
    </div>

    <div class="mindmap">

        <div class="node level-0">
            <div class="node-header">
                <span class="node-title">
                    Ecuaciones Diferenciales en el Mantenimiento Industrial
                </span>
                <button class="toggle" onclick="toggleSection('mainBranches', this)">+</button>
            </div>

            <div class="node-text">
                Las ecuaciones diferenciales permiten representar cómo cambia una variable de un sistema industrial con respecto al tiempo. 
                En mantenimiento ayudan a analizar temperatura, nivel de fluido, presión, velocidad de actuadores y comportamiento de equipos.
            </div>
        </div>

        <div class="connector-main"></div>

        <div id="mainBranches" class="branches">

            <!-- RAMA 1 -->
            <div class="branch-column">
                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">1. Fundamentos y Clasificación</span>
                        <button class="toggle" onclick="toggleSection('rama1', this)">+</button>
                    </div>

                    <div class="node-text">
                        Explica qué es una ecuación diferencial y cómo se clasifica técnicamente.
                    </div>

                    <span class="tag">Base teórica</span>
                </div>

                <div id="rama1" class="subnodes">
                    <div class="connector-small"></div>

                    <div class="node level-2">
                        <div class="node-title">Definición</div>
                        <div class="node-text">
                            Una ecuación diferencial relaciona una función desconocida con una o más de sus derivadas.
                            En mantenimiento se usa para estudiar cómo cambia una magnitud como temperatura, presión, nivel o velocidad con el tiempo.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Orden</div>
                        <div class="node-text">
                            El orden se determina por la derivada más alta presente en la ecuación.
                            Si aparece dy/dt, es de primer orden. Si aparece d²y/dt², es de segundo orden.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Linealidad</div>
                        <div class="node-text">
                            Una ecuación diferencial es lineal cuando la variable dependiente y sus derivadas están elevadas al exponente 1.
                            Además, no deben multiplicarse entre sí.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Tipo: EDO vs EDP</div>
                        <div class="node-text">
                            Una EDO usa derivadas respecto a una sola variable independiente, normalmente el tiempo.
                            Una EDP usa derivadas parciales respecto a dos o más variables independientes.
                        </div>
                    </div>
                </div>
            </div>

            <!-- RAMA 2 -->
            <div class="branch-column">
                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">2. Herramientas de Resolución</span>
                        <button class="toggle" onclick="toggleSection('rama2', this)">+</button>
                    </div>

                    <div class="node-text">
                        Presenta métodos básicos usados para resolver ecuaciones diferenciales de primer orden.
                    </div>

                    <span class="tag">Métodos</span>
                </div>

                <div id="rama2" class="subnodes">
                    <div class="connector-small"></div>

                    <div class="node level-2">
                        <div class="node-title">Variables Separables</div>
                        <div class="node-text">
                            Es un método donde se reorganiza la ecuación para dejar una variable en un lado y la otra variable en el otro lado.
                            Luego se integran ambos lados para obtener la solución.
                        </div>
                        <div class="formula">
                            Forma general: dy/dx = f(x)g(y)
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Factor Integrante</div>
                        <div class="node-text">
                            Se aplica a EDOs lineales de primer orden. Consiste en multiplicar toda la ecuación por una función especial
                            que permite convertirla en una derivada de producto y facilitar la integración.
                        </div>
                        <div class="formula">
                            Forma lineal: y' + p(x)y = q(x)
                        </div>
                    </div>
                </div>
            </div>

            <!-- RAMA 3 -->
            <div class="branch-column">
                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">3. Modelos de Procesos</span>
                        <button class="toggle" onclick="toggleSection('rama3', this)">+</button>
                    </div>

                    <div class="node-text">
                        Relaciona las EDO con procesos reales presentes en una planta industrial.
                    </div>

                    <span class="tag">Aplicación</span>
                </div>

                <div id="rama3" class="subnodes">
                    <div class="connector-small"></div>

                    <div class="node level-2">
                        <div class="node-title">Termicidad: Ley de Newton</div>
                        <div class="node-text">
                            La Ley de Newton del enfriamiento modela cómo cambia la temperatura de un cuerpo según la diferencia
                            entre su temperatura y la temperatura del ambiente.
                            Se aplica en el enfriamiento de motores, rodamientos y componentes sometidos a calentamiento.
                        </div>
                        <div class="formula">
                            dT/dt = -k(T - Ta)
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Fluidos: Ley de Torricelli</div>
                        <div class="node-text">
                            La Ley de Torricelli permite modelar el vaciado de un tanque según la altura del fluido.
                            En planta se puede aplicar a tanques de lubricante, agua o productos químicos.
                        </div>
                        <div class="formula">
                            v = √(2gh)
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Sistemas: Actuadores Hidráulicos</div>
                        <div class="node-text">
                            La dinámica de actuadores hidráulicos permite analizar cómo cambia la posición, velocidad o presión de un actuador con el tiempo.
                            Sirve para estudiar la respuesta del sistema ante una entrada, una carga o una variación de presión.
                        </div>
                    </div>
                </div>
            </div>

            <!-- RAMA 4 -->
            <div class="branch-column">
                <div class="node level-1">
                    <div class="node-header">
                        <span class="node-title">4. Valor para el Mantenimiento</span>
                        <button class="toggle" onclick="toggleSection('rama4', this)">+</button>
                    </div>

                    <div class="node-text">
                        Muestra cómo los modelos matemáticos ayudan al diagnóstico y a la prevención de fallas.
                    </div>

                    <span class="tag">Diagnóstico</span>
                </div>

                <div id="rama4" class="subnodes">
                    <div class="connector-small"></div>

                    <div class="node level-2">
                        <div class="node-title">Constante de tiempo τ</div>
                        <div class="node-text">
                            La constante de tiempo indica qué tan rápido responde un sistema ante un cambio.
                            Si τ aumenta, el sistema responde más lento, lo que puede indicar mayor fricción, desgaste,
                            suciedad, pérdida de eficiencia o degradación del fluido.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Predicción de estados futuros</div>
                        <div class="node-text">
                            Las EDO permiten estimar cómo se comportará un equipo después de cierto tiempo.
                            Por ejemplo, qué temperatura alcanzará un motor o cuánto tardará en vaciarse un tanque.
                        </div>
                    </div>

                    <div class="node level-2">
                        <div class="node-title">Toma de decisiones preventivas</div>
                        <div class="node-text">
                            Con los parámetros matemáticos se puede decidir cuándo inspeccionar, lubricar,
                            ajustar o reemplazar un componente antes de que ocurra una falla.
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="footer">
        Mapa mental elaborado para relacionar teoría de EDO con mantenimiento industrial y gestión de activos.
    </div>

</div>

<script>
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

    function updateBodyState() {
        const mainBranches = document.getElementById("mainBranches");
        const openSubnodes = document.querySelectorAll(".subnodes.show");

        if (mainBranches.classList.contains("show")) {
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

components.html(html_code, height=950, scrolling=True)
