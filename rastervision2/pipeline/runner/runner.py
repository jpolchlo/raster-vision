from abc import abstractmethod
from typing import Optional, List

from rastervision2.pipeline.pipeline import Pipeline


class Runner():
    """A method for running a Pipeline.

    This can be subclassed to provide the ability to run on different cloud
    providers, etc.
    """

    @abstractmethod
    def run(self,
            cfg_json_uri: str,
            pipeline: Pipeline,
            commands: List[str],
            num_splits: int = 1):
        """Run commands in a Pipeline using a serialized PipelineConfig.

        Args:
            cfg_json_uri: URI of a JSON file with a serialized PipelineConfig
            pipeline: the Pipeline to run
            commands: names of commands to run
            num_splits: number of splits to use for splittable commands
        """
        pass

    def get_split_ind(self) -> Optional[int]:
        """Get the split_ind for the process.

        For split commands, the split_ind determines which split of work to perform
        within the current OS process. The CLI has a --split-ind option, but some runners
        may have their own means of communicating the split_ind, and this method should
        be overridden in such cases. If this method returns None, then the --split-ind
        option will be used. If both are null, then it won't be possible to run the
        command.
        """
        return None
