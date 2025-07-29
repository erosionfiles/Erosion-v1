"""
EROSION CORE v1.0
A 100% English Python-based language for beginners
"""

import re

def translate(erosion_code):
    """Translates Erosion code to Python"""
    # Convert PRINT statements
    erosion_code = re.sub(r'PRINT\s+"([^"]+)"', r'print("\1")', erosion_code)
    erosion_code = re.sub(r'PRINT\s+([^"]\S+)', r'print(\1)', erosion_code)
    
    # Convert AND to string concatenation
    erosion_code = erosion_code.replace(' AND ', ' + " " + ')
    
    # Convert SET statements
    erosion_code = re.sub(r'SET\s+(\w+)\s+TO\s+(.+)', r'\1 = \2', erosion_code)
    
    # Convert SHOW IF ELSE
    erosion_code = re.sub(
        r'SHOW\s+"([^"]+)"\s+IF\s+(.+)\s+ELSE\s+SHOW\s+"([^"]+)"',
        r'print("\1" if \2 else "\3")',
        erosion_code
    )
    
    # Convert bare SHOW to PRINT
    erosion_code = erosion_code.replace('SHOW ', 'print(') + ')' * erosion_code.count('SHOW ')
    
    return erosion_code

def run_erosion(erosion_code):
    """Executes Erosion code"""
    try:
        python_code = translate(erosion_code)
        exec(python_code, globals())
    except Exception as e:
        print(f"Erosion Error: {str(e)}")

# Example usage (will run when imported)
if __name__ == "__main__":
    sample_code = """
    PRINT "Welcome to Erosion!"
    SET name TO "'Alice'"
    PRINT "Hello" AND name
    SET age TO 25
    SHOW "Adult" IF age >= 18 ELSE SHOW "Child"
    """
    run_erosion(sample_code)