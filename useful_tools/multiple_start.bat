@echo off
rem OBSを起動
start "" "C:\Program Files\obs-studio\bin\64bit\obs64.exe"

rem Pythonスクリプトを特定のタイトルで起動
start "MyPythonScript" python "C:\path\to\your_script.py"

rem 実行中の状態で停止
echo 終了する場合は「end」と入力してEnterを押してな！
set /p user_input=入力: 
if /i "%user_input%"=="end" (
    goto :exit_program
) else (
    echo 「end」と入力するまで終了せえへんで！
    goto :wait_for_input
)

:exit_program
rem OBSと特定のPythonプロセスを終了
taskkill /im obs64.exe /f
taskkill /fi "WindowTitle eq MyPythonScript"

echo 全部終了したで！
pause
