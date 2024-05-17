import subprocess

def run_microservice(file_path):
    while True:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if not lines:
            print("No more programs to run. Exiting microservice.")
            break

        # Get the first program to run
        program_to_run = lines[0].strip()

        # Call the program as a subprocess
        print(f"Starting {program_to_run}")
        try:
            subprocess.run(program_to_run, check=True)
            print(f"Completed {program_to_run}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running {program_to_run}: {e}")

        # Remove the first line and update the file
        with open(file_path, 'w') as file:
            file.writelines(lines[1:])

if __name__ == "__main__":
    file_path = 'programs_to_run.txt'  # The file containing the names of programs to run
    run_microservice(file_path)
