import streamlit as st

def find_greatest_number(x, y, z):
    return max(x,y,z)

def main():
    st.title("TDS_WK8_22f1000246_Gr8of3")

    # Input for three numbers
    n1 = st.number_input("First number:", value=0)
    n2 = st.number_input("Second number:", value=0)
    n3 = st.number_input("Third number:", value=0)

    # Button to find the greatest number
    if st.button("Find Greatest"):
        ap = find_greatest_number(n1, n2, n3)
        st.success(f"The greatest number is: {ap}")

if __name__ == "__main__":
    main()
