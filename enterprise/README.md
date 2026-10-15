# Enterprise Scenario — Phase 0

## Purpose
This is a **fictional, local-only educational scenario** for the LuizSec Enterprise Security Lab. No real organization, network, identity provider, or physical access device is represented.

## Simulated organization
A small company with 10 workstations, employees, administrative accounts and customer data. This scenario builds on the risk assessment in `fundamentals/README.md`.

## Phase 0 security questions
- Which assets should be protected?
- What threats, vulnerabilities and impacts exist?
- When should a simulated access decision return True or False?
- What assumptions and limitations belong in the report?

## First practical exercise
`python/lab001_acesso.py` models a fictional gym access rule, **not** an authentication service. Access is allowed when the account is active and either payment is current or an exception is approved.

This teaches Boolean expressions and test scenarios; it does **not** verify identities, operate gates, store data, manage users or audit decisions.

## Next milestones (not implemented)
1. Explain the decisions and add more test scenarios using current programming knowledge.
2. Learn conditional statements, functions and tests as covered by coursework.
3. Model employee roles and least privilege.
4. Study network concepts and, later, build an isolated virtual network.
5. Progress toward logging, monitoring and defensive investigation.

## Evidence standards
Mark work as **completed** only after running and checking it. Separate simulations from deployed systems. Never commit credentials, personal data or real customer information.
