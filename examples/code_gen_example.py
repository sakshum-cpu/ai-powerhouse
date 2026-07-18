"""Example: Using the Code Generator"""
from code_generator.generator import CodeGenerator

def main():
    print("\n💻 NEURON Code Generator Example")
    print("=" * 50)
    
    # Create code generator
    gen = CodeGenerator()
    
    # Example 1: Generate simple function
    print("\n📝 Example 1: Generate a palindrome checker function")
    description1 = "Create a function that checks if a number is a palindrome"
    
    try:
        result1 = gen.generate(description1, language="python")
        
        print(f"\n✅ Generated Code (Valid: {result1['valid']}):")
        print("-" * 40)
        print(result1['code'])
        print("-" * 40)
        
        if result1['validation']['security_issues']:
            print(f"⚠️  Security Issues: {result1['validation']['security_issues']}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
    
    # Example 2: Generate and execute
    print("\n\n📝 Example 2: Generate and execute a sorting function")
    description2 = "Write a function to sort a list of numbers in ascending order"
    
    try:
        result2 = gen.generate_and_execute(description2, language="python")
        
        print(f"\n✅ Generated & Executed (Valid: {result2['valid']}):")
        print("-" * 40)
        print(result2['code'])
        print("-" * 40)
        
        if result2['valid']:
            exec_result = result2.get('execution', {})
            if exec_result.get('success'):
                print(f"\n✅ Execution Output:\n{exec_result['output']}")
            else:
                print(f"\n❌ Execution Error: {exec_result.get('error')}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print("\n✅ Code Generator example completed!\n")

if __name__ == "__main__":
    main()
