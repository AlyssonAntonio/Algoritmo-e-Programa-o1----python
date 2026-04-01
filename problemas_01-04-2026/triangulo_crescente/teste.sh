#!/bin/bash

# =========================
# CORES
# =========================
VERDE='\033[0;32m'
VERMELHO='\033[0;31m'
AMARELO='\033[1;33m'
AZUL='\033[0;34m'
NC='\033[0m' # Sem cor

# =========================
# VALIDAÇÃO DE ENTRADA
# =========================
if [ $# -ne 1 ]; then
    echo -e "${AMARELO}Uso: ./testar.sh script.py${NC}"
    exit 1
fi

SCRIPT=$1

if [ ! -f "$SCRIPT" ]; then
    echo -e "${VERMELHO}Erro: arquivo $SCRIPT não encontrado.${NC}"
    exit 1
fi

# =========================
# CONTADORES
# =========================
TOTAL=6
PASSOU=0

# =========================
# LOOP DE TESTES
# =========================
for i in {1..6}; do
    ENTRADA="entrada$i.txt"
    ESPERADA="esperada$i.txt"
    SAIDA="saida$i.txt"

    echo -e "\n${AZUL}------------------------------${NC}"
    echo -e "${AZUL}Caso de teste $i${NC}"
    echo -e "${AZUL}------------------------------${NC}"

    if [ ! -f "$ENTRADA" ] || [ ! -f "$ESPERADA" ]; then
        echo -e "${AMARELO}Arquivos do caso $i não encontrados.${NC}"
        continue
    fi

    # Executa o programa
    python3 "$SCRIPT" < "$ENTRADA" > "$SAIDA"

    # Compara ignorando espaços no final
    if diff -q -Z "$ESPERADA" "$SAIDA" > /dev/null; then
        echo -e "${VERDE}✔ Passou no caso de teste $i.${NC}"
        PASSOU=$((PASSOU+1))
    else
        echo -e "${VERMELHO}✘ FALHOU no caso de teste $i.${NC}"

        #echo -e "\n${AMARELO}Diferenças:${NC}"
        #diff -u "$ESPERADA" "$SAIDA"

        echo -e "\n${AMARELO}Entrada utilizada:${NC}"
        cat "$ENTRADA"

        echo -e "\n${AMARELO}Saída esperada:${NC}"
        cat "$ESPERADA"

        echo -e "\n${AMARELO}Saída obtida:${NC}"
        cat "$SAIDA"
    fi
done

# =========================
# RESUMO FINAL
# =========================
echo -e "\n${AZUL}======================================${NC}"
echo -e "${AZUL}            RESULTADO FINAL${NC}"
echo -e "${AZUL}======================================${NC}"

if [ $PASSOU -eq $TOTAL ]; then
    echo -e "${VERDE}Passou em todos os testes! (${PASSOU}/${TOTAL})${NC}"
else
    echo -e "${VERMELHO}Passou em ${PASSOU} de ${TOTAL} testes.${NC}"
fi

echo -e "${AZUL}======================================${NC}"
