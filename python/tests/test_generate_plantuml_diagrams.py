from click.testing import CliRunner
from os import listdir, path
from typing import Tuple
from tempfile import TemporaryDirectory
from unittest import TestCase

from aac.execute.command_line import cli, initialize_cli


class TestGeneratePlantUMLDiagrams(TestCase):

    def test_puml_component(self):
        # Like in core going to rely on the CLI testing for this, have not determined what we would like to test here
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
        """Test the puml-component CLI command success for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/alarm_clock.yaml")
            args = [aac_file_path, temp_dir]
            exit_code, output_message = self.run_puml_component_cli_command_with_args(args)

            self.assertEqual(0, exit_code) #assert the command ran successfully
            self.assertIn("All AaC constraint checks were successful", output_message) # assert check ran successfully

    def test_cli_puml_component_output(self):
        """Test the puml-sequence CLI command file output for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/alarm_clock.yaml")
            args = [aac_file_path, temp_dir]
            exit_code, output_message = self.run_puml_component_cli_command_with_args(args)

            temp_dir_files = listdir(temp_dir)
            self.assertNotEqual(0, len(temp_dir_files))
            for temp_file in temp_dir_files:
                self.assertTrue(temp_file.find("_component_diagram.puml"))
                temp_file_content = open(path.join(temp_dir, temp_file), "r")
                temp_content = temp_file_content.read()
                self.assertIn("Component Diagram", temp_content)
                temp_file_content.close()

    def test_cli_puml_component_failure(self):
        """Test the puml-component CLI command failure for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/structures.yaml")
            args = [aac_file_path, temp_dir]
            exit_code, output_message = self.run_puml_component_cli_command_with_args(args)
            self.assertNotEqual(0, exit_code)
            self.assertIn("No applicable model definitions to generate a component diagram.", output_message)

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

    def test_cli_puml_sequence_success(self):
        """Test the puml-sequence CLI command success for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/usecase.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_sequence_cli_command_with_args(args)

            self.assertEqual(0, exit_code)  # asserts the command ran successfully
            self.assertGreater(len(output_message), 0)  # asserts the command produced output
            self.assertIn("All AaC constraint checks were successful.", output_message)  # asserts the check command ran successful
            self.assertIn(temp_dir, output_message)  # asserts the puml-sequence command ran successfully

    def test_cli_puml_sequence_file_output(self):
        """Test the puml-sequence CLI command file output for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/usecase.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_sequence_cli_command_with_args(args)

            # Make sure files were created correctly
            temp_dir_files = listdir(temp_dir)
            self.assertNotEqual(0, len(temp_dir_files))
            for temp_file in temp_dir_files:
                self.assertTrue(temp_file.find("_sequence_diagram.puml"))
                temp_file_content = open(path.join(temp_dir, temp_file), "r")
                temp_content = temp_file_content.read()
                self.assertIn("Sequence Diagram", temp_content)
                self.assertIn("participant", temp_content)
                temp_file_content.close()

    def test_cli_puml_sequence_failure(self):
        """Test the puml-sequence CLI command failure for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/alarm_clock.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_sequence_cli_command_with_args(args)

            self.assertNotEqual(0, exit_code)  # asserts the command failed
            self.assertGreater(len(output_message), 0)  # asserts the command produced output
            self.assertIn("No applicable use case definitions to generate a sequence diagram", output_message)  # asserts the puml-sequence command run failed

    def test_puml_object(self):

         # Like in core going to rely on the CLI testing for this, have not determined what we would like to test here
        pass

    def run_puml_object_cli_command_with_args(self, args: list[str]) -> Tuple[int, str]:
        """Utility function to invoke the CLI command with the given arguments."""
        initialize_cli()
        runner = CliRunner()
        result = runner.invoke(cli, ["puml-object"] + args)
        exit_code = result.exit_code
        std_out = str(result.stdout)
        output_message = std_out.strip().replace("\x1b[0m", "")
        return exit_code, output_message

    def test_cli_puml_object_success(self):
        """Test the puml-object CLI command success for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/alarm_clock.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_object_cli_command_with_args(args)

            self.assertEqual(0, exit_code)  # asserts the command ran successfully
            self.assertGreater(len(output_message), 0)  # asserts the command produced output
            self.assertIn("All AaC constraint checks were successful.", output_message)  # asserts the check command ran successful
            self.assertIn(temp_dir, output_message)  # asserts the puml-object command ran successfully

    def test_cli_puml_object_file_output(self):
        """Test the puml-object CLI command file output for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/alarm_clock.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_object_cli_command_with_args(args)

            # Make sure files were created correctly
            temp_dir_files = listdir(temp_dir)
            self.assertNotEqual(0, len(temp_dir_files))
            for temp_file in temp_dir_files:
                self.assertTrue(temp_file.find("_object_diagram.puml"))
                temp_file_content = open(path.join(temp_dir, temp_file), "r")
                temp_content = temp_file_content.read()
                self.assertIn("Object Diagram", temp_content)
                temp_file_content.close()

    def test_cli_puml_object_failure(self):
        """Test the puml-object CLI command failure for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/structures.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_object_cli_command_with_args(args)

            self.assertNotEqual(0, exit_code)  # asserts the command failed
            self.assertGreater(len(output_message), 0)  # asserts the command produced output
            self.assertIn("No applicable model definitions to generate an object diagram.", output_message)  # asserts the puml-object command run failed

    def test_puml_requirements(self):
        # Like in core going to rely on the CLI testing for this, have not determined what we would like to test here
        pass

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

    def test_cli_puml_requirements_success(self):
        """Test the puml-requirements CLI command success for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "calc/model/calculator.yaml")

            args = [aac_file_path, temp_dir]

        exit_code, output_message = self.run_puml_requirements_cli_command_with_args(
            args
        )

        self.assertEqual(0, exit_code)  # asserts the command ran successfully
        self.assertGreater(len(output_message), 0)  # asserts the command produced output
        self.assertIn("All AaC constraint checks were successful.", output_message)  # asserts the check command ran successful
        self.assertIn(temp_dir, output_message)  # asserts the puml-sequence command ran successfully

    def test_cli_puml_requirements_file_output(self):
        """Test the puml-requirements CLI command file output for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "calc/model/calculator.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_requirements_cli_command_with_args(args)

            # Make sure files were created correctly
            temp_dir_files = listdir(temp_dir)
            self.assertNotEqual(0, len(temp_dir_files))
            for temp_file in temp_dir_files:
                self.assertTrue(temp_file.find("_requirements_diagram.puml"))
                temp_file_content = open(path.join(temp_dir, temp_file), "r")
                temp_content = temp_file_content.read()
                self.assertIn("Requirements Diagram", temp_content)
                self.assertIn("id =", temp_content)
                self.assertIn("Text =", temp_content)
                temp_file_content.close()

    def test_cli_puml_requirements_failure(self):
        """Test the puml-requirements CLI command failure for the PUML Plugin."""
        with TemporaryDirectory() as temp_dir:
            aac_file_path = path.join(path.dirname(__file__), "alarm_clock/alarm_clock.yaml")

            args = [aac_file_path, temp_dir]

            exit_code, output_message = self.run_puml_requirements_cli_command_with_args(args)

            self.assertNotEqual(0, exit_code)  # asserts the command failed
            self.assertGreater(len(output_message), 0)  # asserts the command produced output
            self.assertIn("No applicable requirement specification definitions to generate a requirements diagram", output_message)  # asserts the puml-sequence command run failed
