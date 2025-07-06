#!/usr/bin/env python3
"""
Import test for all required modules
"""

def test_imports():
    """Test all imports used in the project"""
    
    try:
        print("Testing basic imports...")
        import os
        import sys
        import logging
        print("✓ Basic imports successful")
        
        print("\nTesting blinker...")
        import blinker
        print(f"✓ blinker imported successfully - version: {blinker.__version__}")
        
        print("\nTesting streamlit...")
        import streamlit as st
        print(f"✓ streamlit imported successfully - version: {st.__version__}")
        
        print("\nTesting dotenv...")
        from dotenv import load_dotenv
        print("✓ dotenv imported successfully")
        
        print("\nTesting constants...")
        import constants as ct
        print(f"✓ constants imported successfully - RAG_RETRIEVER_K: {ct.RAG_RETRIEVER_K}")
        
        print("\nTesting initialize...")
        import initialize
        print("✓ initialize imported successfully")
        
        print("\nTesting utils...")
        import utils
        print("✓ utils imported successfully")
        
        print("\nTesting main...")
        import main
        print("✓ main imported successfully")
        
        print("\n🎉 All imports successful!")
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_imports()
