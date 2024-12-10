# Ana Lúcia Paulo Almeida Pereira 

# UFCD 10790 - Projeto de Programação

# Sistema de Registo de Livros e Autores (Biblioteca - Jardim de Folhas Soltas )

Uma aplicação simples desenvolvida em Python para gerir uma biblioteca de livros, permite adicionar, visualizar, atualizar e remover registos de livros e emprestar a utilizadores registados no sistema e a anónimos.

## Índice

- [Introdução](#introdução)
- [Âmbito do Projeto](#âmbito-do-projeto)
- [Levantamento de Requisitos](#levantamento-de-requisitos)
- [Elaboração do Projeto](#elaboração-do-projeto)
- [Desempenho do Projeto](#desempenho-do-projeto)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Resultados](#resultados)
- [Conclusão](#conclusão)
- [Trabalhos Futuros](#trabalhos-futuros)

## Introdução

O sistema de Registo de Livros e Autores foi projetado para organizar e gerir uma biblioteca pessoal de forma eficiente. O projeto inclui funcionalidades básocas e avançadas, como registo de livros, autores, pesquisa de livros, empréstimos e devoluções.
O objetivo principal é fornecer uma aplicação simples e intuitiva, mas robista, que facilite o controlo e organização da coleção de livros de um utilizador.

## Âmbito do Projeto

- **Objetivo**: Desenvolver uma aplicação para registar e gerir  livros e autores, acompanhando o estado de leitura, permitindo e contolando empréstimos a utilizadores.

- **Objetivos Específicos**:

  - Implementar funcionalidades CRUD (Adicionar, Ler, Atualizar, Eliminar. Emprestar, Devolver e remover registos de livros).
  - Utilizar uma interface de linha de comandos para interagir com o utilizador.
  - Armazenar informações como título, autor, género, estado de leitura, ano de publicação, etc.
  - Implementar um sistema de pesquisa para encontrar livros com base em diferentes critérios.
  - Utilizar uma base de dados simples para armazenamento de livros.
  - Implementar um sistema de empréstimos e devoluções de livros.
  - Garantir a segurança dos dados e a privacidade dos utilizadores.
  - Controlar o estado de leitura dos livros (Lido, a ler, não lido, Emprestado, etc.).

- **Público-Alvo**: 
  - Pessoas interessadas em organizar e gerir uma biblioteca pessoal.
  - Pessoas que desejam manter um registo organizado de seus livros.
  - Programadores ou Estudantesinteressados em estudar ou contribuir para o desenvolvimento e manutenção do projeto.

- ## **Limitações**:

  - A aplicação não inclui recursos de pesquisa avançada, como pesquisa por autor ou género.
  - O projeto atual é desenvolvido em Python com Django e utiliza uma base de dados SQLite para armazenamento de dados, o que pode limitar a escalabilidade e a capacidade de processamento.
  - As interfaces de utilizador estão implementadas como uma aplicação web simples, sem design avançado, o que pode limitar a experiência do utilizador.


## Levantamento de Requisitos

### Requisitos Funcionais

- **RF01**: Permitir adicionar registo de livros com informações como título, autor, ISBN, categoria, ano de publicação, etc.
- **RF02**: Manter registo de empréstimos e devoluções de livros.
- **RF03**: Possibilitar a edição e remoção de livros do sistema já existentes.
- **RF05**: Controlar o estado de leitura dos livros (Lido, a ler, não lido, Emprestado, etc.).
- **RF06**: Permitir aos utilizadores registados emprestar livros a outros utilizadores.
- **RF07**: Permitir aos utilizadores registados devolver livros emprestados.
- **RF08**: Permitir aos utilizadores registados visualizar a lista de livros emprestados.
- **RF09**: Permitir adicionar funcionalidades de autenticação e autorização para proteger os dados dos utilizadores.
- **RF10**: Adicionar suporte para imagens de capa para livros.


### Requisitos Não Funcionais

- **RNF01**: O sistema deve ser executado em Python 3.10.
- **RNF02**: O sistema deve ser desenvolvido utilizando Django.
- **RNF03**: O sistema deve utilizar uma base de dados SQLite para armazenamento de dados.
- **RNF04**: O sistema deve ser seguro e proteger os dados dos utilizadores.
- **RNF05**: O sistema deve ser compatível com sistemas operativos Windows, Linux e MacOS.
- **RNF06**: Interface de linha de comandos para interagir com o utilizador, ter uma interface web responsiva e acessível.

## Desenvolvimento do Projeto

### Arquitetura

A aplicação é baseada na arquitetura de software MVC (Model-View-Controller), típica de frameworks web como Django.
- **Model**: Define as tabelas do banco de dados e as operações de CRUD, incluindo a criação de tabelas, inserção de dados, leitura, atualização e exclusão.
- **View**: Implementa as páginas e os endpoints do Django para exibir informações e receber interações do utilizador.
- **Controller**: Liga o front-end com o back-end, processando as solicitações do utilizador e manipulando as respostas, isto é, a lógica da aplicação.
- **Front-End**: Interface de linha de comandos que permite interagir com o utilizador.

### Tecnologias Utilizadas

- **Linguagens**: Python 3.10: Linguagem de programação.

- **Bibliotecas e Frameworks**:
  - Django: Framework web para Python.
  - Pillow: Biblioteca para manipulação de imagens.
  - SQLite: Sistema de gestão de bases de dados.
  - Bootstrap: Framework CSS para estilização do front-end.
  - HTML, CSS, JavaScript: Linguagens de marcação e estilo.

- **Ferramentas**:
  - GitHub: Plataforma de hospedagem de código, colaboração e controle de versão.
  - Visual Studio Code: Ambiente de desenvolvimento integrado (IDE) para Python.

### Implementação

- Documentar ficheiros do projeto com os comentários para perceber as funcionalidades

## Desempenho do Projeto

### Testes Realizados

- **Testes funcionais**: 
  - Testes de unidade para verificar a correção de funções individuais.
  - Adicionar, visualizar, editar e remover livros.
  - Validar a integração dos dados.
  - Testar a funcionalidade de avaliação das devoluções.


- **Testes de Integração**:
  - Testes de integração para garantir que as diferentes partes do sistema (ex.:banco de dados, interface) interagem corretamente.
  - Testar a integração entre o front-end e o back-end, incluindo a validação de formulários e a exibição de dados.
  - Testar a integração entre o sistema de empréstimos e devoluções.
  - Testar as funcionalidades de autenticação e autorização para proteger os dados dos utilizadores.


- **Testes de Usabilidade**:
  - Testes de usabilidade para avaliar a experiência do utilizador com a aplicação.
  - Avaliar a facilidade de uso da aplicação, incluindo a interface de linha de comandos e a interface web.
  - Avaliar a acessibilidade da aplicação para utilizadores com diferentes níveis de habilidade técnica.


## Como Executar o Projeto

```bash
# Clonar o repositório
git clone https://github.com/AnaLu72/ProjetoBiblioteca.git

# Navegar até ao diretório do projeto
cd projetobiblioteca

# Certificar-se de que tem o Python 3.10 instalado:
python --version

# Criar um ambiente virtual (opcional):
python -m venv venv

# Ativar o ambiente virtual (se necessário):
.\venv\Scripts\activate

# Instalar as dependências (se necessário): 
pip install -r requirements.txt

# Executar as migrações do Django para criar as tabelas do banco de dados:
python manage.py makemigrations
python manage.py migrate

# Executar o servidor de desenvolvimento do Django:
python manage.py runserver

# Executar a applicação:
python main.py

# Acessar a aplicação através do navegador:
Abra o navegador e aceda à URL http://127.0.0.1:8000/
```

## Resultados

  **Principais resultados:**
  - Sistema funcional para gestão de bibliotecas pessoais.
  - Implementação de um sistema de empréstimos e devoluções de livros.
  - Interface intuitiva que facilita o registo e o controlo de livros.
  - Sistema de empréstimos que permite registar utilizadores e controlar devoluções.
  - Implementação de um sistema de autenticação e autorização para proteger os dados dos utilizadores.


## Conclusão

O projeto alcançou o principal objetivo de criar uma aplicação para gerir uma biblioteca pessoal, permitindo o registo e o controlo de livros. Foi implementado com foco em simplicidade e eficiência, com uma interface de linha de comandos intuitiva e uma interface web responsiva.

## Trabalhos Futuros
- **Melhoria da Interface Web**:
  - Adicionar funcionalidades de pesquisa e filtragem para livros.
  - Implementar uma interface de utilizador mais amigável e responsiva.
  - Melhorar a interface do utilizador com frameworks de design modernos.
  - Melhorar a experiência do utilizador com a aplicação.
  - Melhorar as funcionalidades de avaliação de livros.
  



