#!/usr/bin/env python

from qiskit_ibm_provider import IBMProvider
from getpass import getpass

jeton = getpass("Indiquez votre jeton d'API IBM: ")
IBMProvider.save_account(jeton)
