# Cada usuário possui um ID único e um nome.
users = [
    {"id": 0, "name": "Luna"},
    {"id": 1, "name": "Caio"},
    {"id": 2, "name": "Maya"},
    {"id": 3, "name": "Ravi"},
    {"id": 4, "name": "Nina"},
    {"id": 5, "name": "Theo"},
    {"id": 6, "name": "Bia"},
    {"id": 7, "name": "Davi"},
    {"id": 8, "name": "Iris"},
    {"id": 9, "name": "Noah"},
]

# Cada tupla representa uma amizade entre dois IDs de usuários.
friendship_pairs = [
    (0, 1),
    (0, 4),
    (0, 7),
    (0, 8),
    (1, 2),
    (1, 5),
    (2, 3),
    (2, 9),
    (3, 6),
    (4, 5),
    (4, 8),
    (5, 9),
    (6, 7),
    (7, 8),
    (8, 9),
]

# Cria uma lista vazia de amigos para cada usuário.
friendships = {user["id"]: [] for user in users}

# Registra a amizade nos dois sentidos: se A é amigo de B, B também é amigo de A.
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# Retorna a quantidade de amigos de um usuário.
def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

# Soma todas as amizades registradas para obter o total de conexões.
total_connections = sum(number_of_friends(user)
                        for user in users)

# Calcula a média de amigos por usuário.
num_users = len(users)
avg_connections = total_connections / num_users

# Cria uma lista com o ID e a quantidade de amigos de cada usuário.
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

# Ordena os usuários do maior para o menor número de amizades.
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
)



