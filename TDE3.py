import numpy as np

try:
    from sklearn.linear_model import LinearRegression
except ImportError:
    # Fallback caso o scikit-learn não carregue (ex.: bloqueado pelo Windows):
    # regressão linear por mínimos quadrados, equivalente à do sklearn
    class LinearRegression:
        def fit(self, X, y):
            X_com_intercepto = np.column_stack([np.ones(len(X)), X])
            coeficientes = np.linalg.lstsq(X_com_intercepto, y, rcond=None)[0]
            self.intercept_ = coeficientes[0]
            self.coef_ = coeficientes[1:]
            return self

        def predict(self, X):
            return np.asarray(X) @ self.coef_ + self.intercept_

modelo = LinearRegression()

X = np.array([[7.0, 2, 0.9, 8, 2],
              [9.0, 4, 1.0, 12, 4],
              [4.5, 1, 0.6, 5, 1],
              [2.2, 0, 1.0, 3, 0],
              [9.8, 5, 0.8, 13, 5],
              [6.6, 3, 0.7, 6, 3],
              [3.7, 6, 1.0, 2, 1],
              [5.6, 3, 0.6, 4, 2],
              [8.9, 5, 0.7, 10, 6],
              [9.3, 6, 0.7, 15, 5]])

y = np.array([6.5, 8.2, 3.6, 1.3, 9.7, 6.0, 2.8, 4.0, 8.5, 10.0])

modelo.fit(X, y)

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


media = recebe_valor('Digite a média do aluno entre 0.0 a 10.0: ', float, 0.0, 10.0)   
horas_extras = recebe_valor('Digite quantas horas extras o aluno tem entre 0 a 6: ', int, 0, 6)
freq = recebe_valor('Digite a frequência do aluno entre 0.0 a 1.0: ', float, 0.0, 1.0)
tarefas_feitas = recebe_valor('Digite quantas tarefas o aluno completou entre 0 a 15: ', int, 0, 15)
atividades_extras = recebe_valor('Digite quantas atividades extras o aluno realizou entre 0 a 6: ', int, 0, 6)

dados_aluno_novo = np.array([[media, horas_extras, freq, tarefas_feitas, atividades_extras]])
nota_prevista = modelo.predict(dados_aluno_novo)

print(f'\nA nota do aluno novo prevista é: {nota_prevista[0]:.2f}')

if freq >= 0.5 and nota_prevista[0] >= 7.0:
    print('O aluno foi aprovado')
else:
    print(f'O aluno provavelmente reprovará com a nota {nota_prevista[0]:.2f} e frequencia {freq * 100:.0f}%')    