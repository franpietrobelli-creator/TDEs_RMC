# TDEs de RMC

Trabalhos Discentes Efetivos (TDEs) da disciplina **RMC** do 1º semestre de Engenharia de Software (PUCPR), feitos em Python.

| Arquivo | Trabalho | Resumo |
|---|---|---|
| `TDE2.py` | TDE 2: Labirinto em grade | Jogo de terminal em que o jogador procura a saída de um labirinto coberto por neblina |
| `TDE3.py` | TDE 3: Previsão de nota | Usa Machine Learning (regressão linear) para prever a nota de um aluno e dizer se ele foi aprovado |
| `teste.py` | Teste do TDE 3 | Versão de testes do TDE 3 que também mostra a qualidade do modelo (R²) |

---

## TDE 2: Labirinto em grade

Jogo em que o jogador (`J`) começa no canto superior esquerdo de um labirinto 8x8 e precisa chegar até a saída (`S`).

**Regras**
- `#` é parede, `.` é espaço livre e `?` é neblina
- O jogador só enxerga as casas ao redor dele (distância de 1 casa); o resto fica coberto por `?`
- Movimentos: `W` (cima), `S` (baixo), `A` (esquerda), `D` (direita)
- Digite `0` ou `sair` para encerrar

**Como o código funciona**
- `TABULEIRO` é uma matriz (lista de listas) com o mapa do labirinto
- `exibir_com_neblina()` percorre a matriz e só mostra as casas a até 1 de distância do jogador
- `mover()` calcula a nova posição de acordo com a tecla digitada
- `posicao_valida()` impede que o jogador saia do mapa ou atravesse uma parede
- `jogar()` é o laço principal: mostra o tabuleiro, lê o movimento, valida, move o jogador e termina quando ele chega na saída

```bash
python TDE2.py
```

---

## TDE 3: Previsão de nota com regressão linear

O programa usa Machine Learning (regressão linear) para prever a nota de um aluno a partir dos seus atributos acadêmicos e, com isso, indicar se ele foi aprovado ou não.

### Bibliotecas usadas

- `scikit-learn`: modelo de regressão linear
- `numpy`: manipulação de arrays

Se o scikit-learn não carregar (por exemplo, bloqueado pelo Windows), o código usa uma regressão linear própria feita com `numpy` (mínimos quadrados), que dá o mesmo resultado.

### Parte 1: criar e treinar o modelo

```python
modelo = LinearRegression()

X = np.array([[7.0, 2, 0.9, 8, 2], ...])
y = np.array([6.5, 8.2, 3.6, 1.3, 9.7, 6.0, 2.8, 4.0, 8.5, 10.0])

modelo.fit(X, y)
```

`modelo` é um objeto vazio que vai aprender com os dados. `X` tem os atributos de 10 alunos e `y` tem as notas de cada um. O `modelo.fit(X, y)` treina o modelo, ou seja, ele aprende a relação entre os atributos e as notas para conseguir fazer previsões.

**Atributos de X (nessa ordem):**

| Coluna | Atributo | Tipo | Intervalo |
|---|---|---|---|
| 1 | Média do aluno | float | 0.0 – 10.0 |
| 2 | Horas extras | int | 0 – 6 |
| 3 | Frequência | float | 0.0 – 1.0 |
| 4 | Tarefas feitas | int | 0 – 15 |
| 5 | Atividades extras | int | 0 – 6 |

### Parte 2: validação dos valores digitados

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

Função reutilizada para pedir e validar cada atributo. Ela recebe a mensagem, o tipo esperado (`float` ou `int`) e os limites mínimo e máximo. Enquanto o valor for inválido (tipo errado ou fora do intervalo), ela continua pedindo. Quando o valor é válido, ela o retorna.

### Parte 3: coletar os dados e prever a nota

```python
dados_aluno_novo = np.array([[media, horas_extras, freq, tarefas_feitas, atividades_extras]])
nota_prevista = modelo.predict(dados_aluno_novo)
```

O programa pede os atributos do aluno novo no terminal. Os dados ficam em um array de duas dimensões (uma tabela de uma linha), porque o modelo exige o mesmo formato usado no treino. Depois, `modelo.predict()` aplica o que foi aprendido e calcula a nota prevista.

### Parte 4: mostrar o resultado e decidir a aprovação

```python
if freq >= 0.5 and nota_prevista[0] >= 7.0:
    print('O aluno foi aprovado')
else:
    print(f'O aluno provavelmente reprovará com a nota {nota_prevista[0]:.2f} e frequencia {freq * 100:.0f}%')
```

O aluno só é aprovado se as **duas** condições forem verdadeiras ao mesmo tempo (`and`): frequência de pelo menos 50% **e** nota prevista de pelo menos 7.0. Se uma delas falhar, o programa mostra a mensagem de reprovação com a nota e a frequência.

### Como executar

```bash
pip install scikit-learn numpy
python TDE3.py
```

Digite os atributos do aluno quando o programa pedir e veja a previsão.

---

## `teste.py`

Versão usada para testar o TDE 3 antes da entrega. É o mesmo programa, com uma linha a mais que mostra o **R²** (`modelo.score(X, y)`), que indica o quanto o modelo se ajusta aos dados de treino: quanto mais perto de 1, melhor.

---

O TDE 3 também está, junto com os protótipos e o notebook da aula de scikit-learn, no repositório [Notavel](https://github.com/franpietrobelli-creator/Notavel).
