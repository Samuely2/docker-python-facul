class User:
    # Simulação de um banco de dados
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]

    @classmethod
    def get_users(cls):
        return cls.users

    @classmethod
    def get_user_by_id(cls, user_id):
        for user in cls.users:
            if user["id"] == user_id:
                return user
        return None
    
    @classmethod
    def store(cls, data):

        new_user = {
            "id": len(cls.users) + 1,
            "name": data["name"],
            "email": data["email"]
        }

        cls.users.append(new_user)
        
        return cls.users