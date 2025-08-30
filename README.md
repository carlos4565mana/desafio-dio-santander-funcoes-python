# 🏦 Sistema Bancário com Funções - Versão Otimizada

Evolução do sistema bancário simples, agora implementado com **funções modulares** e **recursos** de cadastro de usuários e contas.

## 🎯 Objetivo do Projeto

Refatorar o sistema bancário original aplicando conceitos de **programação funcional** e **modularização**, implementando:

- ✅ Funções de **saque**, **depósito** e **extrato**
- ✅ Sistema de **cadastro de usuários**
- ✅ Criação de **contas bancárias** vinculadas
- ✅ **Listagem** de usuários e contas
- ✅ **Validações** e regras de negócio aprimoradas



## 🔧 Funcionalidades Implementadas

### 💸 Operações Bancárias

#### **Saque**

- **Argumentos**: Apenas por palavra-chave (`keyword-only`)
- **Parâmetros**: `saldo`, `valor`, `extrato`, `numero_saques`, `limite_saques`, `limite_valor`
- **Validações**: Limite diário, valor máximo, saldo suficiente
- **Retorno**: `saldo` e `extrato` atualizados

#### **Depósito**

- **Argumentos**: Apenas por posição (`positional-only`)
- **Parâmetros**: `saldo`, `valor`, `extrato`
- **Validações**: Valor positivo
- **Retorno**: `saldo` e `extrato` atualizados

#### **Extrato**

- **Argumentos**: Mistos (posicionais e nomeados)
- **Posicionais**: `saldo`
- **Nomeados**: `extrato`
- **Funcionalidade**: Exibe histórico formatado

### 👥 Gestão de Usuários

#### **Cadastro de Usuários**

```python
usuario = {
    "nome": "Jose Silva",
    "data_nascimento": "15/03/1990", 
    "cpf": "1234567890",
    "endereco": "Rua A - Centro - Salvador/BA"
}
```

**Regras:**

- ✅ CPF único (não permite duplicatas)

- ✅ Endereço completo em string única

  

#### **Listagem de Usuários**

- Exibe todos os usuários cadastrados
- Formato organizado e legível
- Verificação de lista vazia

### 🏛️ Gestão de Contas

#### **Criação de Contas**

```python
conta = {
    "agencia": "0001",
    "numero_conta": 1,  # Sequencial
    "usuario": usuario  # Referência ao usuário
}
```

**Regras:**

- ✅ Agência fixa: **"0001"**
- ✅ Numeração sequencial: 1, 2, 3...
- ✅ Vinculação obrigatória com usuário existente
- ✅ Um usuário pode ter múltiplas contas
- ✅ Uma conta pertence a apenas um usuário

#### **Listagem de Contas**

- Exibe agência, número e titular
- Formatação clara e organizada
- Verificação de contas existentes

### 

### **Separação de Responsabilidades**

- **Funções puras** sem efeitos colaterais
- **Validações** centralizadas
- **Reutilização** de código

### **2. Menu Principal**

```
========== BANCO TABAJARA ==========

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova conta
[6] Listar contas
[7] Listar usuários
[0] Sair
```

## 🎯 Conceitos Aplicados

### **Estruturas de Dados**

- **Listas**: Armazenamento de usuários e contas
- **Dicionários**: Estruturação de dados complexos
- **Strings**: Formatação e validação de dados

### **Programação Funcional**

- **Funções puras**: Sem efeitos colaterais
- **Immutabilidade**: Dados não alterados diretamente
- **Composição**: Funções que trabalham em conjunto





---

**📚 Curso:** Santander Back-End Python  
**🎯 Módulo:** 03 - Trabalhando com Funções  
**👨‍💻 Desenvolvido por:** Carlos Santos

🔄 Versão:** 2.0 - Sistema Otimizado com Funções
