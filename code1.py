import streamlit as st
import random

GRID_SIZE = 10

def new_round():
    common = random.randint(10, 99)

    different = common
    while different == common:
        different = random.randint(10, 99)

    diff_index = random.randint(0, GRID_SIZE * GRID_SIZE - 1)

    grid = [common] * (GRID_SIZE * GRID_SIZE)
    grid[diff_index] = different

    st.session_state.grid = grid
    st.session_state.diff_index = diff_index
    st.session_state.common = common
    st.session_state.different = different


# --- אתחול ---
if "grid" not in st.session_state:
    new_round()

if "prev_common" not in st.session_state:
    st.session_state.prev_common = None
    st.session_state.prev_diff = None

if "message" not in st.session_state:
    st.session_state.message = None


st.title("מצא את המספר השונה")

# --- הצגת הודעה (אם קיימת) ---
if st.session_state.message:
    st.success(st.session_state.message)
    st.session_state.message = None  # כדי שלא תישאר לנצח

# --- שורה ראשונה ---
if st.session_state.prev_common is not None:
    st.markdown(
        f"חריג קודם: {st.session_state.prev_diff} | רגיל קודם: {st.session_state.prev_common}"
    )
else:
    st.markdown("אין נתונים קודמים עדיין")

st.divider()

# --- הגריד ---
for i in range(GRID_SIZE):
    cols = st.columns(GRID_SIZE)
    for j in range(GRID_SIZE):
        index = i * GRID_SIZE + j
        if cols[j].button(str(st.session_state.grid[index]), key=index):

            if index == st.session_state.diff_index:

                # שמירת סיבוב קודם
                st.session_state.prev_common = st.session_state.common
                st.session_state.prev_diff = st.session_state.different

                # שמירת הודעה
                st.session_state.message = "נכון! סיבוב חדש 🎉"

                new_round()
                st.rerun()

            else:
                st.error("לא נכון, נסה שוב")

# ריסט
if st.button("התחל מחדש"):
    new_round()
    st.rerun()
