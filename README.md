# Course materials for the 2024/2025 edition of Basics of Machine Learning (Podstawy Uczenia Maszynowego) 
## Taught at the Faculty of Chemistry, Jagiellonian University in Kraków

```
,-.----.                             ____                                     ,--,
\    /  \                          ,'  , `.                  ,----,         ,--.'|
|   :    \           ,--,       ,-+-,.' _ |                .'   .' \     ,--,  | :
|   |  .\ :        ,'_ /|    ,-+-. ;   , ||     ,---,.   ,----,'    | ,---.'|  : '
.   :  |: |   .--. |  | :   ,--.'|'   |  ;|   ,'  .' |   |    :  .  ; ;   : |  | ;
|   |   \ : ,'_ /| :  . |  |   |  ,', |  ': ,---.'   ,   ;    |.'  /  |   | : _' |
|   : .   / |  ' | |  . .  |   | /  | |  || |   |    |   `----'/  ;   :   : |.'  |
;   | |`-'  |  | ' |  | |  '   | :  | :  |, :   :  .'      /  ;  /    |   ' '  ; :
|   | ;     :  | | :  ' ;  ;   . |  ; |--'  :   |.'       ;  /  /-,   \   \  .'. |
:   ' |     |  ; ' |  | '  |   : |  | ,     `---'        /  /  /.`|    `---`:  | '
:   : :     :  | : ;  ; |  |   : '  |/                 ./__;      :         '  ; |
|   | :     '  :  `--'   \ ;   | |`-'                  |   :    .'          |  : ;
`---'.|     :  ,      .-./ |   ;/                      ;   | .'             '  ,/ 
  `---`      `--`----'     '---'                       `---'                '--'          
```

## Table of contents
* Lab 1 - Python basics. Conway's Game of Life.
* Lab 2 - Classes and objects in Python. Linear Regression in NumPy.
* Lab 3 - Introduction to `pandas` and `seaborn`. Building a classifier model with `scikit-learn`.
* Lab 4 - Data preprocessing. Building a regression model. Coding a simple app in Streamlit.
* Lab 5 - Introduction to neural networks with PyTorch.
* Lab 6 - Visualizing the training process of neural networks and hyperparameter tuning.
* Lab 7 - Generative models. Variational Autoencoder.

## Course info
During the semester you will have to complete a series of seven laboratory sessions. 
The course material is divided into notebooks, each dedicated to a specific topic.

A notebook is divided into exercises, each of which is worth a certain number of points. The maximum number of points you
can earn at each laboratory session is 10, making it a total of 70 points from the whole course.
At the end of the semester, the points from all notebooks will be summed up and converted into the final grade according 
to the following scale:

* 35 - 41 points: 3.0
* 42 - 48 points: 3.5
* 49 - 55 points: 4.0
* 56 - 62 points: 4.5
* 63 - 70 points: 5.0

The exercises preceded by a star (*) are not graded, but they introduce some fun concepts or more advanced topics. 
Solving them can sometimes earn you additional points. The information about the extra points will be included 
in the exercise description or announced during the laboratory session.

You need to get at least 35 points to pass the course. During each laboratory session, you can earn additional points
by solving extracurricular problems, actively participating in the class, and contributing to the course in other ways. 
The maximum number of additional points you can earn during the course is 10.

The course is taught in Polish, but the course materials are in English so that you can get accustomed to the ML-related
terminology and use it in your future work.

<br>

## Setup

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) following the instructions for your operating
   system.
2. Clone the repository: `git clone https://github.com/hubertrybka/pum-24.git`
3. Navigate to the directory: `cd pum-24`
4. Download datasets from our [dropbox](https://www.dropbox.com/scl/fi/50mnh2dfdr2wgddkwo512/pum24-datasets.zip?rlkey=2woga4c850qivsjwihqmqnpd0&st=vlrg3at6&dl=1) and extract them to `data` directory.
5. Install environment from the YAML file: `conda env create -n pum-24 -f environment.yml`
6. Activate the environment: `conda activate pum-24`


Author: Hubert Rybka
