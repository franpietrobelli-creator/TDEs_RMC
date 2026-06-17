# TDE3 — Previsão de Nota com Regressão Linear

Projeto desenvolvido para a disciplina de RMC. O programa utiliza Machine Learning (Regressão Linear) para prever a nota de um aluno com base em seus atributos acadêmicos e, a partir disso, indicar se ele foi aprovado ou não.

## Bibliotecas utilizadas

- `scikit-learn` — modelo de Regressão Linear
- `numpy` — manipulação de arrays

## Como funciona

### Parte 1 — Criar e treinar o modelo

```python
modelo = LinearRegression()

X = np.array([[7.0, 2, 0.9, 8, 2], ...])
y = np.array([6.5, 8.2, 3.6, 1.3, 9.7, 6.0, 2.8, 4.0, 8.5, 10.0])

modelo.fit(X, y)
```

A variável `modelo` cria um objeto vazio que irá aprender com os dados. `X` contém os atributos de cada aluno e `y` contém as notas correspondentes. O `modelo.fit(X, y)` treina o modelo, fazendo ele aprender o padrão entre os atributos e as notas para poder fazer previsões.

**Atributos de X (nessa ordem):**

| Coluna | Atributo            | Tipo  | Intervalo |
|--------|---------------------|-------|-----------|
| 1      | Média do aluno      | float | 0.0 – 10.0 |
| 2      | Horas extras        | int   | 0 – 6     |
| 3      | Frequência          | float | 0.0 – 1.0 |
| 4      | Tarefas feitas      | int   | 0 – 15    |
| 5      | Atividades extras   | int   | 0 – 5     |

---

### Parte 2 — Validação dos valores digitados

```python
def recebe_valor(mensagem: str, tipo: type, minimo: float, maximo: float) -> float | int:
    valido = False
    while not valido:
        try:
            valor = tipo(input(mensagem))
            if valor < minimo or valor > maximo:
                print(f'Valor tem que ser entre {minimo} e {maximo}')
            else:
                valido = True
        except ValueError as error:
            print(f'Certifique-se de digitar o tipo correto: {tipo}')
    return valor
```

Função reutilizável para coletar e validar qualquer atributo. Ela recebe a mensagem a exibir, o tipo esperado (`float` ou `int`), e os limites mínimo e máximo. Enquanto o valor digitado for inválido (tipo errado ou fora do intervalo), ela continua pedindo. Quando válido, retorna o valor.

---

### Parte 3 — Coletar dados e prever a nota

```python
media = recebe_valor('Digite a média do aluno entre 0.0 a 10.0: ', float, 0.0, 10.0)
horas_extras = recebe_valor('Digite quantas horas extras o aluno tem entre 0 a 6: ', int, 0, 6)
freq = recebe_valor('Digite a frequência do aluno entre 0.0 a 1.0: ', float, 0.0, 1.0)
tarefas_feitas = recebe_valor('Digite quantas tarefas o aluno completou entre 0 a 15: ', int, 0, 15)
atividades_extras = recebe_valor('Digite quantas atividades extras o aluno realizou entre 0 a 5: ', int, 0, 5)

dados_aluno_novo = np.array([[media, horas_extras, freq, tarefas_feitas, atividades_extras]])
nota_prevista = modelo.predict(dados_aluno_novo)
```

O programa coleta os atributos do aluno novo via terminal. Os dados são organizados em um array de duas dimensões (formato de tabela de uma linha) porque o modelo exige o mesmo formato usado no treino. Em seguida, `modelo.predict()` aplica o padrão aprendido e calcula a nota prevista.

---

### Parte 4 — Exibir resultado e decidir aprovação

```python
print(f'\nA nota do aluno novo prevista é: {nota_prevista[0]:.2f}')

if freq >= 0.5 and nota_prevista >= 7.0:
    print('O aluno foi aprovado')
else:
    print(f'O aluno provavelmente reprovará com a nota {nota_prevista[0]:.2f} e frequência {freq * 100}%')
```

Exibe a nota prevista e verifica as condições de aprovação. O aluno é aprovado somente se **ambas** as condições forem verdadeiras ao mesmo tempo (`and`): frequência maior ou igual a 50% **e** nota maior ou igual a 7.0. Se qualquer uma das duas falhar, o programa exibe a mensagem de reprovação com a nota e frequência do aluno.

---

## Como executar

1. Instale as dependências:
```bash
pip install scikit-learn numpy
```

2. Execute o arquivo:
```bash
python TDE3.py
```

3. Digite os atributos do aluno quando solicitado e veja a previsão.
