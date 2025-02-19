import streamlit as st
import pandas as pd
import datetime
import time
from PIL import Image

# Základem aplikace je nadpis Title
st.write("# 1. Nadpis/Titulek (Title)")

st.title("Moje aplikace s widgetmi a komponenty")

# Klasicky text - obycejny
st.write("# 2. Klasicky text")

st.write("Toto je klasicky text")

# Tlacitko - Button
st.write("# 3. Tlacitko - Button")

if st.button("Tlacitko"):
    st.write("kliknul jsi na mě :)")

# Posuvnik - SLIDER
st.write("# 4. Posuvnik - SLIDER")

# ("Nazev", min hodnota, max hodnota)
cislo = st.slider("Vyber cislo", 0, 100)
st.write(f"Vybrali jste cislo: {cislo}")

st.write("Posuvnik s defaultni hodnotou 50")
cislo_s_defaultni_hodnotou = st.slider("Vyber cislo", 0, 100, 50)
st.write(f"Vybrali jste cislo: {cislo_s_defaultni_hodnotou}")

# text input
st.write("# 5. Text input")
input = st.text_input("Zadej jmeno:")
st.write(f"Jmenuji se: {input}")

# Zaskrtavaci pole/checkbox
st.write("# 6. Zaskrtavaci pole/checkbox")

akce = st.checkbox("Zobrazit text ano/ne")
if akce:
    st.write("Text se zobrazil")


# Rozbalovaci seznam/selectbox
st.write("# 7. Rozbalovaci seznam/selectbox")

volba = st.selectbox("Vyber moznost:", ["Moznost 1","Moznost 2","Moznost 3"])
st.write(f"Vybrali jste: {volba}")

# Upload souboru (File uploader)
st.write("# 8. Upload souboru (File uploader)")

soubor = st.file_uploader("Nahrajte soubor")

if soubor is not None:
    st.write("Soubor byl nahrany")


# Upload souboru (CSV - File uploader)
st.write("# 9. CSV - File uploader")

upload_csv = st.file_uploader("Nahrajte soubor", type="csv")

if upload_csv is not None:
    st.write("Soubor byl nahrany")
    #a tady muzu zase treba vyuzit pandas a read_csv
    data_uploaded = pd.read_csv(upload_csv)
    st.write("Toto jsou nase data")
    st.dataframe(data_uploaded)


# Upload obrazku (Obrazek- File uploader)
st.write("# 10. Upload obrazku (Obrazek- File uploader)")

upload_obrazek = st.file_uploader("Nahrajte obrazek", type=["jpg","jpeg","png"])
#zobrazeni obrazku
if upload_obrazek is not None:
    #nacteni obrazku
    obrazek = Image.open(upload_obrazek)
    # zobrazeni obrazku v aplikaci
    st.image(obrazek, caption = "Obrazek, ktery jsem nahral :)", use_container_width=True)


# Tlacitko na stahnuti (Download button)
st.write("# 11. Tlacitko na stahnuti (Download button)")
# data_upload je reference vyse v bode 9., kde jsme udelali upload CSV
# csv = data_uploaded.to_csv(index=False)

# st.download_button(
#     label = "Stahnout csv",
#     data = csv,
#     file_name= "Moje_data.csv",
#     mime = "txt/csv"
# )

# Radio button/Tlacitko jedne volby
st.write("# 12. Radio button/Tlacitko jedne volby")

volba = st.radio("Vyber neco - treba oblibeny zanr filmu:", ("Akcni","Komedie","Horror"))

if volba == "Akcni":
    st.write("Vybral jsi akci filmy")

elif volba == "Komedie":
    st.write("Vybral jsi Komedie filmy")

else:
    st.write("Vybral jsi drama filmy")

# Vice vybranych moznosti button / Multiselect
st.write("# 13. Vice vybranych moznosti button / Multiselect")

vybrane_filmy = st.multiselect(
    "Vyber svoje oblibene filmy:",
    ["Matrix","Harry Potter","Vecernicek","Kacenka a strasidla"],
    placeholder="Tady muzu napsat, co chci, treba: vyber"
)

st.write(f"Vybrali jste: {', '.join(vybrane_filmy)}")



# Vyber datumu (Date input)
st.write("# 14. Vyber datumu (Date input)")

datum = st.date_input(
    "Vyber datum",
    datetime.date(2025,2,19)
)


# Vyber casu (Time input)
st.write("# 15. Vyber casu (Time input)")

cas = st.time_input(
    "Vyber cas",
    datetime.time(10,30,00)  #se sekundama HH,MM, SS - ale muze byt i bez SS
)

st.write(f"Cas je: {cas}")

# Vstup delsiho textu / Text area
st.write("# 16. Vstup delsiho textu / Text area")

st.text_area(
    "Napiste svuj nazor na film",
    # muzu zde mit i placeholder na text
    "Sem napis text..."
)


# Vstup ciselny/ Number input
st.write("# 17. Vstup ciselny/ Number input")

