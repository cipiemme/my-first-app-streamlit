import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="Iron Man App", page_icon="🤖", layout="centered")

# Titolo
st.title("🦾 Iron Man Dashboard")
st.subheader("Benvenuto nel sistema di Tony Stark")

# Sidebar
st.sidebar.header("Controlli Armatura")
potenza = st.sidebar.slider("Livello Potenza", 0, 100, 75)
modalita = st.sidebar.selectbox("Modalità", ["Attacco", "Difesa", "Stealth"])
attiva = st.sidebar.checkbox("Attiva Armatura")

# Contenuto principale
st.write("### Stato Armatura")

if attiva:
    st.success("Armatura Attiva")
    st.progress(potenza)
    
    if modalita == "Attacco":
        st.error("Modalità Attacco Attiva 🚀")
    elif modalita == "Difesa":
        st.info("Modalità Difesa Attiva 🛡️")
    else:
        st.warning("Modalità Stealth Attiva 🕶️")
else:
    st.warning("Armatura Disattivata")

# Input utente
st.write("### Comandi Vocali (simulati)")
comando = st.text_input("Inserisci comando:")

if comando:
    st.write(f"Jarvis esegue: {comando}")

# Pulsante
if st.button("Avvia Sequenza di Volo"):
    st.success("🚀 Decollo avviato!")

# Footer
st.write("---")
st.caption("Creato da Tony Stark Industries")
