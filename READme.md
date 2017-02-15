## Receipt.ID

About
=====

Receipt.ID is a multi-label, multi-class, hierarchical classification system implemented in a two layer feed forward network. It trains individual AdaBoost text-based classifiers and combines the result with other features. Receipt.ID is built to scale with an application as the taxonomy for the domain in which it is applied grows. 

Dependencies
------------

Receipt.id is tested to work under Python 2.7 and Python 3

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [Scikit-learn](http://scikit-learn.org/stable/)


Code
=====

The data preprocessing code is provided in the notebook `receiptID_1_Data_Preprocessing.ipynb`. While the modeling code is provided in the notebook `receiptID_2_Model.ipynb`.

To open it, go to the top-level project directory `receiptID/` and start the notebook server:

```jupyter notebook```

This should open a web browser to the server's dashboard (typically `http://127.0.0.1:8888`). Click on the appropriate notebook (`.ipynb`) to open it, and follow the instructions.

Run
=====

To run a code cell in the notebook, hit `Shift+Enter`. Any output will be displayed below the corresponding cell.

You can also add/edit markdown text cells and render them using `Shift+Enter`.

