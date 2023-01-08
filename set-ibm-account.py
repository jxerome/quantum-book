#!/usr/bin/env python

import qiskit as q
from getpass import getpass

jeton = getpass("Indiquez votre jeton d'API IBM: ")
q.IBMQ.save_account(jeton)
