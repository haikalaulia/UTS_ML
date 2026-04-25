GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Root Variables ── */
:root {
    --bg:          #0d1210;
    --bg-card:     #131a16;
    --bg-glass:    rgba(255,255,255,0.035);
    --border:      rgba(255,255,255,0.07);
    --border-glow: rgba(94,210,130,0.35);
    --green:       #5ed282;
    --green-dim:   #3a9957;
    --amber:       #f0b429;
    --red:         #e85c5c;
    --text:        #e8ede9;
    --text-muted:  #7a8c7e;
    --text-dim:    #4a5e4e;
    --radius:      14px;
    --radius-lg:   20px;
}

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}
.block-container {
    padding: 2rem 2.5rem 3rem !important;
    max-width: 1400px !important;
}

/* ── Streamlit Overrides ── */
.stApp { background: var(--bg) !important; }

section[data-testid="stSidebar"] {
    background: #0b100d !important;
    border-right: 1px solid var(--border) !important;
}

.stButton > button {
    background: var(--green) !important;
    color: #0d1210 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.03em !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.65rem 2rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 0 24px rgba(94,210,130,0.25) !important;
}
.stButton > button:hover {
    background: #7aeba0 !important;
    box-shadow: 0 0 36px rgba(94,210,130,0.4) !important;
    transform: translateY(-1px) !important;
}

.stTabs [data-baseweb="tab-list"] {
    background: var(--bg-card) !important;
    border-radius: var(--radius) !important;
    border: 1px solid var(--border) !important;
    padding: 4px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--text-muted) !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 0.5rem 1.4rem !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    background: var(--green) !important;
    color: #0d1210 !important;
}

.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: #1a2420 !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stSelectbox > div > div:focus-within,
.stNumberInput > div > div > input:focus {
    border-color: var(--green-dim) !important;
    box-shadow: 0 0 0 3px rgba(94,210,130,0.12) !important;
}

label, .stSelectbox label, .stNumberInput label {
    color: var(--text-muted) !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase !important;
}

.stSuccess, .stError { border-radius: var(--radius) !important; }

.stExpander {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}

.stMarkdown h3 { font-family: 'Syne', sans-serif !important; }

div[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.6rem !important;
    font-weight: 700 !important;
    color: var(--green) !important;
}
div[data-testid="stMetricLabel"] {
    font-size: 0.78rem !important;
    color: var(--text-muted) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

.stInfo {
    background: rgba(94,210,130,0.07) !important;
    border: 1px solid rgba(94,210,130,0.2) !important;
    border-radius: var(--radius) !important;
    color: var(--text-muted) !important;
}

hr { border-color: var(--border) !important; }

/* ── Custom Components ── */
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(94,210,130,0.1);
    border: 1px solid rgba(94,210,130,0.25);
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 0.78rem;
    font-weight: 600;
    font-family: 'Syne', sans-serif;
    color: var(--green);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-badge::before {
    content: '';
    display: inline-block;
    width: 7px;
    height: 7px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse 2s ease infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.5; transform: scale(0.75); }
}

.main-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin: 0.3rem 0 0.6rem;
    background: linear-gradient(135deg, #e8ede9 0%, #5ed282 60%, #3a9957 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.subtitle {
    font-size: 0.97rem;
    color: var(--text-muted);
    line-height: 1.65;
    max-width: 700px;
    margin-bottom: 2rem;
    font-weight: 300;
}

.kpi-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 20px 22px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--green), transparent);
}
.kpi-card:hover { border-color: var(--border-glow); }
.kpi-label {
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 8px;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--text);
}
.kpi-pill {
    display: inline-block;
    margin-top: 8px;
    padding: 2px 10px;
    border-radius: 100px;
    font-size: 0.73rem;
    font-weight: 600;
}
.kpi-pill-ok   { background: rgba(94,210,130,0.12); color: var(--green); }
.kpi-pill-off  { background: rgba(232,92,92,0.12);  color: var(--red); }
.kpi-pill-info { background: rgba(240,180,41,0.12); color: var(--amber); }

.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 0.9rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
}

.result-card {
    border-radius: var(--radius-lg);
    padding: 24px 26px;
    position: relative;
    overflow: hidden;
}
.result-card-ok {
    background: linear-gradient(135deg, rgba(94,210,130,0.08), rgba(94,210,130,0.03));
    border: 1px solid rgba(94,210,130,0.3);
}
.result-card-bad {
    background: linear-gradient(135deg, rgba(232,92,92,0.08), rgba(232,92,92,0.03));
    border: 1px solid rgba(232,92,92,0.3);
}
.result-icon  { font-size: 2.2rem; margin-bottom: 10px; display: block; }
.result-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.35rem;
    font-weight: 800;
    margin-bottom: 6px;
}
.result-desc  { font-size: 0.9rem; color: var(--text-muted); line-height: 1.6; }
.result-card-ok  .result-title { color: var(--green); }
.result-card-bad .result-title { color: var(--red); }

/* Sidebar */
.sidebar-logo {
    font-family: 'Syne', sans-serif;
    font-size: 1.25rem;
    font-weight: 800;
    color: var(--green);
    letter-spacing: -0.01em;
    margin-bottom: 3px;
}
.sidebar-sub {
    font-size: 0.78rem;
    color: var(--text-dim);
    line-height: 1.55;
    margin-bottom: 1.5rem;
}
.sidebar-section {
    font-family: 'Syne', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin: 1.2rem 0 0.6rem;
}
.sidebar-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 12px;
    border-radius: 10px;
    background: var(--bg-glass);
    border: 1px solid var(--border);
    margin-bottom: 6px;
    font-size: 0.85rem;
}
.sidebar-row-key { color: var(--text-muted); }
.sidebar-row-val { color: var(--text); font-weight: 500; }

.status-dot-ok  {
    width:8px; height:8px; border-radius:50%; background:var(--green);
    display:inline-block; animation:pulse 2s infinite;
}
.status-dot-off {
    width:8px; height:8px; border-radius:50%; background:var(--red);
    display:inline-block;
}

.tips-box {
    background: rgba(94,210,130,0.06);
    border: 1px solid rgba(94,210,130,0.18);
    border-radius: 12px;
    padding: 14px 16px;
    margin-top: 12px;
    font-size: 0.84rem;
    color: var(--text-muted);
    line-height: 1.65;
}
</style>
"""