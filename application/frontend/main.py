import streamlit as st
from requests.exceptions import RequestException, Timeout

from config     import PAGE_TITLE, PAGE_ICON, APP_VERSION
from styles     import GLOBAL_CSS
from helpers    import check_backend, call_predict, build_payload
from components import (
    render_sidebar,
    render_header,
    render_kpi_cards,
    render_input_form,
    render_result,
    render_footer,
)

# Konfigurasi awal halaman Streamlit (harus dipanggil pertama sebelum komponen lain)
# =========================
# PAGE CONFIG  (must be first Streamlit call)
# =========================
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Menyisipkan CSS global untuk mengatur tampilan dan tema aplikasi 
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# Mengecek status backend FastAPI untuk memastikan layanan siap digunakan
backend_ok, backend_info = check_backend()

# Menyusun layout utama aplikasi (sidebar, header, KPI, dan form input)
render_sidebar(backend_ok, backend_info)
render_header(APP_VERSION)
render_kpi_cards(backend_ok)

st.markdown("<br>", unsafe_allow_html=True)

inputs, submitted = render_input_form()

# Menjalankan proses prediksi ketika tombol submit ditekan
if submitted:
    if not backend_ok:
        st.error("⚠️ Backend tidak aktif. Jalankan FastAPI terlebih dahulu, lalu refresh halaman ini.")
        st.stop()

    payload = build_payload(**inputs)

    with st.spinner("Memproses prediksi, mohon tunggu…"):
        try:
            result      = call_predict(payload)
            prediction  = int(result.get("prediction", 0))
            probability = result.get("probability", None)

            render_result(prediction, probability, payload, result)

        except Timeout:
            st.error("⏱ Request timeout. Pastikan backend merespons dan model sudah ter-load.")
        except RequestException as e:
            st.error(f"🔌 Gagal terhubung ke backend: {e}")
        except Exception as e:
            st.error(f"❌ Error tak terduga: {e}")

# Menampilkan footer sebagai penutup halaman aplikasi
render_footer()