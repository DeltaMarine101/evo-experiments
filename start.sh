source backend/.venv/bin/activate
python-to-typescript-interfaces 'backend/src/typing/interface.py' -o 'frontend/src/utility/interface.ts' --export
tmuxinator start -p .tmuxinator.yml