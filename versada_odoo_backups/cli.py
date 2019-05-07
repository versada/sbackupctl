import argparse
import subprocess
import os
import stat
import glob


def main():
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)


def do_backup(args):
    hook_dir = args.hook_dir
    pre_hooks = os.path.join(hook_dir, 'pre')
    backup_hooks = os.path.join(hook_dir, 'backup')
    post_hooks = os.path.join(hook_dir, 'post')

    for file_name in _get_executable_files(
            pre_hooks, backup_hooks, post_hooks
    ):
        if args.savepoint:
            _call_executable([file_name, args.savepoint])
        else:
            _call_executable([file_name])


def get_backup_list(args):
    list_file_path = os.path.join(args.hook_dir, 'list')
    _call_executable([list_file_path])


def download_backup(args):
    download_file_name = os.path.join(args.hook_dir, 'get')
    _call_executable([download_file_name, args.savepoint])


def get_parser():
    parser = argparse.ArgumentParser('Odoo Backup Controller')
    parser.add_argument(
        '--hook-dir', default=os.getenv('OBCTL_HOOK_DIR', '/opt/obctl/hooks')
    )
    subparsers = parser.add_subparsers()

    parser_backup = subparsers.add_parser('backup', help='Do a backup')
    parser_backup.add_argument(
        'savepoint', nargs='?',
        help='Instead of autogenerated id, do a named savepoint'
    )
    parser_backup.set_defaults(func=do_backup)

    parser_list = subparsers.add_parser('list', help='Lists all savepoints')
    parser_list.set_defaults(func=get_backup_list)

    parser_get = subparsers.add_parser(
        'get', help='Download a specific savepoint')
    parser_get.add_argument('savepoint', help='Savepoint id')
    parser_get.set_defaults(func=download_backup)
    return parser


def _call_executable(*args):
    subprocess.check_call(*args)


def _get_executable_files(*dirs):
    executable_file_paths = []
    for possible_dir in dirs:
        file_paths = sorted(glob.glob(os.path.join(possible_dir, '*')))
        for file_path in file_paths:
            if _is_executable(file_path):
                executable_file_paths.append(file_path)
    return executable_file_paths


def _is_executable(file_path):
    executable = stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH
    mode = os.stat(file_path).st_mode
    return bool(mode & executable)
