import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data_diabetes = pd.read_csv('DATOS_TABULADOS.csv', delimiter=",")
knn = KNeighborsClassifier(n_neighbors=3)
X = data_diabetes[['cumpleaños',	'actividades',	'time',	'gift', 'money',	'party',	'angry',	'vacations']]
y = data_diabetes[['VISUAL','AUDITIVO','KINI']]
knn.fit(X, y)


def validar_datos(data):
    data_list = data.tolist()  # Convertir la matriz a una lista
    if data_list == [[1, 0, 0]]:
        return "VISUAL"
    elif data_list == [[0, 1, 0]]:
        return "AUDITORY"
    elif data_list == [[0, 0, 1]]:
        return "KINESTHETIC"
    else:
        return "Unknown"


def asignarRuta(respuestas_estudiante):
    try:
        print(respuestas_estudiante)    
        df_prediccion = pd.DataFrame([respuestas_estudiante], columns=['cumpleaños', 'actividades', 'time', 'gift', 'money',
                                                                   'party', 'angry', 'vacations'])
        prediccion = knn.predict(df_prediccion)
        print(prediccion)
        return {
            "learningPath": validar_datos(prediccion),
            "status": 200
        }

    except Exception as e:
        print(f"Exception occurred: {e}")
        return {
            "probability": -1,
            "status": 500
        }