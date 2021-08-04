# Testes unitários

Esse projeto visa demonstrar uma introdução à construção de testes unitários em Python. As libs utilzadas no projeto são PyTest e Unittest (nativa do python). A versão do python em que o projeto foi elaborado é a 3.6.9.

## Instalando os requisitos do projeto

Crie seu ambiente virtual da maneira que você está acostumado. No meu caso utilizei o pyenv. Para criar o ambiente:

```
pyenv virtualenv 3.6.9 testando-123
```

Em seguida, ative o ambiente...

```
pyenv activate testando-123
```

...e, por fim, instale as bibliotecas do arquivo _requirements.txt_.

```
pip install -r requirements.txt
```

## Executando o Pytest

Ao baixar esse projeto já é possível observar alguns testes de exemplo que estão separados por diretórios. Para ver o pytest em ação execute:

```
pytest .s
```

Para melhor o resultado apresentado pelo pytest aumente a verbosidade com o parâmetro "-v" (ou ainda mais com "-vv").

```
pytest -v .
```

Se estiver no diretório certo, os testes de exemplo já preenchidos irão ser executados e apresentados no seu terminal.