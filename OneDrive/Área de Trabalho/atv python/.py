def depositar(saldo, valor):
    """Adiciona um valor ao saldo"""
    if valor <= 0:
        raise ValueError("Valor de depósito inválido")
    return saldo + valor


def sacar(saldo, valor):
    """Remove um valor do saldo"""
    if valor <= 0:
        raise ValueError("Valor de saque inválido")
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor


def calcular_taxa_transferencia(valor):
    """Calcula a taxa de 2% sobre o valor"""
    if valor < 0:
        raise ValueError("Valor inválido")
    return valor * 0.02


def transferir(saldo_origem, saldo_destino, valor):
    """Transfere um valor entre contas com taxa"""
    if valor <= 0:
        raise ValueError("Valor inválido")

    taxa = calcular_taxa_transferencia(valor)
    total = valor + taxa

    if total > saldo_origem:
        raise ValueError("Saldo insuficiente")

    saldo_origem -= total
    saldo_destino += valor

    return saldo_origem, saldo_destino