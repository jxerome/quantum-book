import qiskit as q
import numpy as np

simulator = q.Aer.get_backend('statevector_simulator')

def main():
    baba_y()
    etat_init = etat_initial()
    print(f"état initial   = [{etat_init[0]:.6f}; {etat_init[1]:.6f}]")
    resultat_h = executer(circuit_h())
    print(f"resultat H     = [{resultat_h[0]:.6f}; {resultat_h[1]:.6f}]")
    resultat_hx = executer(circuit_hx())
    print(f"resultat H X   = [{resultat_hx[0]:.6f}; {resultat_hx[1]:.6f}]")
    resultat_hxy = executer(circuit_hxy())
    print(f"resultat H X Y = [{resultat_hxy[0]:.6f}; {resultat_hxy[1]:.6f}]")


def etat_initial():
    return [np.sqrt(3)/2, (1 - 1j)/(2*np.sqrt(2))]

def nouveau_circuit():
    circuit = q.QuantumCircuit(1)
    circuit.append(q.extensions.Initialize(etat_initial()), [0])
    return circuit

def circuit_h():
    circuit = nouveau_circuit()
    circuit.h(0)
    return circuit

def circuit_hx():
    circuit = nouveau_circuit()
    circuit.h(0)
    circuit.x(0)
    return circuit

def circuit_hxy():
    circuit = nouveau_circuit()
    circuit.h(0)
    circuit.x(0)
    circuit.y(0)
    return circuit

def baba_y():
    circuit1 = q.QuantumCircuit(1)
    circuit1.append(q.extensions.Initialize([1, 0]), [0])
    circuit1.y(0)
    r0 = executer(circuit1)

    circuit2 = q.QuantumCircuit(1)
    circuit2.append(q.extensions.Initialize([0, 1]), [0])
    circuit2.y(0)
    r1 = executer(circuit2)

    print(f'Y(|0>) = [{r0[0]:.6f}; {r0[1]:.6f}')
    print(f'Y(|1>) = [{r1[0]:.6f}; {r1[1]:.6f}')


def executer(circuit):
    job = q.execute(circuit, simulator)
    resultat = job.result()
    return resultat.get_statevector()
    
if __name__ == '__main__':
    main()

