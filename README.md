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

To add a file into github repository
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