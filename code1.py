import streamlit as st
import random

GRID_SIZE = 10

# יצירת סיבוב חדש
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

# אתחול
if "grid" not in st.session_state:
    new_round()

st.title("מצא את המספר השונה")

# ציור גריד 10x10
for i in range(GRID_SIZE):
    cols = st.columns(GRID_SIZE)
    for j in range(GRID_SIZE):
        index = i * GRID_SIZE + j
        if cols[j].button(str(st.session_state.grid[index]), key=index):
            if index == st.session_state.diff_index:
                st.success("נכון! סיבוב חדש 🎉")
                new_round()
            else:
                st.error("לא נכון, נסה שוב")

# כפתור ריסט ידני (אופציונלי)
if st.button("התחל מחדש"):
    new_round()
