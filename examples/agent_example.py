"""Example: Using the Autonomous Agent"""
from agent.agent import Agent
from utils.logger import get_logger
import json

logger = get_logger(__name__)


def main():
    """Run agent example"""
    logger.info("=" * 50)
    logger.info("AI Powerhouse - Agent Example")
    logger.info("=" * 50)
    
    # Initialize agent
    agent = Agent(name="TaskBot")
    
    # Example tasks
    tasks = [
        "Calculate the sum of 15 and 25",
        "Find information about Python programming",
    ]
    
    for task in tasks:
        logger.info(f"\nExecuting task: {task}")
        try:
            result = agent.execute_task(task)
            
            logger.info(f"Status: {result['status']}")
            logger.info(f"Steps executed: {len(result['steps_executed'])}")
            logger.info(f"Final result: {result['final_result'][:100]}...")
        except Exception as e:
            logger.error(f"Error: {str(e)}")
    
    # Print execution history
    logger.info(f"\nExecution History:")
    history = agent.get_history()
    logger.info(f"Total executions: {len(history)}")
    
    # Print available tools
    logger.info(f"\nAvailable Tools:")
    tools = agent.tools.get_tools()
    for tool in tools:
        logger.info(f"  - {tool['name']}: {tool['description']}")


if __name__ == "__main__":
    main()
