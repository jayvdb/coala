from coalib.bearlib.spacing.SpacingHelper import SpacingHelper
from coalib.bears.LocalBear import LocalBear
from coalib.results.Diff import Diff
from coalib.results.Result import Result


class SpaceConsistencyTestBear(LocalBear):

    def run(self,
            filename,
            file,
            use_spaces: bool,
            allow_trailing_whitespace: bool=False,
            tab_width: int=SpacingHelper.DEFAULT_TAB_WIDTH,
            enforce_newline_at_EOF: bool=True):
        '''
        Checks the space consistency for each line.

        :param use_spaces:                True if spaces are to be used instead
                                          of tabs
        :param allow_trailing_whitespace: Whether to allow trailing whitespace
                                          or not
        :param tab_width:                 Number of spaces representing one
                                          tab
        :param enforce_newline_at_EOF:    Whether to enforce a newline at the
                                          End Of File
        '''
        pass
