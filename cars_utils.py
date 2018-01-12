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
