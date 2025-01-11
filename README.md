<<<<<<< HEAD
# dragon_data
=======
# Dragon Dataset
![Dragon Dataset](resources/title_image.png)

## Getting the dataset
To get the dataset, you'll first have to download the images. There's only about 100 of them, so this won't take long. The links to all the images are in the `annotations` folder, but can automatically be downloaded by using the `get_dataset.py` script. This script will create a folder called `data` with 2 additional folders inside: `train` and `val` containing all the training and validation images respectively.
```
pip install -r requirements.txt
python get_dataset.py
```

## Visualising the dataset
Once you have the images downloaded, we can use the `visualise_annotations.ipynb` notebook to take a look at the annotations using the FiftyOne tool from Voxel51.

## Storing the dataset as a clearML versioned dataset
In order to use this dataset in your other projects, it's a good idea to version track it. This way you can easily get a local copy from anywhere, but also keep track of any changes that might be done to it in the future. This will play nicely with clearML experiment tracking, making sure you know on which data you trained which models. Now you can always recreate your experiments exactly no matter how many times the dataset changes.

Storing the images in a clearML dataset is easy.
You can either use the notebook `create_clearml_dataset.ipynb` which uses the Pyhton SDK to manage the dataset.

Or using the CLI tool you can simply do:

```
# Initialize clearml if not already done so.
# This will ask the details about your clearml server to store the data on.
# If you don't have any yet, checkout the free community server
# or host one yourself with docker-compose!
clearml-init

# Create the dataset, this will return a dataset ID. Copy it because we will need it later.
clearml-data create --project <PROJECT_NAME> --name <DATASET_NAME>

# Add the data and annotations
# Note the dataset-folder argument we use here to keep the data in the same filestructure as on the disk
clearml-data add --id <DATASET_ID> --dataset-folder data/train --files data/train
clearml-data add --id <DATASET_ID> --dataset-folder data/val --files data/val
clearml-data add --id <DATASET_ID> --dataset-folder annotations --files annotations

# We can quickly check if all files are added correctly
clearml-data list

# And then upload the files and finalise the dataset
clearml-data close --id <DATASET_ID>
```
>>>>>>> aa1d073 (add)
