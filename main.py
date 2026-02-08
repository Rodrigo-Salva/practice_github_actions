def hello():
    """Job que ejecuta el saludo inicial"""
    print("Hello! Starting CI/CD pipeline...")
    return True

def test():
    """Job que ejecuta las pruebas"""
    print("Running tests...")
    return True

def main():
    """Flujo principal con condicionales"""
    # Ejecutar job 'hello'
    hello_result = hello()
    
    # El job 'test' se ejecuta SOLO si 'hello' fue exitoso
    if hello_result:
        print("✓ Hello job completed successfully!")
        test_result = test()
        if test_result:
            print("✓ Test job completed successfully!")
    else:
        print("✗ Hello job failed! Skipping test job.")

if __name__ == "__main__":
    main()
