try:
    from app import app
except ImportError as e_imp:
    print(f"The following import ERROR occurred in {__file__}: {e_imp}")

if __name__ == "__main__":
    try:
        app.run()
    except Exception as err:
        print(f"The following ERROR occurred in {__file__}: {err}")