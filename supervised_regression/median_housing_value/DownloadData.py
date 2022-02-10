import os
import pandas as pd
import tarfile
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
        print(f"Creating {housing_path}")
    tgz_path = os.path.join(housing_path, "housing.tgz")
    print(f"Downloading data from {housing_url}...")
    urllib.request.urlretrieve(housing_url, tgz_path)
    print(f"Opening tar file...")
    housing_tgz = tarfile.open(tgz_path)
    print(f"Extracting data...")
    housing_tgz.extractall(path=housing_path)
    print(f"Done.")
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def main():
    fetch_housing_data()
    data = load_housing_data()


if __name__ == '__main__':
    main()
