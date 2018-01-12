"""
Reusable functions for the cars project
"""

def save_matplotlib_fig(fig, file_name, save_dir):
    """
    Saves matplot figure to specified path with given file name

    Inputs:
    -fig: matplotlib figure object to save
    -file_name: Desired filename including extension. i.e: 'image.png'
    -save_dir: path to directory in which the image is to be saved

    Output:
    -Figure is saved in specified directory
    """
    import os

    save_image_path = os.path.join(save_dir, file_name)
    fig.savefig(save_image_path)


def pickle_variable_to_path(variable, file_name, save_dir):
    """
    Pickles variable to specified path with given file name

    Inputs:
    -variable: variable to save. Must be pickle-able
    -file_name: Desired filename including extension. i.e: 'variable.pkl'
    -save_dir: path to directory in which the image is to be saved

    Output:
    -Variable is pickled in specified directory with specified name
    """
    import os
    import pickle

    # Exit if file already exists
    file_path = os.path.join(save_dir, file_name)
    if os.path.isfile(file_path):
        return print('file already exists')

    # Check if save directory already exists, if it doesn't make it
    if not os.path.isdir(save_dir):
        try:
            os.makedirs(save_dir)
        except Exception as expt:
            print(expt)

    with open(file_path, 'wb') as file:
        pickle.dump(variable, file)
   