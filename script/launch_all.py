import subprocess
import os 

path = os.path.dirname(os.path.abspath(__file__))
join = os.path.join

homepage_script = join(path, 'homepage.py')
bureau_script = join(path, 'bureau.py')
event_script = join(path, 'event.py')


def run_script(script_path):
    try:
        subprocess.run(['python3', script_path], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path}: {e.stderr}")


run_script(homepage_script)


run_script(bureau_script)


run_script(event_script)

print("All scripts executed successfully!")
