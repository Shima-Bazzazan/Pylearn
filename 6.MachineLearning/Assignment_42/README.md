# KNN applied to the ANSUR II dataset

The ANSUR II dataset (The Anthropometric Survey of US Army Personnel) is related to an anthropometric study conducted on the measurements and physical dimensions of U.S. Army personnel. This dataset contains detailed information about body sizes and shapes, collected with the aim of improving the design of equipment, uniforms, and work environments for military personnel.

## How to Install
Run following command:
```
pip install -r requirements.txt
```

## Results

<img src="outputs\stature_and_weigths.png" width="571">

<img src="outputs\height.png" width="507">

### Accuracy results for different amounts of k:

|  Features |  k = 3  |  k = 5  |  k = 7 |
|---------------| --------------- | --------------- | --------------- |
|stature, weight|  0.8303   | 0.8459  | 0.8443  |
|stature, weight, biacromial breadth |  0.9168   | 0.9168  | 0.9168 |
|stature , weight, biacromial breadth, shouldercircumference|  0.9505  | 0.9538  | 0.9530  |

### How to Run
Execute this command in terminal:
```
jupyter notebook kNN_ANSUR_II_4features.ipynb
```
