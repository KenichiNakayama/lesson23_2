#!/usr/bin/env python3
"""
Streamlitアプリのデバッグテスト用スクリプト
"""

print("=== Streamlit App Debug Test ===")

try:
    print("1. Importing basic libraries...")
    import os
    import logging
    from dotenv import load_dotenv
    print("✓ Basic libraries imported")
    
    print("2. Loading environment variables...")
    load_dotenv()
    print("✓ Environment loaded")
    
    print("3. Importing streamlit...")
    import streamlit as st
    print("✓ Streamlit imported")
    
    print("4. Importing custom modules...")
    import constants as ct
    print(f"✓ Constants imported - RAG_CHUNK_SIZE: {ct.RAG_CHUNK_SIZE}")
    
    import utils
    print("✓ Utils imported")
    
    import components as cn
    print("✓ Components imported")
    
    from initialize import initialize
    print("✓ Initialize imported")
    
    print("5. Testing initialize function...")
    # initialize()
    print("✓ Initialize function ready (not executed)")
    
    print("\n=== All imports successful! ===")
    
except Exception as e:
    print(f"❌ Error occurred: {e}")
    import traceback
    traceback.print_exc()
