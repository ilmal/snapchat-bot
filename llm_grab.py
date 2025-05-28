import os
import datetime
from pathlib import Path

def collect_project_info(root_dir, output_file="project_context.txt"):
    """
    Traverses a project directory, collects file structure and contents of relevant files,
    and saves them to an output file for LLM context.
    
    Args:
        root_dir (str): Root directory of the project
        output_file (str): Name of the output file to save the context
    """
    # Define relevant file extensions
    relevant_extensions = ('.py', '.txt', '.md', '.gitignore', '.yml', '.yaml', '.json')
    docker_files = ['Dockerfile', 'docker-compose.yml', 'docker-compose.yaml']

    
    # Initialize content to write
    output_content = []
    
    # Add header with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_content.append(f"# Project Context\nGenerated on: {timestamp}\n")
    
    # Get project root name
    project_name = os.path.basename(os.path.abspath(root_dir))
    output_content.append(f"Project Name: {project_name}\n")
    
    # Collect file tree
    output_content.append("\n## Project File Structure\n")
    for root, dirs, files in sorted(os.walk(root_dir)):
        # Skip virtual environment and cache directories
        if any(ignore_dir in root for ignore_dir in ['venv', '.venv', '__pycache__', '.git']):
            continue
            
        # Calculate relative path and depth for tree visualization
        rel_path = os.path.relpath(root, root_dir)
        depth = rel_path.count(os.sep) if rel_path != '.' else 0
        indent = '  ' * depth
        
        # Add directory to tree
        if rel_path != '.':
            output_content.append(f"{indent}├── {os.path.basename(root)}/")
        
        # Add files in this directory
        for file in sorted(files):
            if any(ignore_dir in file for ignore_dir in ['.pyc', '.log']):
                continue
            output_content.append(f"{indent}│   ├── {file}")
    
    # Collect file contents
    output_content.append("\n## File Contents\n")
    
    for root, _, files in sorted(os.walk(root_dir)):
        # Skip ignored directories
        if any(ignore_dir in root for ignore_dir in ['venv', '.venv', '__pycache__', '.git']):
            continue
            
        for file in sorted(files):
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, root_dir)
            
            # Process only relevant files, including Docker-related files
            if not (file.endswith(relevant_extensions) or not file in docker_files):
                continue


                
            if any(ignore_dir in file for ignore_dir in ['.pyc', '.log']):
                continue
                
            output_content.append(f"\n### {rel_path}\n")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    output_content.append("```" + 
                        (file.endswith('.py') and 'python' or 
                         file.endswith(('.yml', '.yaml')) and 'yaml' or 
                         file.endswith('.json') and 'json' or 
                         'text') + "\n")
                    output_content.append(content)
                    output_content.append("\n```")
            except Exception as e:
                output_content.append(f"Error reading file: {str(e)}\n")
    
    # Write to output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(output_content))
        print(f"Project context saved to {output_file}")
    except Exception as e:
        print(f"Error writing output file: {str(e)}")

if __name__ == "__main__":
    # Use current directory as default, or specify your project directory
    project_directory = "."  # Change this to your project directory if needed
    collect_project_info(project_directory)