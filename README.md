# Testes unitários

Esse projeto visa demonstrar uma introdução à construção de testes unitários em Python. As libs utilzadas no projeto são PyTest e Unittest (nativa do python). A versão do python em que o projeto foi elaborado é a 3.6.9.

## Por que testar?

Testes unitários são fundamentais na busca de garantir um código estável. Testes bem planejados e construídos auxiliam na identificação de erros lógicos nas regras de negócio e demais interações que o seu código realiza. 

Antes de mais nada é preciso citar alguns dos princípios que eu considerdo essenciais para a construção dos nossos testes:

1. Organização: um grupo de testes deve focar sobre um conjunto de métodos similares, próximos entre sí. Isto é, não faça todo o teste da sua aplicação/ferramenta/biblioteca em um único arquivo.

2. Teste o necessário: talvez você já tenha ouvido falar sobre a meta do código 100% coberto por testes. Porém, certos métodos ou funções podem não precisar de testes, pois a ação tomada por eles pode não conter lógica ou então só invocar algo externo que já tem seus testes próprios. Por exemplo:

```python
import request

def get_data():
    return request.get('http://my-url.contaazul.com.br')
```

3. Pense: esse código é realmente testável? É importante analisar se o código permite a construção de testes organizados e claros. Códigos mal estruturados podem tornar os testes mais complexos que o próprio código.

4. Quando possível, siga o TDD: o TDD (_Test Driven Development_) segue o fundamento que o teste vem antes do código. Em refatorações impactantes e, principalmente, em códigos novos, tente aplicar o TDD. Mapeie as funcionalidades que serão implementadas, planeje conforme as regras de negócio e construa os testes antes de "codar".

## Preparando o terreno

### Instalando os requisitos do projeto

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

### Executando o Pytest

Ao baixar esse projeto já é possível observar alguns testes de exemplo que estão separados por diretórios. Para ver o pytest em ação execute:

```
pytest .s
```

Para melhor o resultado apresentado pelo pytest aumente a verbosidade com o parâmetro "-v" (ou ainda mais com "-vv").

```
pytest -v .
```

Se estiver no diretório certo, os testes de exemplo já preenchidos irão ser executados e apresentados no seu terminal.

## Referências

* https://python-guide-pt-br.readthedocs.io/pt_BR/latest/writing/tests.html
* https://docs.python.org/pt-br/dev/library/unittest.html]
* http://devfuria.com.br/python/tdd-primeiros-passos-com-testes-unitarios/
* https://docs.pytest.org/en/6.2.x/assert.html