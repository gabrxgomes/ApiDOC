# API de Validação de DOCUMENTOS
Esta é uma API desenvolvida em Python utilizando o FastAPI para validar números de CPF brasileiros. A API expõe um endpoint que recebe um CPF e retorna se é válido ou não.

## **Como Executar o Projeto**
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
venv\Scripts\Activate.ps1
uvicorn main:app --reload

### **Pré-requisitos**

- Python 3.6 ou superior instalado.
- Pip instalado.

### **Passos para Execução**

1. **Clone o repositório ou copie os arquivos do projeto.**

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
