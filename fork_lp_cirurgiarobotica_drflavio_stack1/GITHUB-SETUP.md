# Configuração GitHub para o projeto

## 1. Abrir terminal
- Abra o terminal no VS Code com `Ctrl + \``.
- Verifique se está na pasta do projeto:
  ```bash
  cd "c:\Users\Samsung\Documents\projetos_desenvolvidos\github_projetos\lp_cirurgiarobotica_drflavio"
  ```

## 2. Verificar se já há repositório Git
- Execute:
  ```bash
  git status
  ```
- Se aparecer `fatal: not a git repository`, siga para o passo 3.
- Se aparecer `On branch ...`, o Git já está ativo no projeto.

## 3. Inicializar repositório Git local
- Se ainda não houver repositório:
  ```bash
  git init
  ```
- Adicione os arquivos:
  ```bash
  git add .
  ```
- Faça o primeiro commit:
  ```bash
  git commit -m "Inicializa projeto de landing page Dr. Flávio"
  ```

## 4. Criar repositório no GitHub
- No GitHub, clique em "New repository".
- Defina:
  - Nome: `lp_cirurgiarobotica_drflavio`
  - Visibilidade: `Private` ou `Public`
- Não adicione README, .gitignore ou licença se já tiver iniciado localmente.

## 5. Conectar o repositório local ao GitHub
- Copie a URL do repositório remoto.
- No terminal, execute:
  ```bash
  git remote add origin https://github.com/SEU-USUARIO/NOME-REPO.git
  git branch -M main
  git push -u origin main
  ```
- Substitua `SEU-USUARIO` e `NOME-REPO` pela URL correta.

## 6. Próximos commits
- Depois de cada alteração relevante:
  ```bash
  git add .
  git commit -m "Descrição clara do que foi alterado"
  git push
  ```

## 7. Vantagens para este projeto
- Histórico de mudanças organizado
- Segurança de backup remoto
- Facilidade para voltar a versões anteriores
- Colaboração futura mais simples
- Documentação de decisões por meio de commits

## Dica
- Se quiser conferir o status do repositório remoto:
  ```bash
  git remote -v
  ```

```// filepath: c:\Users\Samsung\Documents\projetos_desenvolvidos\github_projetos\lp_cirurgiarobotica_drflavio\GITHUB-SETUP.md

# Configuração GitHub para o projeto

## 1. Abrir terminal
- Abra o terminal no VS Code com `Ctrl + \``.
- Verifique se está na pasta do projeto:
  ```bash
  cd "c:\Users\Samsung\Documents\projetos_desenvolvidos\github_projetos\lp_cirurgiarobotica_drflavio"
  ```

## 2. Verificar se já há repositório Git
- Execute:
  ```bash
  git status
  ```
- Se aparecer `fatal: not a git repository`, siga para o passo 3.
- Se aparecer `On branch ...`, o Git já está ativo no projeto.

## 3. Inicializar repositório Git local
- Se ainda não houver repositório:
  ```bash
  git init
  ```
- Adicione os arquivos:
  ```bash
  git add .
  ```
- Faça o primeiro commit:
  ```bash
  git commit -m "Inicializa projeto de landing page Dr. Flávio"
  ```

## 4. Criar repositório no GitHub
- No GitHub, clique em "New repository".
- Defina:
  - Nome: `lp_cirurgiarobotica_drflavio`
  - Visibilidade: `Private` ou `Public`
- Não adicione README, .gitignore ou licença se já tiver iniciado localmente.

## 5. Conectar o repositório local ao GitHub
- Copie a URL do repositório remoto.
- No terminal, execute:
  ```bash
  git remote add origin https://github.com/SEU-USUARIO/NOME-REPO.git
  git branch -M main
  git push -u origin main
  ```
- Substitua `SEU-USUARIO` e `NOME-REPO` pela URL correta.

## 6. Próximos commits
- Depois de cada alteração relevante:
  ```bash
  git add .
  git commit -m "Descrição clara do que foi alterado"
  git push
  ```

## 7. Vantagens para este projeto
- Histórico de mudanças organizado
- Segurança de backup remoto
- Facilidade para voltar a versões anteriores
- Colaboração futura mais simples
- Documentação de decisões por meio de commits

## Dica
- Se quiser conferir o status do repositório remoto:
  ```bash
  git remote -v
  ```
