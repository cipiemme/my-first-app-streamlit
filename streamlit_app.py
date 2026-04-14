import streamlit as st

st.set_page_config(page_title="Ironman Feedback", page_icon="🏅", layout="centered")

st.title("🏊🚴🏃 IRONMAN FEEDBACK")
st.markdown("Hai superato i tuoi limiti. Ora dicci come è andata l'organizzazione della gara!")

with st.form(key='ironman_feedback_form'):
    st.subheader("Raccontaci la tua esperienza")
    name = st.text_input("Nome dell'Atleta (obbligatorio)", placeholder="Es. Jan Frodeno")
    rating = st.slider("Valutazione complessiva dell'evento", min_value=1, max_value=5, value=3)
    comments = st.text_area("Commenti (percorso, ristori, transizioni...)", placeholder="Il percorso in bici era fantastico, ma l'acqua era troppo fredda...")    
    submit_button = st.form_submit_button(label="Invia Feedback")

if submit_button:
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
