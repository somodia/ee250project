Team Members: Alexandra Somodi and Victoria Nunez
GitHub link: https://github.com/somodia/ee250project/tree/main/project/ee250/project
To Use DaBaby Monitor:
Step ONE: 
    Connect all hardware components to Rpi and ssh into your RPi through your VM
Step TWO: 
    Start the Flask Web Interface on your VM: 
Installation Instructions for Flask Web InterFace:
# https://dev.to/terieyenike/creating-apis-with-flask-and-testing-in-postman-2ojn
# link to how to run flask api

# We have to create a virtual environment
# Step 1: Install Python: If you don't already have Python installed, download and install it from python.org.
# Step 2: In a new terminal, where you would want the environment folder located, run python -m venv <name-of-project>
# Step 3: Next, navigate to the project directory to activate the virtual environment.
        ## To be sure you are referencing the right shell, check out 
        # https://docs.python.org/3/library/venv.html#how-venvs-work 
        # for the command based on your shell.
            # I have windows so it was 	
            # C:\> EE250Project\Scripts\activate.bat
# Step 4: After activation, your command prompt will show the name of the environment, indicating that you are 
    # working within it.
        ## (flask-apis) (base)  ✝  ~/Desktop/flask-apis 
# Step 5: Next run pip install flask
        ## confirm installation by running: pip show flask
# Step 6: pip install paho-mqtt
# Step 7: Move the flask_api python script into the virtual environment folder
# Step 8: flask --app app --debug run
        ## app: is the name of the file that contains the application code. 
        # If you named the file hello.py, you must replace app with hello
            # flask --app hello --debug run
# Step 9: Terminal should output something similar to this:
    # Serving Flask app 'app'
    #  * Debug mode: on
    # WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    #  * Running on http://127.0.0.1:5000
    # Press CTRL+C to quit
    #  * Restarting with stat
    #  * Debugger is active!
    #  * Debugger PIN: 100-724-825
# Step 10: Click on the link in the above output!

Step THREE: 
    Open 2 more seperate terminals and run VMSubscriber.py in one and VMPublisher.py in the other
Step FOUR: 
    In the terminal in which you ssh'd into your RPi, run RPIPubSub.py

Step FIVE: 
    ENJOY THE DaBaby Monitor!!
