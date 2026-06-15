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
        background: #FFFFFF;
        color: #000000;
        font-family: Inter, Roboto, Arial, Helvetica, sans-serif;
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
        background: #FFFFFF;
    }

    .scale-wrap {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 1200px;
        height: 720px;
        transform: translate(-50%, -50%) scale(var(--fit-scale, 1));
        transform-origin: center center;
        background: #FFFFFF;
    }

    svg.connections {
        position: absolute;
        left: 0;
        top: 0;
        width: 1200px;
        height: 720px;
        z-index: 1;
        overflow: visible;
    }

    .node {
        position: absolute;
        background: #FFFFFF;
        border: 2px solid #01ACF1;
        border-radius: 14px;
        color: #000000;
        padding: 10px 12px;
        z-index: 2;
        box-shadow: none;
    }

    .center-node {
        left: 475px;
        top: 305px;
        width: 250px;
        min-height: 100px;
        border-width: 3px;
        text-align: center;
    }

    .main-node {
        width: 210px;
        min-height: 92px;
    }

    .sub-node {
        width: 205px;
        min-height: 58px;
        border-width: 2px;
    }

    .node-title {
        font-size: 12.5px;
        font-weight: 800;
        line-height: 1.18;
        margin-bottom: 5px;
    }

    .center-node .node-title {
        font-size: 14px;
        margin-bottom: 7px;
    }

    .main-node .node-title {
        font-size: 12.5px;
    }

    .sub-node .node-title {
        font-size: 11.5px;
    }

    .node-text {
        font-size: 10.5px;
        line-height: 1.28;
        font-weight: 400;
        color: #111111;
    }

    .center-node .node-text {
        font-size: 11px;
        line-height: 1.30;
    }

    .tag {
        display: inline-block;
        margin-top: 6px;
        padding: 3px 8px;
        border: 1.5px solid #01ACF1;
        border-radius: 20px;
        background: #FFFFFF;
        color: #000000;
        font-size: 9.5px;
        font-weight: 700;
    }

    .formula {
        margin-top: 5px;
        padding: 4px 6px;
        border: 1.5px solid #01ACF1;
        border-radius: 8px;
        background: #FFFFFF;
        font-size: 10px;
        font-weight: 600;
        text-align: center;
    }

    /* Bloques principales */
    .main-1 { left: 290px; top: 120px; }
    .main-2 { left: 290px; top: 510px; }
    .main-3 { left: 700px; top: 120px; }
    .main-4 { left: 700px; top: 510px; }

    /* Subbloques izquierda superior */
    .sub-1a { left: 40px; top: 35px; }
    .sub-1b { left: 40px; top: 125px; }
    .sub-1c { left: 40px; top: 215px; }
    .sub-1d { left: 40px; top: 305px; }

    /* Subbloques izquierda inferior */
    .sub-2a { left: 40px; top: 470px; min-height: 78px; }
    .sub-2b { left: 40px; top: 575px; min-height: 78px; }

    /* Subbloques derecha superior */
    .sub-3a { left: 955px; top: 40px; min-height: 76px; }
    .sub-3b { left: 955px; top: 145px; min-height: 76px; }
    .sub-3c { left: 955px; top: 250px; min-height: 70px; }

    /* Subbloques derecha inferior */
    .sub-4a { left: 955px; top: 470px; min-height: 70px; }
    .sub-4b { left: 955px; top: 555px; min-height: 66px; }
    .sub-4c { left: 955px; top: 635px; min-height: 66px; }
</style>
</head>

<body>

