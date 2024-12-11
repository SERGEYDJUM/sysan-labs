import json


def get_activation(value: float, array: list[tuple[float, float]]) -> float:
    if value < array[0][0] or value > array[-1][0]:
        return 0.0

    right = 1

    for i in range(1, len(array)):
        if value == array[i][0]:
            return array[i][1]
        elif value < array[i][0]:
            right = i
            break

    x_0, y_0 = array[right - 1][0], array[right - 1][1]
    x_1, y_1 = array[right][0], array[right][1]

    return y_0 + ((value - x_0) * (y_1 - y_0) / (x_1 - x_0))


def task(temp_f: str, control_f: str, rules_f: str, temp: float) -> float:
    # Согласуем названия с теми что в функции отображения
    temp_f = temp_f.replace("комфортно", "нормально")
    control_f = (
        control_f.replace("слабый", "слабо")
        .replace("умеренный", "умеренно")
        .replace("интенсивный", "интенсивно")
    )

    temp_json = json.loads(temp_f)
    control_json = json.loads(control_f)
    rules_json = json.loads(rules_f)

    C_sets = []
    control_points = set()
    for t_id, c_id in rules_json:
        t_fs, c_fs = None, None

        for mode in temp_json["температура"]:
            if mode["id"] == t_id:
                t_fs = mode["points"]

        for mode in control_json["температура"]:
            if mode["id"] == c_id:
                c_fs = mode["points"]

        for point in c_fs:
            control_points.add(point[0])

        temp_act = get_activation(temp, t_fs)
        C_sets.append([(x_s, min(temp_act, y_s)) for x_s, y_s in c_fs])

    optimal_control = []
    for point in sorted(control_points):
        point_activation = max([get_activation(point, c_set) for c_set in C_sets])
        optimal_control.append((point, point_activation))

    # Метод первого максимума
    s, s_act = 0, 0
    for p, p_act in optimal_control:
        if s_act < p_act:
            s, s_act = p, p_act

    return s


main = task

if __name__ == "__main__":
    with open("assets/функция-отображения.json", encoding="utf-8") as rules_f, open(
        "assets\функции-принадлежности-управление.json", encoding="utf-8"
    ) as control_f, open(
        "assets\функции-принадлежности-температуры.json", encoding="utf-8"
    ) as temp_f:
        print(main(temp_f.read(), control_f.read(), rules_f.read(), 19))
