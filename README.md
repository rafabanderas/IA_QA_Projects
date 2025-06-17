Perfeito, Rafael! Aqui está seu `README.md` atualizado, **completo**, incluindo como executar tanto a **API** quanto os **testes automatizados**:

---

# 🧠 IA QA Projects | Rafael Bandeira

> Projetos de **Inteligência Artificial aplicada à Qualidade de Software (QA)**.

![GitHub repo size](https://img.shields.io/github/repo-size/rafabanderas/IA_QA_Projects)
![GitHub last commit](https://img.shields.io/github/last-commit/rafabanderas/IA_QA_Projects)
![GitHub](https://img.shields.io/github/license/rafabanderas/IA_QA_Projects)
![GitHub language count](https://img.shields.io/github/languages/count/rafabanderas/IA_QA_Projects)
![GitHub top language](https://img.shields.io/github/languages/top/rafabanderas/IA_QA_Projects)

---

## 🚀 Sobre o Projeto

Este projeto tem como objetivo aplicar IA no ciclo de testes de software, trazendo automação inteligente para geração de casos de teste, dados sintéticos e automação de QA.

---

## 🗂️ Estrutura do Projeto

```plaintext
/IA_QA_Projects
├── src/                     # Código principal
│   └── api/                 # API com FastAPI
│   └── gerador_casos_teste/ # Funções para gerar casos de teste
├── tests/                   # Testes automatizados
├── notebooks/               # Protótipos e experimentos com Jupyter
├── docs/                    # Documentação técnica
├── data/                    # Dados de entrada e saída
├── requirements.txt         # Dependências
├── pytest.ini               # Configuração do Pytest
├── README.md                # Este arquivo
├── LICENSE                  # Licença
└── .gitignore               # Arquivos ignorados pelo Git
```

---

## 💻 Tecnologias Utilizadas

* Python 3.13
* Pytest
* FastAPI
* Uvicorn
* Pandas
* Requests
* OpenAI API
* Git & GitHub
* PyCharm (ou VSCode)

---

## 🔧 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/rafabanderas/IA_QA_Projects.git
```

2. Acesse o diretório:

```bash
cd IA_QA_Projects
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Ative no Windows:
.venv\Scripts\activate
# Ou no Mac/Linux:
source .venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como executar a API

1. Navegue até o diretório `src`:

```bash
cd src
```

2. Execute o servidor com Uvicorn:

```bash
uvicorn api.main:app --reload
```

3. Acesse a documentação interativa (Swagger):

* 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

4. Teste o endpoint:

* `GET /gerar-casos?cenario=Login`

---

## ✅ Como executar os testes

Execute os testes automatizados com Pytest:

1. No diretório raiz do projeto, execute:

```bash
pytest
```

2. Saída esperada:

* Todos os testes executados e passando ✔️

---

## 🧠 Contribuindo

Sinta-se à vontade para abrir issues, sugerir melhorias ou contribuir diretamente via pull requests.

---

## 📝 Licença

Este projeto está sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---




