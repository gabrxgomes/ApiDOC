from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API de Validação de Documentos",
    description="API para validar documentos brasileiros.",
    version="1.0.0"
)

def validar_cpf(cpf: str) -> bool:
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * len(cpf):
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    # Verificar se os dígitos verificadores são iguais aos informados
    return cpf[-2:] == f"{digito1}{digito2}" #aqui ja é a confirmação do meu true




@app.get("/validar/cpf/{cpf}", summary="Validar CPF", description="Valida se o CPF informado é válido ou não.")
def validar_cpf_endpoint(cpf: str):
    """
    Valida um número de CPF.

    - **cpf**: Número do CPF a ser validado.
    """
    if validar_cpf(cpf):
        return {"cpf": cpf, "valido": True}
    else:
        raise HTTPException(status_code=400, detail="CPF inválido")


def validar_cnpj(cnpj: str) -> bool:
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verificar se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False
    
    # Verificar se todos os dígitos são iguais
    if cnpj == cnpj[0] * len(cnpj):
        return False
        # Cálculo do primeiro dígito verificador
    soma = sum(int(cnpj[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cnpj[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10
    # Verificar se os dígitos verificadores são iguais aos informados
    return cnpj[-2:] == f"{digito1}{digito2}" #aqui ja é a confirmação do meu true


@app.get("/validar/cnpj/{cnpj}", summary="Validar CNPJ", description="Valida se o CNPJ informado é válido ou não.")
def validar_cnpj_endpoint(cnpj: str):

    """
    Valida um número de CNPJ.

    - **cnpj**: Número do CNPJ a ser validado.
    """
    if validar_cnpj(cnpj):
        return {"cnpj": cnpj, "valido": True}
    else:
        raise HTTPException(status_code=400, detail="CNPJ inválido")