#!/usr/bin/env python

import qiskit as q
import PIL
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title='Quantum circuit page 33', page_icon=":atom_symbol:")
st.title("Quantum circuit page 33")

simulator = q.Aer.get_backend('qasm_simulator')

# Création du circuit
circuit = q.QuantumCircuit(2, 2)
circuit.h(0)
circuit.x(1)
circuit.cx(0, 1)
circuit.h(1)
circuit.measure([0, 1], [0, 1])

# Dessin du circuit
st.header("Schéma du circuit")
st.write(circuit.draw(output='mpl'))
#circuit.draw().dump("circuit_33.txt")

# Exécution
job = q.execute(circuit, simulator, shots = 1000)

# Résultats
result = job.result()
counts = result.get_counts(circuit)
st.write("Résultats:", counts)

# Graph
st.pyplot(q.visualization.plot_histogram(counts))


