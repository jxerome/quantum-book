#!/usr/bin/env -S streamlit run 

import qiskit as q
import PIL
import matplotlib.pyplot as plt
import streamlit as st
import random
import math
import numpy as np

def main():
    st.set_page_config(page_title='Quantum circuit page 35', page_icon=":atom_symbol:")
    st.title("Quantum circuit page 35")

    simulator = q.Aer.get_backend('statevector_simulator')

    psy1 = random_vector()
    psy2 = random_vector()

    st.header("État initial")
    st.code(f"psy1 = {psy1}\npsy2 = {psy2}")

    circuit1 = create_circuit1(psy1, psy2)
    circuit2 = create_circuit2(psy1, psy2)

    st.header("Schéma du circuit 1")
    st.write(circuit1.draw(output='mpl'))
    st.header("Schéma du circuit 2")
    st.write(circuit2.draw(output='mpl'))

    res1 = executer(circuit1, simulator)
    res2 = executer(circuit2, simulator)

    st.header("Résultats")
    st.code(f"res1 = {res1}\nres2 = {res2}")

    delta = np.linalg.norm(res1 - res2)
    st.metric("Différence entre les résultats", f"{delta:.3e}")
    if delta < 1e-15:
        st.success("Les résultats sont les mêmes.")
    else:
        st.error("Les résultats sont différents.")

def random_coef():
    return complex(random.random(), random.random())

def random_vector():
    alpha0 = random_coef()
    beta0 = random_coef()
    norm = math.sqrt(alpha0.real ** 2 + alpha0.imag ** 2 + beta0.real ** 2 + beta0.imag ** 2)
    return [ alpha0/norm, beta0/norm ]

def create_circuit1(psy1, psy2):
    circuit = q.QuantumCircuit(2)
    circuit.initialize(psy1, [0])
    circuit.initialize(psy2, [1])
    circuit.h(0)
    circuit.h(1)
    circuit.cx(0, 1)
    circuit.h(0)
    circuit.h(1)
    return circuit

def create_circuit2(psy1, psy2):
    circuit = q.QuantumCircuit(2)
    circuit.initialize(psy1, [0])
    circuit.initialize(psy2, [1])
    circuit.cx(1, 0)
    return circuit

def executer(circuit, simulator):
    job = q.execute(circuit, simulator)
    resultat = job.result()
    return resultat.get_statevector()
 
main()
