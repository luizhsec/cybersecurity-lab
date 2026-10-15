"""LAB-001 (Python): fictional access decision with Boolean expressions.

Educational simulation only. No real authentication, biometrics or gate.
First version based on the student's tested local exercise on 2026-10-14.
"""

conta_ativa = True
mensalidade_em_dia = False
autorizacao_especial = True

liberar_catraca = conta_ativa and (
    mensalidade_em_dia or autorizacao_especial
)

print(liberar_catraca)
