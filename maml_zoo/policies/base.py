

class Policy(object):
    """
    A container for storing the current pre and post update policies
    Also provides functions for executing and updating policy parameters
    Args:

    """
    def __init__(self, env_spec, meta_batch_size):
        self._env_spec = env_spec
        self.init_policy = None

    def get_action(self, observation, policy_params):
        """
        Runs a single observation through the specified policy
        Args:
            observation (array) : single observation
            policy_params (params) : 
        Returns:
            (array) : array of arrays of actions for each env
        """
        raise NotImplementedError

    def get_actions(self, observations, policy_params):
        """
        Runs each set of observations through each task specific policy 
        Args:
            observations (array) : array of arrays of observations generated by each task and env
        Returns:
            (array) : array of arrays of actions for each env
        """
        raise NotImplementedError

    def reset(self, dones=None):
        pass

    @property
    def observation_space(self):
        return self._env_spec.observation_space

    @property
    def action_space(self):
        return self._env_spec.action_space

    @property
    def env_spec(self):
        return self._env_spec

    def log_diagnostics(self, paths):
        """
        Log extra information per iteration based on the collected paths
        """
        pass

    def load_params(self, policy_params):
        """
        Args:
            policy_params (array): array of policy parameters for each task
        """
        raise NotImplementedError

class StochasticPolicy(Policy):

    @property
    def distribution(self):
        """
        Returns:
            (Distribution) : this policy's distribution
        """
        raise NotImplementedError

    def dist_info_sym(self, obs_var, state_info_vars):
        """
        Return the symbolic distribution information about the actions.
        Args:
        	obs_var (placeholder) : symbolic variable for observations
        	state_info_vars (dict) : a dictionary of placeholders that contains information about the 
        	state of the policy at the time it received the observation
        Returns:
        	(dict) : a dictionary of tf placeholders for the policy output distribution
        """
        raise NotImplementedError

    def dist_info(self, obs, state_infos):
        """
        Args:
        	obs_var (placeholder) : symbolic variable for observations
        	state_info_vars (dict) : a dictionary of placeholders that contains information about the 
        	state of the policy at the time it received the observation
        Returns:
        	(dict) : a dictionary of tf placeholders for the policy output distribution
        """
        raise NotImplementedError
