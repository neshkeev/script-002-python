
# Работа с PIP

1. Посмотрите список установленных пакетов.

   ```console
   $ pip list
   ```

2. Проверьте в нём пакет [`pycodestyle`](https://pypi.org/project/pycodestyle/).

3. Если такого пакета нет, то установите для текущего пользователя

   ```console
   $ pip install --user pycodestyle
   ```

   иначе обновите его:

   ```console
   $ pip install --user --upgrade pycodestyle
   ```

4. Запустите `pycodestyle` для любой вашей программы:

   ```console
   $ pycodestyle 03_others/pip/myprogram.py
   $ pycodestyle --show-source --show-pep8 03_others/pip/myprogram.py
   ```

5. Исправьте указанные ошибки и запустите на проверку снова.
