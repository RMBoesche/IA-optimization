import numpy as np

def get(data, variable):
    """
    Seleciona x ou y do csv das datas.
    Se passado a variável 'y' é retornado a coluna 1. Caso contrário é retornado a coluna 0 (utilizado para a variável 'x')
    :param data: list - lista das datas a ser selecionado
    :param variable: string - nome da variável a ser selecionada (x ou y)
    :return: list - lista contendo somente os valores da coluna desejada
    """
    column = 0
    if (variable == 'y'):
        column = 1
    return [row[column] for row in data]

    
def predict(theta_0, theta_1, x_values):
    """
    Realiza a predição multiplicando theta_1 por x e somando theta_0 para cada valor na lista x_values
    :param theta_0: int - intercepto da reta
    :param theta_1: int - inclinacao da reta
    :param x_values: list - nome da variável a ser selecionada (x ou y)
    :return: list - lista contendo as predições para cada valor de x
    """
    return [theta_0 + theta_1 * x for x in x_values]

def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: int - intercepto da reta
    :param theta_1: int - inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    x = get(data, 'x')
    y = get(data, 'y')

    predicted = predict(theta_0, theta_1, x)

    y = np.array(y)
    predicted = np.array(predicted)

    erros = np.subtract(predicted, y)
    mse = np.mean(erros**2)
    return mse

def differential(theta, y, predicted, x = 0):
    """
    Calcula a derivada do theta_0 ou do theta_1.
    :param theta: string - nome do theta a ser calculado a derivada (theta_0 ou theta_1)
    :param y: list - lista dos valores reais de y
    :param predicted: list - lista dos valores preditos de y
    :param x: list (optional) - para o caso do theta_1 é necessário multiplicar pelo valor de x
    :return: np.array - derivada do theta
    """
    y = np.array(y)
    predicted = np.array(predicted)
    differences = np.subtract(predicted, y)
    if (theta == 'theta_1'):
        differences = np.multiply(differences, x)

    return 2 * np.mean(differences)


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    x = get(data, 'x')
    y = get(data, 'y')
    predicted = predict(theta_0, theta_1, x)

    differential_theta0 = differential('theta_0', y, predicted)
    differential_theta1 = differential('theta_1', y, predicted, x)

    new_theta0 = theta_0 - alpha * differential_theta0
    new_theta1 = theta_1 - alpha * differential_theta1
    return new_theta0, new_theta1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    theta0_list = [theta_0]
    theta1_list = [theta_1]
    for i in range(num_iterations):
        (theta_0, theta_1) = step_gradient(theta_0, theta_1, data, alpha)
        theta0_list.append(theta_0)
        theta1_list.append(theta_1)
    return theta0_list, theta1_list
