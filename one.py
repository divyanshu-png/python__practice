def func():
    print("func() in one.py is invoked")
print("Top level in one.py")

if __name__=="__main__":
    print("ONE.PY is being run directly")
else:
    print("ONE.PY is being imported")
#you either run directly or import the file in another file

# if __name__ == "__main__": in Python acts as a conditional guard, ensuring specific code runs only when a script is executed directly, not when imported as a module. It sets up a main entry point for code execution, allowing files to be reused in other projects without executing unwanted code, such as tests or initialization scripts. 

# Why Use if __name__ == "__main__":?
# 1. Prevent Unwanted Execution: Without it, any code outside functions runs immediately upon importing a module.
# 2. Modular Reusability: It allows you to use functions/classes from a file without running the entire script.
# 3. Entry Point Definition: It defines a clear starting point (main) for your application. 

# How It Works
# Direct Running: When you run a script (python script.py), Python sets the special variable __name__ to __main__, causing the block to run.
# Importing: When you import a file (import script), Python sets __name__ to the filename (module name), so the block is skipped.

#Yes, if you import a Python file that does not have the if __name__ == "__main__": conditional check, all top-level code(all execcutable code in the file above the conditon) in that file will run immediately upon import

