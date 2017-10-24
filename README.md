# Skeleton

A skeleton set of files to help accelerate development on Python pet projects.

The best way to start a new project using this repository is to do the following:
```
git clone --bare git@github.com:benhoyle/skeleton_proj.git
cd skeleton_proj.git
```
Then setup a new repository on GitHub for your new project. Then run:
```
git push --mirror git@github.com:[your_name]/[your_new_project].git
rm -rf skeleton_proj.git
git clone git@github.com:[your_name]/[your_new_project].git
```

The ```core.py``` file holds the main classes and functions. 

Generic helper functions are found in (and are added to) ```helper.py```.

Database models for SQLAlchemy are found in ```models.py```.

The ```webserver.py``` file holds a basic Flask webserver for the frontend.

To start the webserver that implements the user interface run - 
```
python -m skeleton.webserver
```
and point your browser to:
```
localhost:3000
```

Remember to edit the data in ```setup.py```.

Once started you can install by cd-ing to the project directory and running:
```
pip install .
```

Library for [doing stuff].


