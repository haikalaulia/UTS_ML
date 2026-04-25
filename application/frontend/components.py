import streamlit as st
from config import APP_VERSION, MODEL_NAME, MODEL_TUNING, MODEL_TASK, MODEL_TARGET
from helpers import confidence_label, format_prediction


# Fungsi untuk menampilkan sidebar aplikasi yang berisi informasi sistem, status backend, detail model, dan panduan penggunaan
def render_sidebar(backend_ok: bool, backend_info: dict) -> None:
    with st.sidebar:
        st.markdown(
            f"""
            <div class="sidebar-logo">🌿 AgroSense</div>
            <div class="sidebar-sub">
                Prediksi kegagalan pertumbuhan tanaman berbasis kondisi tanah dan
                lingkungan menggunakan Machine Learning.
            </div>
            """,
            unsafe_allow_html=True,
        )

        # — Status —
        st.markdown('<div class="sidebar-section">Status Sistem</div>', unsafe_allow_html=True)
        dot   = "status-dot-ok" if backend_ok else "status-dot-off"
        label = "Backend Online"  if backend_ok else "Backend Offline"
        note  = "Model siap digunakan" if backend_ok else backend_info.get("error", "Tidak diketahui")
        st.markdown(
            f"""
            <div class="sidebar-row">
                <span class="sidebar-row-key">
                    <span class="{dot}" style="margin-right:7px;"></span>API
                </span>
                <span class="sidebar-row-val">{label}</span>
            </div>
            <div style="font-size:0.76rem;color:var(--text-dim);margin:-2px 0 10px 12px;">{note}</div>
            """,
            unsafe_allow_html=True,
        )

        # — Model Info —
        st.markdown('<div class="sidebar-section">Model Info</div>', unsafe_allow_html=True)
        for key, val in [
            ("Algoritma", MODEL_NAME),
            ("Tuning",    MODEL_TUNING),
            ("Task",      MODEL_TASK),
            ("Target",    MODEL_TARGET),
        ]:
            st.markdown(
                f'<div class="sidebar-row">'
                f'<span class="sidebar-row-key">{key}</span>'
                f'<span class="sidebar-row-val">{val}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )

        # — Guide —
        st.markdown('<div class="sidebar-section">Panduan</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div style="font-size:0.82rem;color:var(--text-dim);line-height:1.7;padding:0 4px;">
                ① Isi seluruh parameter input<br>
                ② Pastikan backend FastAPI aktif<br>
                ③ Tekan tombol <b style="color:var(--green)">Predict</b><br>
                ④ Baca hasil dan probabilitas
            </div>
            """,
            unsafe_allow_html=True,
        )


# Fungsi untuk menampilkan header utama aplikasi yang mencakup versi, judul sistem, dan deskripsi singkat model
def render_header(version: str = APP_VERSION) -> None:
    st.markdown(
        f"""
        <div class="hero-badge">Agro ML · {version}</div>
        <div class="main-title">Agro-Environmental<br>Prediction System</div>
        <div class="subtitle">
            Masukkan kondisi tanah, nutrisi, dan lingkungan untuk memprediksi apakah
            tanaman berisiko gagal tumbuh menggunakan model
            <em>Random Forest Tuned</em>.
        </div>
        """,
        unsafe_allow_html=True,
    )


# Fungsi untuk menampilkan KPI cards sebagai ringkasan informasi sistem seperti status API, jenis model, tipe task, dan target variabel
def render_kpi_cards(backend_ok: bool) -> None:
    col_a, col_b, col_c, col_d = st.columns(4)

    pill_cls = "kpi-pill-ok" if backend_ok else "kpi-pill-off"
    pill_txt = "Online"       if backend_ok else "Offline"

    with col_a:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">API Status</div>
                <div class="kpi-value">FastAPI</div>
                <span class="kpi-pill {pill_cls}">{pill_txt}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">Model</div>
                <div class="kpi-value">Random Forest</div>
                <span class="kpi-pill kpi-pill-info">Tuned</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_c:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">Task Type</div>
                <div class="kpi-value">Classification</div>
                <span class="kpi-pill kpi-pill-info">Binary</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_d:
        st.markdown(
            """
            <div class="kpi-card">
                <div class="kpi-label">Target Variable</div>
                <div class="kpi-value">failure_flag</div>
                <span class="kpi-pill kpi-pill-ok">0 / 1</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


# Fungsi untuk menampilkan form input parameter yang dibagi menjadi dua tab (tanah & lingkungan serta nutrisi & tanaman) dan mengembalikan data input beserta status submit
def render_input_form() -> tuple[dict, bool]:
    """
    Renders the two-tab input form.
    Returns (raw_inputs dict, submit bool).
    """
    st.markdown('<div class="section-label">Parameter Input</div>', unsafe_allow_html=True)

    inputs = {}

    with st.form("prediction_form", clear_on_submit=False):
        tab1, tab2 = st.tabs(["🌍  Tanah & Lingkungan", "🌿  Nutrisi & Tanaman"])

        with tab1:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Tipe & Fisik Tanah**")
                inputs["soil_type"]               = st.selectbox("Soil Type", ["Clayey", "Alluvial", "Sandy", "Loamy"])
                inputs["bulk_density"]             = st.number_input("Bulk Density", min_value=0.0, value=1.20, step=0.01, format="%.2f")
                inputs["organic_matter_pct"]       = st.number_input("Organic Matter (%)", min_value=0.0, value=3.50, step=0.1, format="%.2f")
                inputs["cation_exchange_capacity"] = st.number_input("Cation Exchange Capacity", min_value=0.0, value=25.0, step=0.5, format="%.2f")
                inputs["salinity_ec"]              = st.number_input("Salinity EC", min_value=0.0, value=0.50, step=0.01, format="%.2f")
                inputs["buffering_capacity"]       = st.number_input("Buffering Capacity", min_value=0.0, value=0.80, step=0.01, format="%.2f")
            with c2:
                st.markdown("**Kelembaban & Suhu**")
                inputs["soil_moisture_pct"]  = st.number_input("Soil Moisture (%)", min_value=0.0, value=20.0, step=0.1, format="%.2f")
                inputs["moisture_limit_dry"] = st.number_input("Moisture Limit Dry", min_value=0.0, value=15.0, step=0.1, format="%.2f")
                inputs["moisture_limit_wet"] = st.number_input("Moisture Limit Wet", min_value=0.0, value=45.0, step=0.1, format="%.2f")
                inputs["moisture_regime"]    = st.selectbox("Moisture Regime", ["dry", "optimal", "wet"])
                inputs["soil_temp_c"]        = st.number_input("Soil Temperature (°C)", min_value=-20.0, value=25.0, step=0.1, format="%.2f")
                inputs["air_temp_c"]         = st.number_input("Air Temperature (°C)", min_value=-20.0, value=28.0, step=0.1, format="%.2f")
                inputs["thermal_regime"]     = st.selectbox("Thermal Regime", ["optimal", "heat_stress", "cold_stress"])

        with tab2:
            c3, c4 = st.columns(2)
            with c3:
                st.markdown("**Nutrisi Tanah**")
                inputs["light_intensity_par"] = st.number_input("Light Intensity PAR", min_value=0.0, value=800.0, step=10.0, format="%.2f")
                inputs["soil_ph"]             = st.number_input("Soil pH", min_value=0.0, value=6.50, step=0.01, format="%.2f")
                inputs["ph_stress_flag"]      = st.selectbox("pH Stress Flag", [0, 1])
                inputs["nitrogen_ppm"]        = st.number_input("Nitrogen (ppm)", min_value=0.0, value=100.0, step=0.1, format="%.2f")
                inputs["phosphorus_ppm"]      = st.number_input("Phosphorus (ppm)", min_value=0.0, value=50.0, step=0.1, format="%.2f")
                inputs["potassium_ppm"]       = st.number_input("Potassium (ppm)", min_value=0.0, value=120.0, step=0.1, format="%.2f")
            with c4:
                st.markdown("**Kategori Tanaman**")
                inputs["nutrient_balance"] = st.selectbox("Nutrient Balance", ["optimal", "deficient", "excessive"])
                inputs["plant_category"]   = st.selectbox("Plant Category", ["vegetable", "fruit", "grain"])
                st.markdown(
                    """
                    <div class="tips-box">
                        💡 <strong style="color:var(--green)">Tips:</strong>
                        Pastikan nilai input mencerminkan kondisi nyata lahan.
                        Nilai yang tidak realistis dapat memengaruhi akurasi prediksi.
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown("<br>", unsafe_allow_html=True)
        col_btn, _ = st.columns([1, 3])
        with col_btn:
            submit = st.form_submit_button("🔍  Jalankan Prediksi", use_container_width=True)

    return inputs, submit


# Fungsi untuk menampilkan hasil prediksi model termasuk status (berisiko/tidak), confidence, visualisasi probabilitas, serta data request dan response
def render_result(prediction: int, probability: float | None, payload: dict, raw_result: dict) -> None:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Hasil Prediksi</div>', unsafe_allow_html=True)

    left, right = st.columns([1.3, 1])

    # — Verdict card —
    with left:
        label = format_prediction(prediction)
        if prediction == 1:
            st.markdown(
                f"""
                <div class="result-card result-card-bad">
                    <span class="result-icon">⚠️</span>
                    <div class="result-title">{label}</div>
                    <div class="result-desc">
                        Model mendeteksi adanya risiko kegagalan tumbuh berdasarkan
                        kombinasi kondisi tanah, nutrisi, dan lingkungan yang dimasukkan.
                        Pertimbangkan perbaikan pada parameter yang anomali.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="result-card result-card-ok">
                    <span class="result-icon">✅</span>
                    <div class="result-title">{label}</div>
                    <div class="result-desc">
                        Kondisi yang dimasukkan diprediksi mendukung pertumbuhan tanaman
                        secara optimal. Lanjutkan pemantauan rutin untuk mempertahankan
                        kondisi ini.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # — Probability panel —
    with right:
        st.markdown(
            '<div style="font-family:\'Syne\',sans-serif;font-size:0.72rem;font-weight:700;'
            'letter-spacing:0.1em;text-transform:uppercase;color:var(--text-dim);'
            'margin-bottom:1rem;">Ringkasan Probabilitas</div>',
            unsafe_allow_html=True,
        )
        m1, m2 = st.columns(2)
        with m1:
            st.metric("Class", prediction)
        with m2:
            if probability is not None:
                st.metric("Confidence", confidence_label(float(probability)))

        if probability is not None:
            _render_probability_bar(prediction, float(probability))
        else:
            st.caption("Probabilitas tidak tersedia dari backend.")

    # — Raw data expanders —
    st.markdown("<br>", unsafe_allow_html=True)
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        with st.expander("📤 Lihat payload yang dikirim"):
            st.json(payload)
    with col_e2:
        with st.expander("📥 Lihat response backend"):
            st.json(raw_result)


# Fungsi internal untuk menampilkan visualisasi bar probabilitas berdasarkan nilai confidence dari model
def _render_probability_bar(prediction: int, probability: float) -> None:
    prob_pct  = probability * 100
    bar_color = "#e85c5c" if prediction == 1 else "#5ed282"
    st.markdown(
        f"""
        <div style="margin-top:14px;">
            <div style="display:flex;justify-content:space-between;margin-bottom:6px;">
                <span style="font-size:0.78rem;color:var(--text-muted);">Probabilitas Gagal</span>
                <span style="font-family:'Syne',sans-serif;font-size:0.88rem;font-weight:700;
                             color:{bar_color};">{probability:.4f}</span>
            </div>
            <div style="background:rgba(255,255,255,0.06);border-radius:100px;height:8px;overflow:hidden;">
                <div style="width:{prob_pct:.1f}%;height:100%;background:{bar_color};border-radius:100px;
                            transition:width 0.8s ease;box-shadow:0 0 10px {bar_color}55;"></div>
            </div>
            <div style="display:flex;justify-content:space-between;margin-top:5px;">
                <span style="font-size:0.72rem;color:var(--text-dim);">0%</span>
                <span style="font-size:0.72rem;color:var(--text-dim);">100%</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Fungsi untuk menampilkan footer aplikasi yang berisi identitas sistem dan teknologi yang digunakan
def render_footer() -> None:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="
            border-top: 1px solid var(--border);
            padding-top: 1.2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
        ">
            <span style="font-family:'Syne',sans-serif;font-size:0.82rem;color:var(--text-dim);">
                🌿 <strong style="color:var(--green)">AgroSense</strong> ML Dashboard
            </span>
            <span style="font-size:0.78rem;color:var(--text-dim);">
                FastAPI · Streamlit · Random Forest &nbsp;|&nbsp; UTS Praktikum Machine Learning
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )