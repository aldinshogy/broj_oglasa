import streamlit as st
from datetime import datetime

# Naslov aplikacije
st.title("Kalkulator dostupnih oglasa")

# Ulaz: Datum registracije
datum_registracije = st.date_input(
    "Odaberi datum registracije:",
    value=datetime(2009, 10, 6),  # podrazumijevani datum
    min_value=datetime(2000, 1, 1),
    max_value=datetime.today()
)

# Trenutni datum
danas = datetime.today().date()

# Početni broj oglasa
pocetni_oglasi = 20

# Izračunavanje broja punih godina koje su prošle
pune_godine = danas.year - datum_registracije.year
if (danas.month, danas.day) < (datum_registracije.month, datum_registracije.day):
    pune_godine -= 1

# Svake godine dodaješ 5 novih oglasa
dodatni_oglasi = pune_godine * 5
ukupno_oglasa = pocetni_oglasi + dodatni_oglasi

# Prikaz rezultata
st.write(f"📅 Datum registracije: **{datum_registracije}**")
st.write(f"📅 Današnji datum: **{danas}**")
st.write(f"🔢 Broj punih godina: **{pune_godine}**")
st.write(f"📦 Ukupan broj dostupnih oglasa: **{ukupno_oglasa}**")
