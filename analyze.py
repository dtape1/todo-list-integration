import ast
 
def analyze(filename):
    with open(filename, encoding="utf-8") as f:
        source = f.read()
 
    tree = ast.parse(source)
    print(f"=== {filename} ===")
 
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if not ast.get_docstring(node):
                kind = "Клас" if isinstance(node, ast.ClassDef) else "Функція/метод"
                print(f"  {kind} '{node.name}' — відсутній docstring (рядок {node.lineno})")
 
    print()
 
analyze("task_manager.py")
analyze("main.py")
 