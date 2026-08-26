---
title: "Jupyter Notebooks"
unit_id: 79
course_id: 3
level: "Expert"
slug: jupyter-notebooks
is_course: 0
---

# Jupyter Notebooks

Open-source application for interactive code execution, data visualization, and narrative documentation. Supports Julia, Python, R (Ju-Pyt-R). FAIR principles-aligned: open-source license, rich metadata documentation, searchable registries (GitHub). Platform: Web-based application on localhost:8888; Jupyter starts local Python server.

## Installation & Setup

Installation methods: (1) Anaconda distribution (recommended for beginners; includes 1000+ pre-loaded libraries like NumPy, pandas, Matplotlib); (2) pip3 install jupyter. Launch: jupyter notebook command from terminal; starts dashboard displaying accessible files/directories. File format: .ipynb (JSON text file containing cells, outputs, image attachments, metadata).

Naming notebooks: Click file name at top; type new name; save (Ctrl+S). Shutdown: File > Close and Halt or Kernel > Shutdown. Checkpoint system: .ipynb_checkpoints hidden subdirectory; autosaves every 120 seconds; recover via File > Revert to Checkpoint.

## Cell Types & Execution

**Code Cells**: Execute Python (or other language) code. Label: In [N] (execution order number). Output: Out [N]. Code from previously executed cells persists as kernel state (variables, functions, imports shared across all cells).

**Markdown Cells**: Format using Markdown syntax (headers # ## ###, bold **text**, italics *text*, lists, hyperlinks [text](url), code blocks ```, inline code ```, images ![alt](url)). Rendered in-place upon execution.

**Execution Modes**:
- Command Mode (blue border): Esc key. Select/manipulate cells. Shortcuts: A/B (insert above/below), M (convert to Markdown), Y (convert to code), D+D (delete), Z (undo), Up/Down (scroll).
- Edit Mode (green border): Enter key or click cell. Edit content. Shortcuts: Ctrl+Enter (run cell), Shift+Enter (run & select next), Alt+Enter (run & insert below), Ctrl+Shift+– (split cell), Ctrl+Click (multiple cursors).

Execution order: Numbers indicate sequence of cell runs, not position in notebook. Kernel maintains state across non-sequential execution. Reset: Kernel > Restart (clear all variables), Restart & Clear Output, Restart & Run All (top-to-bottom execution), Interrupt (stop running computation).

## Kernels

Computational engine running code. One kernel per notebook instance. Choices available at notebook creation: Python (various versions), R, Julia, Scala, Java, C, Fortran, MATLAB (imatlab, Calysto MATLAB Kernel). SoS kernel provides multi-language support. Each requires separate installation; conda environments integrate seamlessly.

## Magic Commands

Special Jupyter commands (not standard Python). List all: %lsmagic. Documentation: %command?

**Line Magics** (% prefix, single-line arguments):
- %matplotlib inline: Embed Matplotlib plots in cell output
- %timeit: Measure cell execution time
- %writefile / %savefile: Save cell contents to file
- %store: Save variable for use in other notebooks
- %pwd: Print working directory
- %run: Execute external Python script
- %time: Time single statement execution

**Cell Magics** (%% prefix, entire cell as arguments):
- %%javascript: Interpret cell as JavaScript
- %%html: Render cell as HTML
- %%bash: Execute bash commands
- %%writefile: Save entire cell to file

**Bash integration**: !command syntax (e.g., !pip list, !ls -la, !mkdir, !cd) executes system commands.

## Example Workflow: Fortune 500 Data Analysis

Dataset: 500 companies/year from 1955–2005. Columns: Year, Rank, Company, Revenue (millions), Profit (millions).

**Setup Cell** (best practice):
```python
%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
df = pd.read_csv('fortune500.csv')
```

**Data Exploration**: df.head(), df.tail(), df.dtypes, len(df), df.loc[] filtering. Identify missing values (N.A. strings); remove/convert. Checkpoint work frequently with Ctrl+S.

**Plotting**: pandas groupby() → aggregate (mean, std). matplotlib plot() + seaborn styling. fill_between() for confidence bands. Multi-subplot layouts: plt.subplots(ncols=2).

**Output**: Code cells auto-display final line value (e.g., variable, function result). print() for intermediate reporting. Pandas DataFrames render as formatted tables.

## Sharing & Export

**Export Formats**: File > Download As → HTML, PDF, LaTeX, Python script, Markdown, .ipynb.

**GitHub (12M+ public notebooks, April 2023)**:
- GitHub Gists (gist.github.com): Paste .ipynb JSON content; creates shareable URL; fork-able.
- Git repositories: Full version control; add .ipynb_checkpoints to .gitignore to avoid committing checkpoint files.
- Render .ipynb directly in repos and gists.

**Nbviewer** (nbviewer.jupyter.org): Free rendering service. Input URL, Gist ID, or GitHub username/repo. Displays notebook as webpage; shareable constant URL.

**Pre-sharing Checklist**:
- Cell > All Output > Clear
- Kernel > Restart & Run All
- Verify cells execute in order top-to-bottom

## Advanced Features

**Jupyter Widgets** (ipywidgets): Interactive GUI components (sliders, buttons, dropdowns, text fields). Example: IntRangeSlider for year filtering; interact() decorator to trigger updates.

**Jupyter Terminal**: Access terminal via New > Terminal. Commands: cd, ls, mkdir, cp, mv, pip, conda, git. Password protection: jupyter notebook password.

**Jupyter Lab**: Modern tabbed interface supporting multiple notebooks, terminals, files, editors simultaneously. More resource-intensive; better for large projects. Install: pip install jupyterlab. Launch: jupyter lab.

**Extensions** (via Nbextensions): Table of Contents, Variable Inspector (type/size/value/shape), ExecuteTime (execution duration). Install: pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install. Enable from Nbextensions tab.

## Keyboard Shortcuts Summary

**Command Mode (Esc)**:
- A/B: Insert cell above/below
- M/Y: Convert cell type (Markdown/code)
- D+D: Delete cell
- Z: Undo deletion
- Shift+Up/Down: Select multiple cells
- Shift+M: Merge selected cells
- Ctrl+Shift+P: Command palette

**Edit Mode (Enter)**:
- Ctrl+Enter: Run cell, stay
- Shift+Enter: Run cell, move to next
- Alt+Enter: Run cell, insert below
- Ctrl+Shift+–: Split cell at cursor
- Ctrl+Click: Multiple cursors

## FAIR Science Alignment

Open-source (GPL license, GitHub/jupyter). Rich metadata (jupyter.readthedocs.io). Searchable registry (github.com/jupyter). Reproducible research: code + outputs + narrative in single document. Widely adopted in academia (LIGO gravitational wave research, published as executable notebooks).

## Resources & References

Dataquest tutorial (comprehensive beginner walkthrough), mygeohub.org platform, YouTube tutorials, Project Jupyter gallery, Advanced Jupyter Notebook tutorials, 28 Tips/Tricks/Shortcuts guides, interactive guided projects.

## Summarized attachments
- **How to Use Jupyter Notebook: A Beginner's Tutorial** (https://www.dataquest.io/blog/jupyter-notebook-tutorial/, link): Comprehensive Dataquest tutorial covering Jupyter Notebook fundamentals including installation via Anaconda or pip, notebook creation and interface, .ipynb file format, code and Markdown cell types, execution modes, kernel functionality, and Fortune 500 profit analysis example using pandas, matplotlib, and seaborn for data exploration and visualization. Includes installation instructions, setup best practices, data manipulation workflows, sharing via GitHub/Nbviewer, Jupyter Widgets, JupyterLab, and keyboard shortcuts.
