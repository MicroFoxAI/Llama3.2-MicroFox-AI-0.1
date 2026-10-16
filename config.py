# MicroFox AI Configuration File
# Target Architecture: Llama-3.2
# Compatibility: Designed for local mode runtime deployment

# Security Credentials
TOKEN = "YOUR_HUGGINGFACE_API_TOKEN_HERE"

# Core Model Behavior
SYSTEM_PROMPT = """You are MicroFox, a highly optimized, agile, and intelligent AI assistant. 
You provide precise, efficient, and direct answers while maintaining a helpful and professional tone."""

# Runtime Optimization Settings
MODEL_TARGET = "meta-llama/Llama-3.2-3B-Instruct"
LOCAL_MODE_RELOAD_FIX = True
MAX_SEQUENCE_LENGTH = 2048
