# Quiz de Programação Python

Um quiz interativo em web desenvolvido com Flask para testar conhecimentos sobre Python. O aplicativo apresenta perguntas sobre conceitos fundamentais de Python e fornece feedback imediato com explicações detalhadas.

## 🎯 Características

- ✅ Interface intuitiva e responsiva
- ✅ Perguntas sobre conceitos fundamentais de Python
- ✅ Feedback imediato com explicações
- ✅ Relatório de resultados final
- ✅ Sistema de pontuação
- ✅ API backend em Flask

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## 🚀 Instalação

1. **Clone ou baixe o projeto:**

   ```bash
   cd Quiz-de-Programacao-Python
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Como Usar

1. **Inicie a aplicação:**

   ```bash
   python app.py
   ```

2. **Acesse no navegador:**
   Abra seu navegador e vá para `http://localhost:5000`

3. **Realize o quiz:**
   - Clique em "Começar Quiz" na página inicial
   - Responda todas as perguntas
   - Veja o feedback com a resposta correta e explicação
   - Confira seu resultado final

## 📁 Estrutura do Projeto

```
Quiz-de-Programacao-Python/
├── app.py                 # Aplicação principal (rotas e lógica)
├── questions.py           # Base de dados de perguntas
├── requirements.txt       # Dependências do projeto
├── templates/             # Templates HTML
│   ├── index.html         # Página inicial
│   ├── quiz.html          # Página do quiz
│   └── result.html        # Página de resultados
└── static/
    └── css/
        ├── index.css      # Estilos da página inicial
        ├── quiz.css       # Estilos do quiz
        └── result.css     # Estilos de resultados
```

## 🔧 Tecnologias Utilizadas

- **Backend:** Flask 2.3.2
- **Frontend:** HTML5, CSS3, JavaScript
- **Linguagem:** Python 3

## 📝 Rotas da Aplicação

| Rota            | Método | Descrição                    |
| --------------- | ------ | ---------------------------- |
| `/`             | GET    | Página inicial do quiz       |
| `/quiz`         | GET    | Página com perguntas do quiz |
| `/check-answer` | POST   | API para validar resposta    |
| `/results`      | GET    | Página de resultados final   |

## 🎓 Conteúdo do Quiz

O quiz aborda os seguintes tópicos de Python:

- Operadores aritméticos e exponenciação
- Funções básicas (print, input, len)
- Conversão de tipos (int, str, float)
- Conceitos fundamentais da linguagem

## 🛠️ Desenvolvimento

Para adicionar novas perguntas, edite o arquivo `questions.py`:

```python
{
    "question": "Sua pergunta aqui?",
    "options": ["Opção 1", "Opção 2", "Opção 3"],
    "answer": "Opção correta",
    "explanation": "Explicação da resposta correta"
}
```

## 📄 Licença

Este projeto é de uso livre para fins educacionais.

## 👨‍💻 Autor

Desenvolvido como um projeto educacional para aprendizado de Flask e desenvolvimento web.

---

**Aproveite o quiz e bons estudos! 🐍**
