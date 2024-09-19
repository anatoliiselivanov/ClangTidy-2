import subprocess
import os

def get_changed_files():
    # Get list of changed files
    result = subprocess.run(['git', 'diff', '--name-only', '--cached'], 
                            stdout=subprocess.PIPE, text=True)
    files = result.stdout.strip().split('\n')
    
    # Check only C/C++ files
    changed_files = [f for f in files if f.endswith(('.c', '.cpp', '.h'))]
    
    return changed_files

def run_clang_tidy(files):
    for file in files:
        print(f"Running Clang-Tidy on {file}")
        result = subprocess.run(['clang-tidy', file, '--config-file=.clang-tidy'],
                                stdout=subprocess.PIPE, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"Clang-Tidy check failed for {file}")
            return False
    return True

def main():
    changed_files = get_changed_files()
    
    if not changed_files:
        print("No changed files to check.")
        return

    success = run_clang_tidy(changed_files)
    
    if not success:
        print("Clang-Tidy checks failed.")
        exit(1) 

if __name__ == "__main__":
    main()
