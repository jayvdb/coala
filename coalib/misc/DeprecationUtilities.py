import logging


def check_deprecation(param_list):
    """
    Shows a deprecation warning message if the parameters
    passed are not ``None``.

    :param param_list:
        A dictionary of parameters with their names mapped
        to their values being checked for deprecation.
    """
    for param_name, param_value in param_list.items():
        if param_value is not None:
            logging.warning('{} parameter is deprecated'.format(param_name))
