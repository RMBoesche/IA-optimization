import numpy as np

def get(data, variable):
    column = 0
    if (variable == 'y'):
        column = 1
    return [row[column] for row in data]

    
def predict(theta_0, theta_1, x_values):
    return [theta_0 + theta_1 * x for x in x_values]

def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    # calcula os erros (diferenças entre as previsões e os valores reais de y)
    x = get(data, 'x')
    y = get(data, 'y')

    predicted = predict(theta_0, theta_1, x)

    y = np.array(y)
    predicted = np.array(predicted)

    erros = np.subtract(predicted, y)
    mse = np.mean(erros**2)
    return mse

def differential(theta, y, predicted, x = 0):
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
    print('nosso')
    theta0_list = [theta_0]
    theta1_list = [theta_1]
    for i in range(num_iterations):
        (theta_0, theta_1) = step_gradient(theta_0, theta_1, data, alpha)
        theta0_list.append(theta_0)
        theta1_list.append(theta_1)
    return theta0_list, theta1_list
