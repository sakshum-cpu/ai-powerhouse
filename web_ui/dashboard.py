"""Web UI Dashboard for NEURON AI Powerhouse"""
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from threading import Thread
import asyncio
from chatbot.chatbot import Chatbot
from agent.agent import Agent
from code_generator.generator import CodeGenerator
from config import settings
from utils.logger import get_logger

logger = get_logger(__name__)

app = Flask(__name__)
CORS(app)

# Initialize AI components
chatbot = Chatbot(name="NEURON")
agent = Agent(name="TaskMaster")
code_gen = CodeGenerator()

# Store active sessions
sessions = {}


@app.route("/", methods=["GET"])
def index():
    """Serve dashboard"""
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """Chat endpoint with streaming response"""
    data = request.json
    message = data.get("message", "")
    session_id = data.get("session_id", "default")
    
    if not message:
        return jsonify({"error": "Message required"}), 400
    
    try:
        response = chatbot.chat(message)
        return jsonify({
            "success": True,
            "response": response,
            "session_id": session_id,
            "timestamp": str(datetime.now())
        })
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/agent/execute", methods=["POST"])
def execute_task():
    """Execute agent task with progress streaming"""
    data = request.json
    task = data.get("task", "")
    
    if not task:
        return jsonify({"error": "Task required"}), 400
    
    try:
        result = agent.execute_task(task)
        return jsonify({
            "success": True,
            "result": result,
            "timestamp": str(datetime.now())
        })
    except Exception as e:
        logger.error(f"Task execution error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/generate-code", methods=["POST"])
def generate_code():
    """Generate code with validation"""
    data = request.json
    description = data.get("description", "")
    language = data.get("language", "python")
    
    if not description:
        return jsonify({"error": "Description required"}), 400
    
    try:
        result = code_gen.generate(description, language)
        return jsonify({
            "success": True,
            "code": result["code"],
            "language": language,
            "timestamp": str(datetime.now())
        })
    except Exception as e:
        logger.error(f"Code generation error: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/api/history/chat", methods=["GET"])
def get_chat_history():
    """Get chat history"""
    try:
        history = chatbot.get_history()
        return jsonify({"success": True, "history": history})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/history/agent", methods=["GET"])
def get_agent_history():
    """Get agent execution history"""
    try:
        history = agent.get_history()
        return jsonify({"success": True, "history": history})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/clear-chat", methods=["POST"])
def clear_chat():
    """Clear chat history"""
    try:
        chatbot.clear_history()
        return jsonify({"success": True, "message": "Chat history cleared"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/stats", methods=["GET"])
def get_stats():
    """Get system statistics"""
    try:
        return jsonify({
            "success": True,
            "chatbot": chatbot.get_stats(),
            "agent_executions": len(agent.get_history()),
            "code_generations": len(code_gen.get_history()),
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "app_name": settings.app_name,
        "model": settings.llm_model
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
