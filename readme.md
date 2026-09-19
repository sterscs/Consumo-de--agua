# 💧 Consumo de Água

## 📌 Sobre o projeto

O **Consumo de Água** é um programa desenvolvido em **Python** para classificar o perfil de consumo de água de diferentes tipos de imóveis.

O sistema solicita o tipo de imóvel e o consumo mensal de água em metros cúbicos (m³). Com essas informações, apresenta uma mensagem educativa de acordo com as regras de consumo estabelecidas.

O objetivo é incentivar a conscientização sobre o uso responsável da água e ajudar os moradores a identificar situações de consumo elevado.

## 🏠 Tipos de imóveis

O programa trabalha com três tipos de imóveis:

* 🏢 **Comercial**
* 🏠 **Casa**
* 🏘️ **Apartamento**

## 📊 Regras de classificação

| Tipo de imóvel      | Consumo          | Resultado                 |
| ------------------- | ---------------- | ------------------------- |
| Comercial           | Qualquer consumo | Tarifa comercial aplicada |
| Apartamento         | Menor que 10 m³  | Consumo econômico         |
| Apartamento ou casa | Até 25 m³        | Consumo moderado          |
| Outros casos        | Acima do limite  | Consumo excessivo         |

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 💻 GitHub
* 🌱 Conceitos de sustentabilidade
* ⌨️ Terminal/Console

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd consumo-agua
```

### 3. Execute o programa

```bash
python app.py
```

## 💡 Exemplo de execução

```text
======================================
     SISTEMA DE CONSUMO DE ÁGUA 💧
======================================

Digite o tipo de imóvel (comercial, casa ou apartamento): apartamento
Digite o consumo mensal de água em m³: 8

--- Resultado ---

Consumo econômico – excelente controle de água!
```

## 🌱 Objetivo ambiental

O uso consciente da água é importante para a preservação dos recursos naturais. O sistema busca contribuir para essa conscientização por meio de mensagens educativas sobre o consumo.

💧 **Economize água. Evite desperdícios e fique atento a possíveis vazamentos!**
