from click.testing import CliRunner
from os import listdir, path
from typing import Tuple
from tempfile import TemporaryDirectory
from unittest import TestCase

from aac.execute.command_line import cli, initialize_cli


class TestGeneratePlantUMLDiagrams(TestCase):

    def test_puml_component(self):

        # TODO: Write success and failure unit tests for puml_component
        self.fail("Test not yet implemented.")

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

         # Like in core going to rely on the CLI testing for this, have not determined what we would like to test here
        pass

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
        """Test the puml-sequence CLI command for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.abspath("./alarm_clock/usecase.yaml")

            args = [aac_file_path, temp_dir, "UNCLASSIFIED"]

            exit_code, output_message = self.run_puml_sequence_cli_command_with_args(args)

            self.assertEqual(0, exit_code)  # asserts the command ran successfully
            self.assertGreater(len(output_message) > 0)  # asserts the command produced output
            self.assertIn("All AaC constraint Checks were successful", output_message)  # asserts the check command ran successful
            self.assertIn(temp_dir, output_message)  # asserts the generate command ran successfully

            # Make sure files were created correctly
            temp_dir_files = listdir(temp_dir)
            self.assertEqual(2, len(temp_dir_files))


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
