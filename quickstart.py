#!/usr/bin/env python3
"""
🚀 NEURON - Quick Start Script
Runs everything you need in one command!
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"🔄 {description}")
    print('='*60)
    try:
        result = subprocess.run(cmd, shell=True, capture_output=False)
        if result.returncode != 0:
            print(f"⚠️ {description} had issues")
            return False
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main execution"""
    print("\n" + "="*60)
    print("🧠⚡ NEURON - AI Powerhouse Quick Start")
    print("="*60)
    
    # Check Python version
    print(f"\n✅ Python {sys.version}")
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Please ensure .env file is configured with your OpenAI API key")
        sys.exit(1)
    
    print("✅ .env file found (API key configured)")
    
    # Run setup and test
    print("\n" + "="*60)
    print("🚀 STARTING SETUP & TESTS")
    print("="*60)
    
    success = run_command(
        "python setup_and_test.py",
        "Running Setup & Verification Tests"
    )
    
    if success:
        print("\n" + "="*60)
        print("✅ ALL SYSTEMS GO!")
        print("="*60)
        print("\n🎉 NEURON is ready to use!\n")
        print("📚 Next Steps:")
        print("   1. python examples/chatbot_example.py")
        print("   2. python examples/agent_example.py")
        print("   3. python examples/code_gen_example.py")
        print("\n📖 Or read: QUICKSTART.md\n")
    else:
        print("\n❌ Setup failed. Check errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
