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

    def test_cli_puml_component(self):
        args = []

        # TODO: populate args list, or pass empty list for no args

        exit_code, output_message = self.run_puml_component_cli_command_with_args(args)

        # TODO:  perform assertions against the output message
        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertTrue(len(output_message) > 0)  # asserts the command produced output
        # TODO:  assert the output message is correct

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
