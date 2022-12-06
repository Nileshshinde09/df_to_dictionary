from setuptools import setup
setup(name="df_to_dictionary"
,version="0.2"
,long_description_content_type='text/markdown',
long_description=
"""
    % This is module of convert dataframe to dictionary in river dataset format %

    River is the famous online machine learning dictionary in python but it can only support dictionary as a input. For that reason we have to convert dataframe to dictionary.

    WHY DataFrame
    In this situation you might be thinking whay first we convert other formate to dataframe and then dictionary ,because pandas gives us some amazing feature for data visualization.
    For more info
    https://pandas.pydata.org/

    Function in this module

    xdata,ydata = df_to_dictionary(x_data,y_data)

    here x_data means the fetures and y_data means the labels of the dataset.
    It will returns transformed xdata and ydata


    Installation :
        Requirements:
    pandas
    numpy
    Installation :
        pip install pandas==1.5.2
        pip install numpy==1.23.5
    

    Github link
        https://github.com/Nileshshinde09/df_to_dictionary
""",
author="Nilesh Shinde",
packages=['df_to_dictionary'],
install_requires=["numpy==1.23.5","pandas==1.5.2","python-dateutil==2.8.2","pytz==2022.6","six==1.16.0"]

)