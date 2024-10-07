@echo off
cd /d %~dp0
SET current_path=%~dp0
SchTasks /Create /SC MINUTE /TN "My Task" /TR "%current_path%seven-days.exe --seven"
