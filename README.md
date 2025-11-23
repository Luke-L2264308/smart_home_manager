# Smart Home Manager

A small educational Python application that provides a simple GUI for creating and managing virtual smart homes and devices (lights, doors and plugs). The project demonstrates object-oriented design for smart devices together with a Tkinter-based frontend that allows creating multiple smart homes, adding/removing devices, toggling states and saving/loading basic persistence.

**Key features**
- **Create multiple Smart Homes** with configurable device limits.
- **Manage devices**: add SmartLight, SmartDoor and SmartPlug devices.
- **Control devices**: toggle devices on/off, edit brightness (lights), edit consumption rate (plugs), toggle door lock.
- **Overview and persistence**: shows a summary of homes and saves/loads state from a simple local file (`smart homes`).

**Note:** This repository is a coursework/demo project and is intended for learning and experimentation rather than production use.

**Quick Start / At-a-glance**
- Run the multi-home GUI (recommended entry point):
	- `python coursework2_extension.py`
- Run a single Smart Home GUI instance (for testing/dev):
	- `python coursework2_frontend.py` (this file exposes `test_smart_home_system` for manual testing)

**Prerequisites**
- Python 3.8+ installed (Windows, macOS or Linux).
- The GUI uses the standard library `tkinter` module (usually included with standard Python installers). On some Linux distributions, you may need to install additional OS packages (for example `sudo apt install python3-tk`).

Installation
1. Clone the repository:
	 - `git clone https://github.com/Luke-L2264308/smart_home_manager/tree/main `
2. Change into the project folder:
	 - `cd smart_home_manager`
3. Run the app (Windows PowerShell example):
	 - `python coursework2_extension.py`

Usage
- **Overview**: The top-level window lists added smart homes and provides a summary of device counts and how many devices are switched on.
- **Add Home**: Click `Add home` and enter the maximum number of devices the new smart home should support.
- **Access Home**: Click a `Smart Home N` button to open the home view. From there you can:
	- `Add` a device (enter `light`, `plug` or `door` and provide the requested value).
	- `Toggle` a device to switch it on/off.
	- `Edit` a device to change brightness (lights), consumption rate (plugs) or toggle door lock.
	- `Delete` a device to remove it from the home.
- **Turn On/Off All**: Buttons are provided to turn every device in the open home on or off.
- **Save / Load**: The app persists homes to a local file named `smart homes` using a plain-text representation. Use `Save` in the top-level view to write current state.

Running tests / manual checks
- There are no automated unit tests in the repo. Small manual test functions are available in the code for interactive checks:
	- `test_smart_home()` and `test_custom_device()` in `python_coursework_2_improvedplug.py`.
	- `test_smart_home_system(on_own)` in `coursework2_frontend.py` and `coursework2_extension.py` (used by the demo main functions).
- To exercise a quick manual test: run `python coursework2_extension.py` and use the GUI, or import the modules in a Python REPL and call the provided `test_...` functions.

Project structure and key files
- `python_coursework_2_improvedplug.py` - Core domain classes for devices and the `SmartHome` container:
	- `SmartObject` base class, `SmartPlug`, `SmartLight`, `SmartDoor` classes.
	- `SmartHome` class: maintains a device list and provides methods to add/remove/toggle devices.
- `coursework2_frontend.py` - `SmartHomeApp`: Tkinter frontend for a single Smart Home. Provides the device CRUD and control UI.
- `coursework2_extension.py` - `SmartHomesApp`: extends the frontend to manage multiple Smart Homes, load/save state and present an overview. This file is the recommended entry point for the full application.
- `smart homes` - (created/used at runtime) plain-text persistence file used by `SmartHomesApp.save()` and `load()`.

Dependencies
- Uses only Python standard library modules (`tkinter`, `os`, etc.). No external pip packages required.

Development notes
- The GUI code uses `tkinter` and simple layout via `grid()`. The `SmartHome` and device classes are intentionally simple for coursework demonstration.
- To extend this project you might:
	- Add unit tests (pytest) for `SmartPlug`, `SmartLight`, `SmartDoor` and `SmartHome` behaviours.
	- Replace the simple text persistence with JSON or SQLite for more robust storage.
	- Improve the UI layout, validation and error handling.


License
- No license file is included. Add a `LICENSE` if you want to specify reuse terms.




