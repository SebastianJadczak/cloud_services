from pages.first_step import FirstStepPage
from tests.BaseTest import BaseTest
import pytest

@pytest.mark.usefixtures('setup')
class TestFirstStep(BaseTest):
    """The class responsible for the first step in the form."""

    def test_first_step(self):
        """Test first step form."""
        self.driver.get(self.url)
        firs_step = FirstStepPage(self.driver)
        firs_step.complete_first_step('Sebastian', 'Jadczak', 'sebastian-jadczak@wp.pl','518521272', '05240167335','AYH706804','21.06.1990')