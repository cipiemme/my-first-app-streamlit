import streamlit as st

# 1. Configurazione della pagina e stili personalizzati (Colori e Stili)
st.set_page_config(page_title="Ironman Feedback", page_icon="🏅", layout="centered")

# Aggiungiamo un po' di CSS personalizzato per il tema Ironman
st.markdown("""
    <style>
    /* Cambia il colore del titolo principale in rosso stile Ironman */
    h1 {
        color: #cc0000;
        text-align: center;
        font-family: 'Impact', sans-serif;
    }
    /* Stile per il pulsante di submit */
    .stButton>button {
        background-color: #cc0000;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff0000;
        color: white;
    }
    /* Sfondo leggero per evidenziare il form */
    div[data-testid="stForm"] {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Intestazione
st.title("🏊🚴🏃 IRONMAN FEEDBACK")
st.markdown("Hai superato i tuoi limiti. Ora dicci come è andata l'organizzazione della gara!")

# 2. Creazione del Form
with st.form(key='ironman_feedback_form'):
    st.subheader("Raccontaci la tua esperienza")
    
    # Input utente
    name = st.text_input("Nome dell'Atleta (obbligatorio)", placeholder="Es. Jan Frodeno")
    
    # Slider per la soddisfazione (1 a 5)
    rating = st.slider("Valutazione complessiva dell'evento", min_value=1, max_value=5, value=3)
    
    # Area di testo per i commenti
    comments = st.text_area("Commenti (percorso, ristori, transizioni...)", placeholder="Il percorso in bici era fantastico, ma l'acqua era troppo fredda...")
    
    # Pulsante di invio
    submit_button = st.form_submit_button(label="Invia Feedback")

# 3. Gestione del submit e delle eccezioni/validazioni
if submit_button:
    # Gestione delle eccezioni: controlliamo che il nome non sia vuoto
    if not name.strip():
        st.error("⚠️ Attenzione: Il nome dell'atleta è obbligatorio. Per favore, compila il campo e riprova.")
    else:
        # 4. Mostra i dati inseriti dopo l'invio
        st.markdown("---")
        st.write("### Riepilogo Feedback Ricevuto")
        st.write(f"**Atleta:** {name}")
        st.write(f"**Valutazione:** {rating} / 5")
        
        # Gestiamo il caso in cui il commento sia stato lasciato vuoto
        if comments.strip():
            st.write(f"**Commenti:** {comments}")
        else:
            st.write("**Commenti:** *Nessun commento aggiuntivo fornito.*")
        
        # 5. Messaggi condizionali basati sul rating
        st.markdown("---")
        if rating <= 2:
            st.warning("Ci dispiace che la tua esperienza non sia stata all'altezza delle aspettative. Analizzeremo i tuoi commenti per migliorare le prossime edizioni. 😔")
        elif rating >= 4:
            st.success(f"Fantastico {name}! Siamo felicissimi che l'evento ti sia piaciuto. YOU ARE AN IRONMAN! 🏅")
        else:
            st.info("Grazie per il tuo feedback! Lavoreremo sodo per rendere la prossima gara ancora migliore.")
