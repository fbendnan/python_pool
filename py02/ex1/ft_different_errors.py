def garden_operations(error, is_one_error):
    if is_one_error:
        try:
            if error == "ValueError":
                int("abc")
            elif error == "ZeroDivisionError":
                result = 4/0
            elif error == "FileNotFoundError":
                open("missing.txt", "r")
            elif error == "KeyError":
                d = {}
                print(d["plant"])
        except ValueError:
            print(f"Caught ValueError: invalid literal for int()")
        except ZeroDivisionError:
            print(f"Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print(f"Caught FileNotFoundError: No such file 'missing.txt'")
        except KeyError:
            print(f"Caught KeyError: 'missing\\_plant'")
    
    
def test_error_types():
    print("=== Garden Error Types Demo ===")
    errors = ["ValueError", "ZeroDivisionError", "FileNotFoundError", "KeyError"]

    for error in errors:
        print(f"\nTesting {error}...")
        garden_operations(error, True)
    print("\nTesting multiple errors together...")
    try:
        result = 4/0
        d = {}
        print(d["plant"])
        open("missing.txt", "r")
    except:
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")

test_error_types()