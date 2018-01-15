"""
Reusable functions for the cars project
"""

def save_matplotlib_fig(fig, filename, save_dir):
    """
    Saves matplot figure to specified path with given file name

    Inputs:
    -fig: matplotlib figure object to save
    -filename: Desired filename including extension. i.e: 'image.png'
    -save_dir: path to directory in which the image is to be saved

    Output:
    -Figure is saved in specified directory
    """
    import os

    save_image_path = os.path.join(save_dir, filename)
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    fig.savefig(save_image_path)


def pickle_variable_to_path(variable, filename, save_dir):
    """
    Pickles variable to specified path with given file name

    Inputs:
    -variable: variable to save. Must be pickle-able
    -filename: Desired filename WITHOUT extension. i.e: 'variable'
    -save_dir: path to directory in which the image is to be saved

    Output:
    -Variable is pickled in specified directory with specified name
    """
    import os
    import pickle

    # Exit if file already exists
    file_path = os.path.join(save_dir, filename+'.pkl')
    if os.path.isfile(file_path):
        return print('\n********** pickle file already exists **********\n')

    # Check if save directory already exists, if it doesn't make it
    if not os.path.isdir(save_dir):
        try:
            os.makedirs(save_dir)
        except Exception as expt:
            print(expt)

    with open(file_path, 'wb') as file:
        pickle.dump(variable, file)

def display_add_train_time(start_time, end_time, history_dicto):
    """ TODO """
    train_time_seconds = round(end_time - start_time, 0)
    train_time_minutes = round(train_time_seconds/60, 0)
    history_dicto['train_time_seconds'] = train_time_seconds
    history_dicto['train_time_minutes'] = train_time_minutes
    return print('traing took: {} minutes' .format(train_time_minutes))


def save_model_and_history(model, history_dicto, filename, save_dir):
    """ TODO """
    import os

    h5_file_path = os.path.join(save_dir, filename + '.h5')

    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    if not os.path.isfile(h5_file_path):
        model.save_weights(h5_file_path)
    else:
        return print(
            '\n********** h5 file already exists **********\n pickle file not saved'
        )

    pickle_variable_to_path(history_dicto, filename, save_dir)

def time_save_model(model, history_dicto, start_time, end_time, filename, save_dir):
    """
    combines display_add_train_time and save_model_and_history into a single function
    """
    display_add_train_time(start_time, end_time, history_dicto)
    save_model_and_history(model, history_dicto, filename, save_dir)

def plot_metrics(history_dicto, key_list, fig_size=(10, 25)):
    """
    Plots training and validation metrics found in history_dicto
    and specified in key_list into Jupyter Notebook

    Inputs:
    -history_dicto: dictionary attached to history object output by keras fit methods
    -key_list: list of strings with key names to plot. DOES NOT INCLUDE 'val_metric' keys
               Those are generated automatically
    -fig_size: tuple with (width, height) in inches. default: (10, 25)

    Output:
    plot of figure in Jupyter notebook
    """
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(len(key_list), 1)
    fig.set_size_inches(fig_size)
    axes = axes.reshape(-1)

    for i, key in enumerate(key_list):
        dependent = history_dicto.get(key)
        epochs = range(1, 1 + len(dependent))
        val_dependent = history_dicto.get('val_' + key)
        assert len(dependent) == len(val_dependent),\
        'validation and train sets do not match'

        try:
            axes[i].plot(epochs, dependent, label='Training {}'.format(key))
            axes[i].plot(epochs, val_dependent, label='Validation {}'.format(key))
            axes[i].set_title('Training and validation {}'.format(key))
            axes[i].set_ylabel(key)
            axes[i].set_xlabel('epochs')
            axes[i].legend()
        except Exception as expt:
            print(expt)

    return plt.show()
