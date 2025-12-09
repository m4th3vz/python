# 🚀 Como rodar este projeto com Streamlit

## 1. Instale as dependências

No terminal, execute:

```bash
pip install -r requirements.txt
```

Ou, se o projeto não tiver `requirements.txt`:

```bash
pip install streamlit
```

## 2. Execute o aplicativo

No terminal, dentro da pasta do projeto, rode:

```bash
streamlit run app.py
```

Substitua `app.py` pelo nome do arquivo principal do seu projeto.

## 3. Acesse no navegador

Após rodar o comando, o Streamlit abrirá automaticamente uma janela com o endereço:

```
http://localhost:8501
```

Caso não abra automaticamente, copie o link e cole no navegador.

## 4. Atualizações em tempo real

Sempre que você modificar o código, o Streamlit recarrega a página automaticamente.

---

## 📋 Requisitos

- Python 3.7 ou superior
- Streamlit

## 💡 Dicas

- Para parar o servidor, pressione `Ctrl + C` no terminal
- Para rodar em uma porta diferente: `streamlit run app.py --server.port 8502`
- Para desabilitar o recarregamento automático: `streamlit run app.py --server.runOnSave false`

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.