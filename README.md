This notebook contains step-by-step development and walkthough of fake news classification using Convolutional Neural Network, Deep Neural Network, and Long Short-Term Memory (Recurrent Neural Network) architecture. It includes the end-to-end design that covers the 6Ds of creating AI-enabled systems. It also includes a Docker deployment and a detailed step-by-step analysis of process.

========================================================================================

Instruction for downloading Dataset


========================================================================================

Instruction of Deploying and running Flask server.

1. Pull the docker image from following repo https://hub.docker.com/repository/docker/pjdocker101/fakenewsclassification

2. We need 2 terminals to connect to the same container where one terminal will run flask server and ther other will run user_control.py

3. Terminal 1: Connect to the imagge using the following command: This will allow you to start a container and basn into it.
    Command: docker run -it --entrypoint bash pjdocker101/fakenewsclassification:3.1
    
4. Terminal 1: left side of the cursor you will see root@CONTAINER_ID: Copy the container id from your terminal 1
    Example: root@11629d863a80:/#  Copied:11629d863a80

5. Terminal 2: Connect to the same container as terminal 1 using the following command. Replace the earlier copied above.
    Command: docker exec -it CONTAINER_ID bash
    Example: docker exec -it 11629d863a80 bash
    
6. Wait for it to load.

7. Terminal 1: Run the following command to run user_control.py
    Command:  python user_control.py
    
8. Terminal 2: Run the Following gommands to start Flask server
    Command 1: cd FlaskServer
    Command 2: python server.py
    
9. Now go back to Terminal 1 and make a choise to connect to server or make and POST call to pass in the article.


*NOTE* - Currently The API is only accesible inside the container, but the port can be exposed to allow the host to make API calls from outside the container.

========================================================================================

You can also use the jupyter lab to run the notebook inside the container which will also allow you to make API calls using the example client provided in the jupyter notebook.

========================================================================================

    
