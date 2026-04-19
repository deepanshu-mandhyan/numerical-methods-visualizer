import streamlit as st
import matplotlib.pyplot as plt
from src.methods import bisection, newton
from src.utils import create_function

st.set_page_config(page_title="Numerical Visualizer", layout="wide")

st.title("🔥 Numerical Methods Convergence Visualizer")

# Sidebar UI
st.sidebar.header("⚙️ Controls")

equation = st.sidebar.text_input("Enter function f(x):", "x**3 - x - 2")
x0 = st.sidebar.number_input("Initial Guess (Newton):", value=1.5)
a = st.sidebar.number_input("Interval Start (Bisection):", value=1.0)
b = st.sidebar.number_input("Interval End (Bisection):", value=2.0)
tol = st.sidebar.slider("Tolerance", 1e-6, 1e-2, 1e-5)

# Convert equation to function
f, df = create_function(equation)

if st.button("🚀 Run Simulation"):

    root_b, err_b, it_b = bisection(f, a, b, tol)
    root_n, err_n, it_n = newton(f, df, x0, tol)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Results")

        if root_b:
            st.success(f"Bisection Root: {round(root_b, 5)}")
            st.write(f"Iterations: {it_b}")
        else:
            st.error("Invalid Bisection Interval")

        if root_n:
            st.success(f"Newton Root: {round(root_n, 5)}")
            st.write(f"Iterations: {it_n}")
        else:
            st.error("Newton Failed")

    with col2:
        st.subheader("📈 Convergence Graph")

        fig, ax = plt.subplots()

        if err_b:
            ax.plot(err_b, label="Bisection")
        if err_n:
            ax.plot(err_n, label="Newton")

        ax.set_yscale('log')
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Error")
        ax.set_title("Convergence Comparison")
        ax.legend()
        ax.grid()

        st.pyplot(fig)
