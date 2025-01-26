
def create_connection_string(
        user_name: str,
        password: str,
        host: str,
        port: int,
        database: str,
) -> str:
    return f"postgres://{user_name}:{password}@{host}:{port}/{database}"
    