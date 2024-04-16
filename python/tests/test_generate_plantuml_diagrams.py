from unittest import TestCase
from typing import Tuple
from click.testing import CliRunner
from aac.execute.command_line import cli, initialize_cli
from aac.execute.aac_execution_result import ExecutionStatus


from puml.generate_plantuml_diagrams_impl import (
    plugin_name,
    puml_component,
    before_puml_component_check,
    puml_sequence,
    before_puml_sequence_check,
    puml_object,
    before_puml_object_check,
    puml_requirements,
    before_puml_requirements_check,
)


class TestGeneratePlantUMLDiagrams(TestCase):

    def test_puml_component(self):
        pass

    def run_puml_component_cli_command_with_args(
        self, args: list[str]
    ) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["puml-component"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_puml_component_success(self):
        args = []
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/alarm_clock.yaml")
            args = [aac_file_path, temp_dir]
            exit_code, output_message = self.run_puml_component_cli_command_with_args(args)

            self.assertEqual(0, exit_code) #assert the command ran successfully
            self.assertIn("All AaC constraint checks were successful", output_message) # assert check ran successfully

            self.assertTrue(path.exists(path.join(temp_dir, "alarmclock_component_diagram.puml")))
            with open(path.join(temp_dir, "alarmclock_component_diagram.puml")) as alarmclock_file:
                self.assertIn("title AlarmClock Component Diagram", alarmclock_file)
                self.assertIn('component "AlarmClock"', alarmclock_file)
                self.assertIn("Timestamp --> ClockTimer : targetTime", alarmclock_file)

            self.assertTrue(path.exists(path.join(temp_dir, "clock_component_diagram.puml")))
            with open(path.join(temp_dir, "clock_component_diagram.puml")) as clock_file:
                self.assertIn("title Clock Component Diagram", clock_file)
                self.assertIn('component "Clock"', clock_file)
                self.assertIn("Clock --> Timestamp : currentTime", clock_file)

            self.assertTrue(path.exists(path.join(temp_dir, "clockalarm_component_diagram.puml")))
            with open(path.join(temp_dir, "clockalarm_component_diagram.puml")) as clockalarm_file:
                self.assertIn("title ClockAlarm Component Diagram", clockalarm_file)
                self.assertIn('component "ClockAlarm"', clockalarm_file)
                self.assertIn("ClockAlarm --> AlarmNoise : alarmNoise", clockalarm_file)

            self.assertTrue(path.exists(path.join(temp_dir, "clocktimer_component_diagram.puml")))
            with open(path.join(temp_dir, "clocktimer_component_diagram.puml")) as clocktimer_file:
                self.assertIn("title ClockTimer Component Diagram", clocktimer_file)
                self.assertIn('component "ClockTimer"', clocktimer_file)
                self.assertIn("ClockTimer --> TimerAlert : timerAlert", clocktimer_file)

    def test_cli_puml_component_failure(self):
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/structures.yaml")
            args = [aac_file_path, temp_dir]
            exit_code, output_message = self.run_puml_component_cli_command_with_args(args)
            self.assertNotEqual(0, exit_code)
            self.assertIn("No models found", output_message)

    def test_puml_sequence(self):

        # TODO: Write success and failure unit tests for puml_sequence
        self.fail("Test not yet implemented.")

    def run_puml_sequence_cli_command_with_args(
        self, args: list[str]
    ) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["puml-sequence"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_puml_sequence(self):
        args = []

        # TODO: populate args list, or pass empty list for no args

        exit_code, output_message = self.run_puml_sequence_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct

    def test_puml_object(self):

        # TODO: Write success and failure unit tests for puml_object
        self.fail("Test not yet implemented.")

    def run_puml_object_cli_command_with_args(self, args: list[str]) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["puml-object"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_puml_object(self):
        args = []

        # TODO: populate args list, or pass empty list for no args

        exit_code, output_message = self.run_puml_object_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct

    def test_puml_requirements(self):

        # TODO: Write success and failure unit tests for puml_requirements
        self.fail("Test not yet implemented.")

    def run_puml_requirements_cli_command_with_args(
        self, args: list[str]
    ) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["puml-requirements"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_puml_requirements(self):
        args = []

        # TODO: populate args list, or pass empty list for no args

        exit_code, output_message = self.run_puml_requirements_cli_command_with_args(
            args
        )

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct
