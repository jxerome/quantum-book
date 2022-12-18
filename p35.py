#!/usr/bin/env streamlit run 

import qiskit as q
import PIL
import matplotlib.pyplot as plt
import streamlit as st
import random
import math

def main():
    st.set_page_config(page_title='Quantum circuit page 35', page_icon=":atom_symbol:")
    st.title("Quantum circuit page 35")

    simulator = q.Aer.get_backend('statevector_simulator')

    psy1 = random_vector()
    psy2 = random_vector()

    st.header("État initial")
    st.write(f"psy1 = {psy1}")
    st.write(f"psy2 = {psy2}")

    circuit1 = create_circuit1(psy1, psy2)
    circuit2 = create_circuit2(psy1, psy2)

    st.header("Schéma du circuit 1")
    st.write(circuit1.draw(output='mpl'))
    st.header("Schéma du circuit 2")
    st.write(circuit2.draw(output='mpl'))



def random_coef():
    return complex(random.random(), random.random())

def random_vector():
    alpha0 = random_coef()
    beta0 = random_coef()
    norm = math.sqrt(alpha0.real ** 2 + alpha0.imag ** 2 + beta0.real ** 2 + beta0.imag ** 2)
    return [ alpha0/norm, beta0/norm ]

def create_circuit1(psy1, psy2):
    circuit = q.QuantumCircuit(2)
    circuit.append(q.extensions.Initialize([psy1, psy2], num_qubits=2), [0, 1])
    circuit.h(0)
    circuit.h(1)
    circuit.cx(0, 1)
    circuit.h(0)
    circuit.h(1)
    return circuit

def create_circuit2(psy1, psy2):
    circuit = q.QuantumCircuit(2)
    circuit.append(q.extensions.Initialize([psy1, psy2]), [0, 1])
    circuit.cx(1, 0)
    return circuit
    
main()
