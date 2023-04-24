# Boston House Price Prediction - Linear Reggression

## Software And tools Requirements

1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Heroku Account](https://heroku.com)
4. [Git CLI](https://git-scm.com/downloads)


Create a new enviornment
```
conda -p venv python==3.7 -y
```

Create a new ```requirements.txt``` file and write down all the libraries you need to install over there
```
Flask
scikit-learn
numpy
pandas
matplotlib
seaborn
```
install these libraries in bulk using command prompt
```
pip install -r requirements.txt
```
## Configuring the Git
Git CLI is used to push our code into our github repository.
We need to configure the user name
```
git config --global user.name "Musthakh Ahammed"
```
Alos we need to configure the email. The email should be same as the one we created the github account
```
git config --global user.email "yourmail@gmail.com"
```
In case of password, it will ask at the beginning once we try pushing. We can enter the password at that time and that will be automatic at the next time we push.

The ```.gitignore``` file is to spcify any files or folders we don't need to push into repository. 

To add a file into
```
git add requirements.txt
```
To check the status
```
git status
```
To add all the files
```
git add .
```
The next step is to commit the files. 
Commit does that from our local pushes into the staging enviornment.

Always check [Atlassian tutorial](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) to undertand more about the commit.

We are going to use the below code to commit. Because, we need to add a message along with the commit.
```
git commit -m "commit message"
```
The next step is to push from staging enviornment into Github.
```
git push origin main
```
This will push from origin to main branch. The origin is the branch where we will commit into. 

This will ask to enter the password. We can just enter at this time and no worries.
<br />
<br />
<br />
<br />
To recap, we use mainly 3 steps.
1. Adding all files: - Adds a change in the working directory to the staging area
``` 
git add .
 ```
2. Commit the changes: - Commit a snapshot of all changes in the working directory.
```
git commit -m "Commit message"
```
3. Push everything form origin branch to main
```
git push origin main
```


Now we can check our Github repository to see the changes
<br />
<br />

## Building the Front-End Application

Create a new folder called ```templates```. inside that, create the HTML page. For demo purpose just create a simple 'hello world' webpage.

Create a new file called ```app.py```.

Run the ```app.py```. Click on the URLto open in browser.

Test the predict_api is working using Postman. Use the below JSON format to test.
```
{
    "data": {
        "CRIM": 0.00632,
        "ZN": 18.0,
        "INDUS": 2.31,
        "CHAS": 0.0,
        "NOX": 0.538,
        "RM": 6.575,
        "AGE": 65.2,
        "DIS": 4.0900,
        "RAD": 1.0,
        "TAX": 296.0,
        "PTRATIO": 15.3,
        "B": 396.90,
        "LSTAT": 4.98
    }
}
```
Create the ```homne.html``` and also make changes in ```app.py``` and check it is working.