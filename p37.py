#!/usr/bin/env -S streamlit run

import qiskit as q
from qiskit_ibm_provider import IBMProvider
from qiskit.tools.monitor import job_monitor
import PIL
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pyarrow as pa


class BackendSummary:
    def __init__(self, backend) -> None:
        self.backend = backend
        self.name = backend.name
        status = backend.status()
        self.active = status.operational and status.status_msg == 'active'
        self.pending_jobs = status.pending_jobs
        config = backend.configuration()
        self.simulator = config.simulator
        self.n_qubits = config.n_qubits

    def __str__(self) -> str:
        return f"{self.name} {'- simulator' if self.simulator else ''}- en attente: {self.pending_jobs} - nb qubits: {self.n_qubits}"


def main():
    st.set_page_config(page_title='Quantum circuit page 37', page_icon=":atom_symbol:")
    st.title("Quantum circuit page 37")

    provider = ibmq_provider()

    st.header("Backends")
    backends = load_backends(provider)
    st.table(backends)

def ibmq_provider():
    if 'ibmq_provider' not in st.session_state:
        with st.spinner('Connection to IBM Quantum provider'):
            st.session_state['ibmq_provider'] = IBMProvider()
    return st.session_state['ibmq_provider']



@st.cache
def load_backends(provider):
    backends=[]
    barContainer = st.empty()
    progressBar = barContainer.progress(0)
    backendList=provider.backends()
    count=len(backendList)
    for i,backend in enumerate(backendList, start=1):
        backends.append(BackendSummary(backend))
        progressBar.progress(i/count)
    progressBar.progress(100)
    barContainer.empty()
    return backends
    
main()