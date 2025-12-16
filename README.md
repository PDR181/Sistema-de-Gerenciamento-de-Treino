# MoveFit 🏋️‍♂️

Aplicação web em Django para **gerenciamento de fichas de treino**.  
Permite ao usuário criar, visualizar e gerenciar fichas de exercícios, registrando séries, repetições, carga (kg) e visualizando GIFs demonstrativos de cada exercício.

---

## 🚀 Tecnologias

- Python 3.x
- Django 4.x (ou versão usada no projeto)
- HTML, CSS (layout próprio)
- SQLite (padrão do Django para desenvolvimento)

---

## ⚙️ Como rodar o projeto

### 1. Clonar o repositório

git clone https://github.com/PDR181/Sistema-de-Gerenciamento-de-Treino.git
cd seu-repo/MoveFit

---
### 2. Criar e ativar o ambiente virtual (opcional, mas recomendado)

No Windows (CMD):

python -m venv env
env\Scripts\activate



### 3. Instalar dependências

pip install -r requirements.txt



(se ainda não tiver o `requirements.txt`, você pode gerar com `pip freeze > requirements.txt`.)

### 4. Aplicar as migrações

python manage.py migrate



### 5. Criar um superusuário (opcional, para acessar o admin)

python manage.py createsuperuser



### 6. Rodar o servidor

python manage.py runserver



Acesse no navegador:

http://127.0.0.1:8000/



---

## 📌 Funcionalidades principais

- Cadastro e login de usuários.
- Perfil do usuário com edição de dados básicos.
- Listagem de **fichas de treino** do usuário.
- Criação de fichas personalizadas, vinculadas ao usuário.
- Adição de itens na ficha:
  - Exercício
  - Número de séries
  - Número de repetições
  - Peso (kg)
- Edição e exclusão de itens da ficha.
- Exclusão de fichas completas, com confirmação.
- Exibição de **GIFs demonstrativos** dos exercícios em modal.
- Sistema de mensagens de feedback (sucesso/erro).
- Telas de autenticação personalizadas:
  - Login
  - Alteração de senha
  - Recuperação e redefinição de senha (fluxo completo)
  - Integração total com o layout MoveFit.

---
## 📂 Estrutura geral (simplificada)

MoveFit/
manage.py
movefit/ # Configurações do projeto
treino_app/ # App principal (fichas, exercícios, perfil)
templates/
base.html
treino/
fichas_list.html
ficha_detalhe.html
...
registration/
login.html
password_change_form.html
password_change_done.html
password_reset_form.html
password_reset_done.html
password_reset_confirm.html
password_reset_complete.html
static/
treino_app/
style.css



---

## 📝 Próximos passos (ideias)

- Adicionar gráficos de progresso.
- Filtros por grupo muscular / tipo de treino.
- Integração com dispositivos/wearables.
- Sugestão automática de treinos com base no histórico.

---