<div class="page">
    <div class="map-viewport">
        <div class="scale-wrap">

            <svg class="connections" viewBox="0 0 1200 720" preserveAspectRatio="none">

                <!-- Núcleo a bloques principales -->
                <path d="M475 355 L425 355 L425 166 L500 166" 
                      fill="none" stroke="#01ACF1" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>

                <path d="M475 355 L425 355 L425 556 L500 556" 
                      fill="none" stroke="#01ACF1" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>

                <path d="M725 355 L775 355 L775 166 L700 166" 
                      fill="none" stroke="#01ACF1" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>

                <path d="M725 355 L775 355 L775 556 L700 556" 
                      fill="none" stroke="#01ACF1" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>

                <!-- Rama 1 a subbloques -->
                <path d="M290 166 L260 166 L260 64 L245 64" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M260 166 L245 154" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M260 166 L260 244 L245 244" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M260 244 L260 334 L245 334" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

                <!-- Rama 2 a subbloques -->
                <path d="M290 556 L260 556 L260 509 L245 509" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M260 556 L260 614 L245 614" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

                <!-- Rama 3 a subbloques -->
                <path d="M910 166 L935 166 L935 78 L955 78" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M935 166 L955 183" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M935 166 L935 285 L955 285" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

                <!-- Rama 4 a subbloques -->
                <path d="M910 556 L935 556 L935 505 L955 505" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M935 556 L955 588" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M935 556 L935 668 L955 668" 
                      fill="none" stroke="#01ACF1" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>

            </svg>

            <!-- Nodo central -->
            <div class="node center-node">
                <div class="node-title">
                    Ecuaciones Diferenciales en el Mantenimiento Industrial
                </div>
                <div class="node-text">
                    Modelan cambios de temperatura, presión, nivel o velocidad para diagnosticar y predecir el comportamiento de equipos.
                </div>
            </div>

            <!-- Rama 1 -->
            <div class="node main-node main-1">
                <div class="node-title">1. Fundamentos y Clasificación</div>
                <div class="node-text">
                    Identifica la estructura básica de una ecuación diferencial.
                </div>
                <div class="tag">Base teórica</div>
            </div>

            <div class="node sub-node sub-1a">
                <div class="node-title">Definición</div>
                <div class="node-text">
                    Relación entre una función desconocida y sus derivadas.
                </div>
            </div>

            <div class="node sub-node sub-1b">
                <div class="node-title">Orden</div>
                <div class="node-text">
                    Lo define la derivada más alta: dy/dt es primer orden y d²y/dt² es segundo orden.
                </div>
            </div>

            <div class="node sub-node sub-1c">
                <div class="node-title">Linealidad</div>
                <div class="node-text">
                    Es lineal si la variable dependiente y sus derivadas están al exponente 1.
                </div>
            </div>

            <div class="node sub-node sub-1d">
                <div class="node-title">Tipo</div>
                <div class="node-text">
                    EDO: una variable independiente. EDP: dos o más variables independientes.
                </div>
            </div>

            <!-- Rama 2 -->
            <div class="node main-node main-2">
                <div class="node-title">2. Herramientas de Resolución</div>
                <div class="node-text">
                    Métodos básicos para resolver EDOs de primer orden.
                </div>
                <div class="tag">Métodos</div>
            </div>

            <div class="node sub-node sub-2a">
                <div class="node-title">Variables Separables</div>
                <div class="node-text">
                    Se separan las variables en lados distintos y luego se integran.
                </div>
                <div class="formula">dy/dx = f(x)g(y)</div>
            </div>

            <div class="node sub-node sub-2b">
                <div class="node-title">Factor Integrante</div>
                <div class="node-text">
                    Se aplica a EDOs lineales de primer orden para facilitar la integración del producto.
                </div>
                <div class="formula">y' + p(x)y = q(x)</div>
            </div>

            <!-- Rama 3 -->
            <div class="node main-node main-3">
                <div class="node-title">3. Modelos de Procesos</div>
                <div class="node-text">
                    Aplican las EDO al análisis de procesos reales en planta.
                </div>
                <div class="tag">Aplicación</div>
            </div>

            <div class="node sub-node sub-3a">
                <div class="node-title">Termicidad</div>
                <div class="node-text">
                    Ley de Newton: enfriamiento de motores y rodamientos.
                </div>
                <div class="formula">dT/dt = -k(T - Ta)</div>
            </div>

            <div class="node sub-node sub-3b">
                <div class="node-title">Fluidos</div>
                <div class="node-text">
                    Ley de Torricelli: vaciado de tanques de lubricante o químicos.
                </div>
                <div class="formula">v = √(2gh)</div>
            </div>

            <div class="node sub-node sub-3c">
                <div class="node-title">Sistemas</div>
                <div class="node-text">
                    Dinámica de actuadores hidráulicos: presión, velocidad y posición.
                </div>
            </div>

            <!-- Rama 4 -->
            <div class="node main-node main-4">
                <div class="node-title">4. Valor para el Mantenimiento</div>
                <div class="node-text">
                    Convierte modelos matemáticos en diagnóstico y prevención.
                </div>
                <div class="tag">Diagnóstico</div>
            </div>

            <div class="node sub-node sub-4a">
                <div class="node-title">Constante de tiempo τ</div>
                <div class="node-text">
                    Indica rapidez de respuesta. Si aumenta, puede existir fricción o degradación del fluido.
                </div>
            </div>

            <div class="node sub-node sub-4b">
                <div class="node-title">Predicción</div>
                <div class="node-text">
                    Estima estados futuros de temperatura, presión, nivel o velocidad.
                </div>
            </div>

            <div class="node sub-node sub-4c">
                <div class="node-title">Decisiones preventivas</div>
                <div class="node-text">
                    Permite programar inspección, lubricación, ajuste o reemplazo antes de la falla.
                </div>
            </div>

        </div>
    </div>
</div>

<script>
    function fitCanvas() {
        const viewport = document.querySelector(".map-viewport");
        const wrap = document.querySelector(".scale-wrap");

        const canvasWidth = 1200;
        const canvasHeight = 720;

        const scaleX = viewport.clientWidth / canvasWidth;
        const scaleY = viewport.clientHeight / canvasHeight;

        const scale = Math.min(scaleX, scaleY, 1);

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
