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
* Lab 3 - Exploratory data analysis. Dataset manipulations. Building a regression model.
* Lab 4 - Binary classification. Clustering and unsupervised learning.
* Lab 5 - Introduction to neural networks with PyTorch.
* Lab 6 - Managing the training process of neural networks with W&B.
* Lab 7 - Generative models. Variational Autoencoder.
---

## Quick introduction to the Python random module

The Python standard library includes a module called `random` that provides functions for generating pseudorandom numbers. To complete the exercises in this notebook, you may want to learn the following functions:


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

The exercises preceded by a star (*) are not graded, but they will help you to better understand the material
or are just fun to do.

You need to get at least 35 points to pass the course.
The final marks will be increased by 0.5 for active participation in laboratory classes or other forms of
contribution to the course.

The course is taught in Polish, but the course materials are in English so that you can get accustomed to the ML-related
terminology and use it in your future work.

<br>

## Setup

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) following the instructions for your operating
   system.
2. Clone the repository: `git clone https://github.com/hubertrybka/pum-24.git`
3. Navigate to the directory: `cd pum-24`
4. Install environment from the YAML file: `conda env create -n pum-24 -f environment.yml`
5. Activate the environment: `conda activate pum-24`


Author: Hubert Rybka