hodnoceni = st.number_input(
    "Zadejte hodnoceni filmu (od 1 do 10)",
    min_value=1,
    max_value=10,
    value=5
)

st.write(f"Vase hodnoceni je {hodnoceni}/10")

# Posuvnik s vybere (Select Slider)
st.write("# 18. Posuvnik s vybere (Select Slider)")

stupnice = st.select_slider(
    "Jak velmi se ti libil film",
    options=["Hrozne","Slabe","Prumer","Dobre","Vyborne"],
    # zase muzu (nemusim) definovat default value
    value = "Dobre"
)

st.write(f"Vase hodnoceni je {stupnice}")

# Posuvnik s vybere (Select Slider)
st.write("# 18 ZKOUSIM. Posuvnik s vybere (Select Slider)")

stupnice_2 = st.select_slider(
    "Jak velmi se ti libil film",
    options=["1","2","3","4","5"],
    # zase muzu (nemusim) definovat default value
    value = "3"
)

st.write(f"Vase hodnoceni je {stupnice_2}")

# Vyber barvy (Color picker)
st.write("# 19. Vyber barvy (Color picker)")

barva = st.color_picker(
    "Vyber barvu",
    "#12501A"  #muzu nastavit default
)
st.write(f"Vase barva je: {barva}")


# Indikator progresu
st.write("# 20. Indikator progresu")

progress_objekt = st.progress(0)

# for cyclus pro iteraci od 0 po 100
# for i in range (0,100):
#     #a abychom to videli, protoze vykon je rychlej, tak to pomoci time zpomalime (import time)
#     time.sleep(0.05)
#     progress_objekt.progress(i + 1)


# LaTeX zobrazeni - Matematicky vystup
st.write("# 21. LaTeX zobrazeni - Matematicky vystup")

#pythagorova veta
st.latex(r'''
    a^2 + b^2 = c^2
    '''
)

# Zobrazeni kodu s formatovanim (code)
st.write("# 22. Zobrazeni kodu s formatovanim (code)")

st.code('''
def ahoj():
    print("Ahoj streamlit!")
''', language= 'python')


# Zobrazeni JSON dat (json)
st.write("# 23. Zobrazeni JSON dat (json)")

data = {
    "jmeno" : "Petr",
    "prijmeni" : "Netolicky",
    "vek" : 30
}

st.json(data)


# Dynamicky widget (podle aktualni hodnoty obsahu)
st.write("# 24. Dynamicky widget (podle aktualni hodnoty obsahu)")

st.write("Textovy retezec")
st.write(123)
st.write({"klic":"hodnota"})


# Zobrazeni klicovych metrik (metric)
st.write("# 25. Zobrazeni klicovych metrik (metric)")

st.metric(label="Teplota",value="24°C", delta="2°C")


# Zobrazeni zprav
st.write("# 26. Zobrazeni zprav - typy")

st.error("Chybove hlaseni")
st.success("Uloha uspesne dokoncena")
st.warning("Toto je varovani")
st.info("Toto je informacni zprava")


# Zobrazeni spinneru pri nacitani
st.write("# 26. Zobrazeni spinneru pri nacitani")

# with st.spinner("Cekejte prosim..."):
#     # zase abychom to videli tam import kniznice time a sleep(8 sekundy zpomali to nacitani)
#     time.sleep(8)
# st.success("Hotovo!")

# Zobrazeni textove poznamky
st.write("# 27. Zobrazeni textove poznamky")

st.caption("Toto je poznamka")


# Obrazek z webu nacteni
st.write("# 28. Obrazek z webu nacteni")

st.image("https://www.vita.sk/wp-content/themes/vita/images/user.png", 
        caption="Toto je muj nacteny obrazek z webu"
)

# Video/Audio z webu nacteni
st.write("# 29. Video/Audio z webu nacteni")

st.video("https://www.youtube.com/watch?v=vVy9Lgpg1m8")

# Rozdeleni obrazovkydo sloupcu
st.write("# 30. Rozdeleni obrazovkydo sloupcu")

# nadefinuju kolik sloupcu
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Sloupec 1")

with col2:
    st.write("Sloupec 2")

with col3:
    st.write("Sloupec 3")


# Rozdeleni obrazovky do tabu
st.write("# 31. Rozdeleni obrazovky do tabu")

# nadefinuju kolik tabu
tab1, tab2, tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"])

with tab1:
    st.write("Obsah pro zalozku 1")

with tab2:
    st.write("Obsah pro zalozku 2")

with tab3:
    st.write("Obsah pro zalozku 3")


# Rozbalovaci blok (expander)
st.write("# 32. Rozbalovaci blok (expander)")

with st.expander("Klikni sem pro vice informaci"):
    st.write("Toto je rozbalena informace")




# Zobrazeni grafu Matplotlib (pyplot)
st.write("# 33. Zobrazeni grafu Matplotlib (pyplot)")

import matplotlib.pyplot as plt
#vytvoreni jednoducheho grafu
fig, ax = plt.subplots()
ax.plot([1,2,3],[1,4,9])

#zobrazeni grafu
st.pyplot(fig)