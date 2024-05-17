# Microservice Documentation

## Communication Contract

### Request Data

The microservice reads from `programs_to_run.txt` and executes each command listed. An example command that can be given to the microservice is as follows
```sh
py thingThatNeedsExecuting.py
```
To formally call this microservice from another python application, it is recommended to approach as follows.

```sh
import subprocess

# Create the programs_to_run.txt file
programs = [
    "py applicationToRun.py",
]

with open('programs_to_run.txt', 'w') as file:
    for program in programs:
        file.write(f"{program}\n")

# Run the microservice
subprocess.run(['python', 'microService.py'])
```

Once running, the microservice will execute each command listed in the `programs_to_run.txt` file.

### Receive Data

Data from the microservice can be observed in the form of commands being removed from the `programs_to_run.txt`.
Succesful operations are noted in the terminal by the microservice.
The user is responsible for handling Data proccessed by commands executed by the microservice. An example of using the `programs_to_run.txt` to evaluate data might be as follows.
```sh
while True:
    time.sleep(1)

    with open('programs_to_run.txt', 'r') as file:
        lines = file.readlines()

    if not lines:
        print("The MicroService is Done!")
        break
```
In this example, once the microservice has been called we wait on the .txt file to be fully empty before continuing with our application.

### UML Sequence Diagram

![CadeMicroservice](https://github.com/ThomaDevOSU/CadeMicroservice/assets/166056408/92df0f8d-cdfb-4dd0-855f-49896ca3e892)
