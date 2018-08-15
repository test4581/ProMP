from maml_zoo.utils.serializable import Serializable


class Baseline(Serializable):
    """
    Reward baseline interface
    """

    def __init__(self, *args, **kwargs):
        Serializable.quick_init(self, locals())

    def get_param_values(self):
        """
        Returns the parameter values of the baseline object

        """
        raise NotImplementedError

    def set_params(self, value):
        """
        Sets the parameter values of the baseline object

        Args:
            value: parameter value to be set

        """
        raise NotImplementedError

    def fit(self, paths):
        """
        Fits the baseline model with the provided paths

        Args:
            paths: list of paths

        """
        raise NotImplementedError

    def predict(self, path):
        """
        predicts the reward baselines for a provided trajectory / path

        Args:
            path: dict of lists/numpy array containing trajectory / path information
                  such as "observations", "rewards", ...

        Returns: numpy array of the same length as paths["observations"] specifying the reward baseline

        """
        raise NotImplementedError

    def log_diagnostics(self, paths):
        """
        Log extra information per iteration based on the collected paths
        """
        pass

    def __getstate__(self):
        state = {
            'init_args': Serializable.__getstate__(self),
            'baseline_params': self.get_param_values()
        }
        return state

    def __setstate__(self, state):
        Serializable.__setstate__(self, state['init_args'])
        self.set_params(state['baseline_params'])
