# Contributing to Aware-AI-Framework

Thank you for your interest in contributing! Please follow these guidelines to keep the project organized and reproducible.

## How to Contribute

1. **Fork the repository** and clone your fork locally:
```bash
git clone https://github.com/<your-username>/Aware-AI-Framework.git
cd Aware-AI-Framework
```

2. **Create a new branch** for your feature or bugfix:
```bash
git checkout -b feature/my-new-feature
```

3. **Install the dev environment** if you haven’t already:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Write code following the modular architecture**:
   - Stage1: `stage1_demodulators/`  
   - Stage2: `stage2_codebook/`  
   - Stage3: `stage3_recursive_closure/`  
   - Core helpers: `ai_core/` and `utils/`  

5. **Add tests** in `tests/` and ensure all tests pass:
```bash
pytest tests/
```

6. **Update documentation** in `docs/` if needed.

7. **Commit your changes** with a clear message:
```bash
git add .
git commit -m "Brief description of your change"
```

8. **Push your branch** and open a pull request:
```bash
git push origin feature/my-new-feature
```

## Guidelines

- Keep your commits small and focused.  
- Document any new modules or interfaces.  
- Ensure experiments are reproducible with seed data.  
- Follow the existing coding style (PEP8 / docstrings).  

## Code of Conduct
Be respectful, collaborative, and constructive. Follow GitHub community guidelines.

## License
All contributions are under the MIT license.
