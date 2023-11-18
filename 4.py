import pickle
import pandas as pd
import matplotlib.pylab as plt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "score": [60, 63, 64, 67, 68, 71, 72, 75, 76, 78],
        }
    )
    df_x = df["hours"]
    df_y = df["score"]

    plt.scatter(df_x, df_y, label="data")
    plt.xlabel("hours")
    plt.ylabel("score")
    plt.show()

    x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.3)

    lr = LinearRegression()
    lr.fit(x_train.values.reshape(-1, 1), y_train)
    y_pred = lr.predict(x_test.values.reshape(-1, 1))
    print("Mean Squared Error:", metrics.mean_squared_error(y_test, y_pred))

    with open("models/model.pkl", "wb") as f:
        pickle.dump(lr, f)

    with open("models/model.pkl", "rb") as f:
        load_lr = pickle.load(f)

    hour_12 = load_lr.predict([[12]])
    hour_14 = load_lr.predict([[14]])
    print(hour_12)
    print(hour_14)
