"""Example: Using the Autonomous Agent"""
from agent.agent import Agent

def main():
    print("\n🤖 NEURON Autonomous Agent Example")
    print("=" * 50)
    
    # Create agent
    agent = Agent(name="TaskMaster")
    
    # Show available tools
    print("\n🔧 Available Tools:")
    tools = agent.get_available_tools()
    for tool, desc in tools.items():
        print(f"  - {tool}: {desc}")
    
    # Execute a complex task
    task = "Calculate 100 + 50, then check if the result is prime, then generate 5 random numbers"
    
    print(f"\n📋 Task: {task}")
    print("\n⚙️  Executing task...")
    
    try:
        result = agent.execute_task(task)
        
        print(f"\n✅ Task Status: {result['status']}")
        print(f"Steps Executed: {result['steps_executed']}")
        
        print("\n📝 Execution Plan:")
        for i, step in enumerate(result['results'], 1):
            print(f"  Step {i}: {step['description']}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
    
    print("\n✅ Agent example completed!\n")

if __name__ == "__main__":
    main()
