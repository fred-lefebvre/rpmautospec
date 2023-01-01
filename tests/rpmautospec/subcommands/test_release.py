import logging
import os.path
import tarfile
import tempfile
from pathlib import Path
from unittest.mock import Mock

import pytest

from rpmautospec.subcommands import release


__here__ = os.path.dirname(__file__)


class TestRelease:
    """Test the rpmautospec.subcommands.release module"""

    @pytest.mark.parametrize("method_to_test", ("calculate_release", "main"))
    def test_calculate_release(self, method_to_test, caplog):
        with tempfile.TemporaryDirectory() as workdir:
            with tarfile.open(
                os.path.join(
                    __here__,
                    os.path.pardir,
                    os.path.pardir,
                    "test-data",
                    "repodata",
                    "dummy-test-package-gloster-git.tar.gz",
                )
            ) as tar:
                def is_within_directory(directory, target):
                    
                    abs_directory = os.path.abspath(directory)
                    abs_target = os.path.abspath(target)
                
                    prefix = os.path.commonprefix([abs_directory, abs_target])
                    
                    return prefix == abs_directory
                
                def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
                
                    for member in tar.getmembers():
                        member_path = os.path.join(path, member.name)
                        if not is_within_directory(path, member_path):
                            raise Exception("Attempted Path Traversal in Tar File")
                
                    tar.extractall(path, members, numeric_owner=numeric_owner) 
                    
                
                safe_extract(tar, path=workdir)

            unpacked_repo_dir = Path(workdir) / "dummy-test-package-gloster"

            expected_release = "11"

            if method_to_test == "calculate_release":
                assert release.calculate_release(unpacked_repo_dir) == expected_release
            else:
                with caplog.at_level(logging.INFO):
                    args = Mock()
                    args.spec_or_path = unpacked_repo_dir
                    release.main(args)
                assert f"calculate_release release: {expected_release}" in caplog.text
