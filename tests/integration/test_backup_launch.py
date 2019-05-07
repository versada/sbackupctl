import os
import mock

from versada_odoo_backups import cli

DIR_HERE = os.path.abspath(os.path.dirname(__file__))
DIR_HOOKS = os.path.join(DIR_HERE, 'test_hook_dir')


def _hook_dir(path):
    return os.path.join(DIR_HOOKS, path)


@mock.patch('versada_odoo_backups.cli._call_executable')
def test_backup_subcommand(call_executable):
    _call('--hook-dir=%s backup' % DIR_HOOKS)
    expected_calls = [
        mock.call([_hook_dir('pre/pre-hook.sh')]),
        mock.call([_hook_dir('pre/pre2-hook.sh')]),
        mock.call([_hook_dir('backup/backup1.sh')]),
        mock.call([_hook_dir('backup/backup2.sh')]),
        mock.call([_hook_dir('post/post-hook.sh')]),
        mock.call([_hook_dir('post/post2-hook.sh')]),
    ]
    call_executable.assert_has_calls(expected_calls)


@mock.patch('versada_odoo_backups.cli._call_executable')
def test_list_subcommand(call_executable):
    _call('--hook-dir=%s list' % DIR_HOOKS)
    expected_calls = [mock.call([_hook_dir('list')])]
    call_executable.assert_has_calls(expected_calls)


@mock.patch('versada_odoo_backups.cli._call_executable')
def test_get_subcommand(call_executable):
    _call('--hook-dir=%s get 12345' % DIR_HOOKS)
    expected_calls = [mock.call([_hook_dir('get'), '12345'])]
    call_executable.assert_has_calls(expected_calls)


def _call(call_args):
    parser = cli.get_parser()
    args = parser.parse_args(call_args.split())
    return args.func(args)
