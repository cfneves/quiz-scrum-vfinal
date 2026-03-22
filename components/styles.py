PREMIUM_CSS = """
<style>
/* === TIPOGRAFIA === */
html, body, [class*="css"] {
    font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
}

/* === BOTÕES PRIMÁRIOS === */
.stButton > button {
    background: linear-gradient(135deg, #00BFFF 0%, #0080FF 100%);
    border: none;
    border-radius: 10px;
    color: #fff;
    font-weight: 600;
    font-size: 0.95rem;
    padding: 0.55rem 1.5rem;
    transition: all 0.25s ease;
    box-shadow: 0 4px 15px rgba(0, 191, 255, 0.2);
    letter-spacing: 0.02em;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 191, 255, 0.4);
    background: linear-gradient(135deg, #1acfff 0%, #1090ff 100%);
    border: none;
}
.stButton > button:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(0, 191, 255, 0.2);
}

/* === INPUTS === */
.stTextInput > div > div > input {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(0, 191, 255, 0.2);
    border-radius: 10px;
    color: #F0F0F0;
    padding: 0.5rem 0.9rem;
    transition: border-color 0.2s, box-shadow 0.2s;
}
.stTextInput > div > div > input:focus {
    border-color: #00BFFF;
    box-shadow: 0 0 0 3px rgba(0, 191, 255, 0.12);
}
.stTextInput > div > div > input::placeholder {
    color: #555;
}

/* === CARDS DE MÉTRICAS === */
[data-testid="metric-container"] {
    background: rgba(0, 191, 255, 0.04);
    border: 1px solid rgba(0, 191, 255, 0.15);
    border-radius: 14px;
    padding: 1rem;
    text-align: center;
    transition: border-color 0.2s;
}
[data-testid="metric-container"]:hover {
    border-color: rgba(0, 191, 255, 0.35);
}

/* === BARRA DE PROGRESSO === */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #00BFFF, #0080FF);
    border-radius: 99px;
}

/* === RADIO BUTTONS === */
.stRadio > div {
    gap: 0.4rem;
}
.stRadio [data-testid="stMarkdownContainer"] p {
    font-size: 0.95rem;
    line-height: 1.5;
}

/* === ALERTAS === */
.stSuccess, .stError, .stWarning, .stInfo {
    border-radius: 10px;
}

/* === SIDEBAR === */
[data-testid="stSidebar"] {
    background: rgba(10, 14, 26, 0.98);
    border-right: 1px solid rgba(0, 191, 255, 0.08);
}

/* === DIVIDER === */
hr {
    border-color: rgba(0, 191, 255, 0.1) !important;
    margin: 1.5rem 0;
}

/* === SPINNER === */
.stSpinner > div {
    border-top-color: #00BFFF !important;
}

/* === SUBHEADERS === */
h2, h3 {
    letter-spacing: -0.3px;
}
</style>
"""
