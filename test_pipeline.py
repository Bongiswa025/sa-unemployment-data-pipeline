
import unittest
from unittest.mock import patch
from pathlib import Path

import run_pipeline


class TestPipeline(unittest.TestCase):

    def test_pipeline_has_four_steps(self):
        self.assertEqual(len(run_pipeline.STEPS), 4)

    def test_pipeline_steps_are_in_correct_order(self):
        expected = [
            "extract.py",
            "transform.py",
            "load.py",
            "analysis.py",
        ]
        self.assertEqual(run_pipeline.STEPS, expected)

    def test_all_pipeline_scripts_exist(self):
        for script in run_pipeline.STEPS:
            script_path = run_pipeline.BASE_DIR / "src" / script
            self.assertTrue(script_path.is_file())

    @patch("run_pipeline.subprocess.run")
    def test_pipeline_runs_every_step(self, mock_run):
        run_pipeline.run_pipeline()

        self.assertEqual(mock_run.call_count, 4)

        for call, script in zip(
            mock_run.call_args_list,
            run_pipeline.STEPS,
        ):
            self.assertEqual(
                Path(call.args[0][1]).name,
                script,
            )
            self.assertTrue(call.kwargs["check"])


if __name__ == "__main__":
    unittest.main()
