#!/usr/bin/env python 

import qiskit as q
from qiskit.providers.ibmq import IBMQ
import time

class BackendSummary:
    def __init__(self, backend) -> None:
        self.backend = backend
        self.name = backend.name()
        status = backend.status()
        self.active = status.operational and status.status_msg == 'active'
        self.pending_jobs = status.pending_jobs
        config = backend.configuration()
        self.simulator = config.simulator
        self.n_qubits = config.n_qubits

    def __str__(self) -> str:
        return f"{self.name} {'- simulator' if self.simulator else ''}- en attente: {self.pending_jobs} - nb qubits: {self.n_qubits}"


def main():
    start = time.time_ns()

    provider = IBMQ.load_account()

    end = time.time_ns()
    print(f"load account { (end - start)  / 1_000_000 }")
    start = end

    # provider = IBMQ.get_provider(group='open')

    # end = time.time_ns()
    # print(f"get_provider { (end - start)  / 1_000_000 }")
    # start = end

    raw_backends = provider.backends()

    end = time.time_ns()
    print(f"get_backends { (end - start)  / 1_000_000 }")
    start = end

    lima = provider.get_backend("ibmq_lima")

    end = time.time_ns()
    print(f"get_backend(lima) { (end - start)  / 1_000_000 }")
    start = end

    backends = [ BackendSummary(backend) for backend in raw_backends ]

    end = time.time_ns()
    print(f"summarize_backends { (end - start)  / 1_000_000 }")
    start = end

    for backend in backends:
        print(backend)

    end = time.time_ns()
    print(f"display { (end - start)  / 1_000_000 }")

main()