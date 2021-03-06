import numpy as np


def crossOverIndividuo(pai_1, pai_2):
    filho_1 = []

    for cromossomo in range(6):
        filhos = crossOver(pai_1[cromossomo], pai_2[cromossomo])
        filho_1.append(filhos)

    return filho_1


def crossOver(pai_1, pai_2):
    filho_1 = list(np.full(len(pai_1), fill_value={'disciplina': None}))

    mask = list(np.full(len(pai_1)//2, fill_value=1)) + list(np.full(len(pai_1)//2, fill_value=0))

    np.random.shuffle(mask)

    delete_pai_1 = []

    for aula in range(len(filho_1)):
        if mask[aula] == 1:
            filho_1[aula] = pai_1[aula]
            delete_pai_1.append(aula)

    pai_1_deleted = np.delete(pai_1, delete_pai_1)

    pai_2_index = []

    pai_2_array = np.array(pai_2)

    for i in pai_1_deleted:
        pai_2_index.append(np.where(pai_2_array == i)[0][0])

    filho_1_rest = [x for _, x in sorted(zip(pai_2_index, pai_1_deleted))]

    contador_filho_1 = 0

    for aula in range(len(filho_1)):
        if mask[aula] != 1:
            filho_1[aula] = filho_1_rest[contador_filho_1]
            contador_filho_1 += 1

    return filho_1
