import pandas as pd
from sqlalchemy import create_engine

def load_users():
    print("Loading user data from source...")
    data = {
        'user_id': range(1, 101),
        'email': [f'user{i}@example.com' for i in range(1, 101)],
        'status': ['active'] * 80 + ['inactive'] * 20,
    }
    df = pd.DataFrame(data)
    print(f"Loaded {len(df)} users")
    return df

if __name__ == "__main__":
    load_users()
