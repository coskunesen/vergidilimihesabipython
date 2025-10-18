import streamlit as st
st.title("2025  Vergi Dilimi Hesabı")
brut_gelir = st.number_input("Yıllık Brüt Gelir (TL):", min_value=0.0, step=1000.0)

ucret_geliri = st.selectbox("Gelir Türü:", ["Ücret Geliri", "Ücret Dışı Gelir"])
ucret_mi = True if ucret_geliri == "Ücret Geliri" else False
net_gelir = 0
st.subheader("📊 Sonuçlar")
if ucret_mi:
    if brut_gelir <= 158000:
        vergi = brut_gelir * 0.15
        st.write("Gelir Türü: Ücretli")
        st.write("Vergi Dilimi: 0.15")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir=brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        if brut_gelir > 0:
            st.progress(min(vergi / brut_gelir, 1.0))

    elif brut_gelir <= 330000:
        vergi = 23700 + (brut_gelir - 158000) * 0.20
        st.write("Gelir Türü: Ücretli")
        st.write("Vergi Dilimi: 0.20")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu

    elif brut_gelir <= 1200000:
        vergi = 58100 + (brut_gelir - 330000) * 0.27
        st.write("Gelir Türü: Ücretli")
        st.write("Vergi Dilimi: 0.27")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu

    elif brut_gelir <= 4300000:
        vergi = 293000 + (brut_gelir - 1200000) * 0.35
        st.write("Gelir Türü: Ücretli")
        st.write("Vergi Dilimi: 0.35")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu


    else:
        vergi = 1378000 + (brut_gelir - 4300000) * 0.40
        st.write("Gelir Türü: Ücretli")
        st.write("Vergi Dilimi: 0.40")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu

else:  # Ücret dışı gelir
    if brut_gelir <= 158000:
        vergi = brut_gelir * 0.15
        st.write("Gelir Türü: Ücret Dışı")
        st.write("Vergi Dilimi: 0.15")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        if brut_gelir > 0:
            st.progress(min(vergi / brut_gelir, 1.0))

    elif brut_gelir <= 330000:
        vergi = 23700 + (brut_gelir - 158000) * 0.20
        st.write("Gelir Türü: Ücret Dışı")
        st.write("Vergi Dilimi: 0.20")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu

    elif brut_gelir <= 800000:
        vergi = 58100 + (brut_gelir - 330000) * 0.27
        st.write("Gelir Türü: Ücret Dışı")
        st.write("Vergi Dilimi: 0.27")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu

    elif brut_gelir <= 4300000:
        vergi = 185000 + (brut_gelir - 800000) * 0.35
        st.write("Gelir Türü: Ücret Dışı")
        st.write("Vergi Dilimi: 0.35")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu

    else:
        vergi = 1410000 + (brut_gelir - 4300000) * 0.40

        st.write("Gelir Türü: Ücret Dışı")
        st.write("Vergi Dilimi: 0.40")
        st.write("Yıl Sonu Vergi kesinti tutarı: ", vergi)
        net_gelir = brut_gelir - vergi
        st.write("Yıl Sonu Net Kazanç: ", net_gelir)
        st.progress(min(vergi / brut_gelir, 1.0))  # oran çubuğu

st.info("Not: Hesaplama 2025 yılı gelir vergisi dilimlerine göre yapılmıştır.")
