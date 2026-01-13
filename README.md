# AIForge 3D – AI‑Powered Blender Assistant

<p align="center">
  <img src="ui/icons/logo.png" alt="AIForge 3D Logo" width="128" height="128">
</p>

[![Version](https://img.shields.io/badge/version-1.3.1-blue.svg)](https://github.com/aiforge3d/blender-addon/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/aiforge3d/blender-addon/blob/main/LICENSE)
[![Blender](https://img.shields.io/badge/Blender-4.0%2B-orange.svg)](https://www.blender.org/)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-7289DA.svg)](https://discord.gg/dXAN23NwkM)

> **AIForge 3D** brings generative AI directly into Blender's 3D viewport, offering real‑time chat, tool orchestration, and specialist agents for modeling, shading, animation, and more.

🌐 **Language:** **English** | [Bahasa Indonesia](README_ID.md)

---

## 📖 Table of Contents
- [🌟 Overview](#-overview)
- [✨ Features](#-features)
- [📦 Installation](#-installation)
- [🔑 API Setup](#-api-setup)
- [🚀 Quick Start](#-quick-start)
- [🖥️ User Interface](#️-user-interface)
  - [Agent Selector](#agent-selector)
  - [Chat Panel & Streaming](#chat-panel--streaming)
  - [Settings Panel](#settings-panel)
- [🤖 Multi‑Agent System](#-multiagent-system)
  - [Available Agents](#available-agents)
  - [Orchestrator Mode](#orchestrator-mode)
- [💬 Usage Examples](#-usage-examples)
  - [Basic Commands](#basic-commands)
  - [Code Execution](#code-execution)
  - [Advanced Workflows](#advanced-workflows)
- [🔒 Thread‑Safety & Security](#-threadsafety--security)
- [📁 Architecture](#-architecture)
- [🛠️ Development](#️-development)
- [✅ Testing & CI](#-testing--ci)
- [❓ Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙌 Acknowledgements](#-acknowledgements)
- [📞 Support](#-support)

---

## 🌟 Overview

AIForge 3D is a **Blender add‑on** that integrates large‑language‑model back‑ends (MiniMax, OpenAI, etc.) to assist artists and developers directly inside Blender. It transforms natural language instructions into Blender operations, enabling you to:

- **Create 3D objects** using plain English commands
- **Modify scenes** with transformations, materials, and animations
- **Query your scene** for object information and properties
- **Execute Python code** safely within a sandboxed environment
- **Orchestrate complex workflows** using AI‑powered task delegation

---

## ✨ Features

### Core Capabilities
| Feature | Description |
|---------|-------------|
| **Natural Language Control** | Create, modify, and animate objects using plain English |
| **Streaming Responses** | See AI responses in real‑time as they are generated |
| **Multi‑Agent System** | Switch between specialist agents (Modeler, Shading, Animator, Director) |
| **Orchestrator Mode** | High‑level task decomposition and automatic delegation |
| **Tool Integration** | Web search, file operations, and inline result display |
| **Code Execution** | Safe sandboxed Python execution with undo/rollback |
| **Markdown Rendering** | Rich text with code blocks, tables, images, and blockquotes |

### Technical Features
- **Thread‑safe** – All `bpy.context` accesses via `bpy.app.timers.register`
- **Secure storage** – API keys encrypted in Blender's `WindowManager`
- **Auto‑resizing UI** – Chat panel adapts to content dynamically
- **Activity indicators** – Visual feedback during AI processing
- **Extensive logging** – Debug output to system console
- **CI/CD ready** – GitHub Actions for cross‑platform testing

---

## 📦 Installation

### Requirements
| Component | Version |
|-----------|---------|
| Blender | **4.0** or higher |
| API Key | MiniMax or OpenAI |
| OS | Windows, macOS, Linux |

### Installation Steps

1. **Download the addon**
   ```
   aiforge3d_v1.3.1.zip
   ```
   Get the latest release from the [Releases page](https://github.com/aiforge3d/blender-addon/releases).

2. **Install in Blender**
   - Open Blender
   - Navigate to `Edit > Preferences > Add‑ons`
   - Click **Install…**
   - Select the downloaded ZIP file
   - Enable the **AIForge 3D** checkbox

3. **Restart Blender**
   - Close and reopen Blender for full initialization

4. **Verify Installation**
   - Open 3D Viewport sidebar (`N` key)
   - Look for the **AIForge** tab

> 💡 **Tip:** Press `Ctrl+Alt+R` to reload the UI without restarting Blender.

---

## 🔑 API Setup

### Step 1: Obtain API Key

#### MiniMax (Recommended)
1. Visit [api.minimaxi.com](https://api.minimaxi.com)
2. Create an account
3. Navigate to API Keys section
4. Generate a new API key

#### OpenAI (Alternative)
1. Visit [platform.openai.com](https://platform.openai.com)
2. Create an account
3. Go to API Keys
4. Create a new secret key

### Step 2: Configure the Add‑on
1. Open Blender
2. Go to `View3D > Sidebar (N)` → **AIForge 3D** tab
3. Click the **Settings** icon (⚙️)
4. Paste your API key in the **API Key** field
5. Click **Save** or **Authenticate**

> 🔐 Your API key is stored securely and encrypted locally.

---

## 🚀 Quick Start

### Your First Interaction

1. **Open the AIForge panel** (Sidebar → **AIForge** tab)

2. **Select an Agent** from the dropdown:
   - *Generalist* – General‑purpose assistant
   - *Modeler* – Mesh and topology specialist
   - *Shading* – Materials and nodes expert
   - *Animator* – Keyframes and motion specialist
   - *Director* – Lighting and camera expert
   - *Orchestrator* – Multi‑step task coordinator

3. **Type a prompt** in the text box:
   ```
   Create a red cube at the origin
   ```

4. **Press Enter** or click **Send**

5. **Watch the response** stream in real‑time

6. **See your 3D scene** update automatically!

---

## 🖥️ User Interface

### Agent Selector
<p align="center">
  <img src="assets/agent_selector.gif" alt="Agent Selector" width="400">
</p>

- **Location:** Top of the AIForge panel
- **Function:** Switch between specialist AI agents
- **Source:** Configured in `llm/agent_prompts.py`
- **Property:** Updates `vibe4d_active_agent` scene property

### Chat Panel & Streaming
- **Markdown rendering** with syntax‑highlighted code blocks
- **Inline images** (URL or base64 encoded)
- **Tables and lists** for structured data
- **Auto‑resize** to fit content
- **Scroll navigation** for long conversations

### Settings Panel
| Setting | Description |
|---------|-------------|
| API Key | Your MiniMax/OpenAI key (encrypted) |
| Model | Select AI model version |
| Custom Instructions | Define persistent behavior rules |
| Theme | Light/Dark mode toggle |

---

## 🤖 Multi‑Agent System

### Available Agents

| Agent | Specialty | Best For |
|-------|-----------|----------|
| **Generalist** | All‑purpose | General questions, simple tasks |
| **Modeler** | Mesh & Topology | Creating/editing 3D geometry |
| **Shading** | Materials & Nodes | Textures, shaders, node setups |
| **Animator** | Keyframes & Motion | Animation, rigging, timing |
| **Director** | Lighting & Camera | Rendering, composition, lighting |
| **Orchestrator** | Task Coordination | Complex multi‑step workflows |

### Orchestrator Mode

The **Orchestrator** is a meta‑agent that can:

1. **Decompose** complex tasks into subtasks
2. **Delegate** to specialist agents automatically
3. **Coordinate** results across multiple operations
4. **Synthesize** a final comprehensive response

#### Example Orchestrator Prompt:
```
Design a sci‑fi spaceship interior with:
- A detailed cockpit with control panels
- Metallic brushed aluminum materials
- Animated blinking lights
- Dramatic spotlight lighting
```

The Orchestrator will automatically:
- Use **Modeler** for geometry
- Use **Shading** for materials
- Use **Animator** for light animations
- Use **Director** for lighting setup

---

## 💬 Usage Examples

### Basic Commands

#### Creating Objects
```
Create a cube at (0, 0, 0)
Add a UV sphere with radius 2 at location (5, 0, 0)
Create a torus with major_radius=3, minor_radius=0.5
Make a cylinder with depth=4 and radius=1
```

#### Scene Queries
```
List all objects in the scene
Show me all mesh objects
What is the location of the Camera?
How many vertices does the Cube have?
```

#### Transformations
```
Move the cube to (0, 0, 2)
Rotate the sphere by 45 degrees on the Z axis
Scale all selected objects to 0.5
Mirror the mesh along the X axis
```

#### Materials
```
Create a red glossy material called "Ruby"
Assign the Ruby material to the Cube
Create a glass material with IOR 1.45
Make the sphere emit blue light
```

#### Animation
```
Insert a keyframe at frame 1 for location
Animate the cube from (0,0,0) to (0,0,5) over 100 frames
Set the timeline to frame 50
Create a bouncing animation for the sphere
```

#### Rendering
```
Capture the current viewport
Take a screenshot from the active camera
Render the scene at 1920x1080
Set up a 3‑point lighting rig
```

### Code Execution

Execute Python code directly:
```python
import bpy

# Create a grid of cubes
for x in range(5):
    for y in range(5):
        bpy.ops.mesh.primitive_cube_add(
            size=0.8,
            location=(x * 2, y * 2, 0)
        )
```

### Advanced Workflows

#### Procedural Landscape
```
Create a procedural mountain landscape with:
- Subdivided plane with displacement
- Rocky material with variation
- Grass particles on flat areas
- Atmospheric fog
```

#### Character Setup
```
Set up a basic biped character:
- Create an armature with spine, arms, and legs
- Add IK constraints for feet and hands
- Create control shapes for animators
```

---

## 🔒 Thread‑Safety & Security

### Thread Safety
- All **`bpy.context`** accesses occur on the main thread
- Background operations use `bpy.app.timers.register`
- API key extracted in main thread, passed to workers
- Error handling prevents silent failures

### API Key Security
- Keys stored encrypted in `WindowManager`
- Never transmitted except to API endpoints
- Not included in scene files or exports
- Can be cleared via Settings panel

### Code Execution Safety
- Sandboxed Python environment
- Undo support for all operations
- Error capture and display
- No system‑level access

---

## 📁 Architecture

```
aiforge3d/
├── __init__.py           # Main addon entry point
├── api/
│   └── client.py         # HTTP wrapper, headers, error handling
├── auth/
│   └── manager.py        # Authentication and credential storage
├── llm/
│   ├── agent_prompts.py  # Specialist agent definitions
│   ├── chat_client.py    # Background streaming handler
│   └── response_handler.py # Response parsing, tool calls
├── operators/
│   └── *.py              # Blender operator definitions
├── tools/
│   ├── definitions.py    # Tool schemas for AI
│   ├── executor.py       # Tool execution engine
│   └── helpers.py        # Utility functions
├── ui/
│   ├── manager.py        # UI orchestration, timers
│   ├── ui_factory.py     # View creation and management
│   ├── components/
│   │   ├── agent_selector.py    # Agent dropdown
│   │   ├── markdown_message.py  # Rich text rendering
│   │   └── *.py                 # Other UI components
│   └── views/
│       ├── main_view.py  # Main chat interface
│       └── auth_view.py  # Login/settings view
├── utils/
│   ├── error_utils.py    # Error handling helpers
│   ├── history_manager.py # Conversation persistence
│   └── secure_storage.py # Encrypted key storage
└── external/             # Third‑party libraries
```

### Key Module Responsibilities

| Module | Responsibility |
|--------|----------------|
| `api/client.py` | Low‑level HTTP, authentication headers |
| `llm/chat_client.py` | Background thread streaming |
| `llm/response_handler.py` | Parse responses, handle tool calls |
| `ui/manager.py` | Coordinate UI updates via Blender timers |
| `ui/components/markdown_message.py` | Render markdown with auto‑resize |

---

## 🛠️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/aiforge3d/blender-addon.git
cd blender-addon

# Install dependencies (using Blender's Python)
blender --background --python - <<PY
import sys, subprocess, pathlib
sys.path.append(str(pathlib.Path('.').resolve()))
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
PY
```

### Running Tests

```bash
# Run all unit tests
blender --background --python -m unittest discover -s tests

# Run specific test file
blender --background --python -m unittest tests.test_chat_client
```

### Building Release ZIP

```powershell
# PowerShell
Compress-Archive -Path 'aiforge3d' -DestinationPath 'aiforge3d_latest.zip' -Force
```

```bash
# Bash/Linux
zip -r aiforge3d_latest.zip aiforge3d/
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Document public functions with docstrings
- Run `flake8` before committing

---

## ✅ Testing & CI

### Test Coverage
| Area | Coverage |
|------|----------|
| Chat Client | Unit tests for streaming, error handling |
| Response Handler | Tool call parsing, continuation logic |
| UI Components | Rendering, resizing, event handling |
| API Client | Request building, response parsing |

### Continuous Integration
- **GitHub Actions** runs on every push and PR
- Tests on Windows, macOS, and Linux
- Multiple Blender versions (4.0, 4.1, 4.2)
- Linting with `flake8`
- Type checking with `mypy`

---

## ❓ Troubleshooting

### Common Issues

| Symptom | Cause | Solution |
|---------|-------|----------|
| No response appears | Invalid/missing API key | Re‑enter key in Settings |
| UI freezes | Timer registration issue | Press `Ctrl+Alt+R` or restart Blender |
| Images not loading | URL unreachable | Check URL accessibility; use base64 for local images |
| Streaming stops | Network interruption | Check internet; retry the prompt |
| "Thinking" never ends | API timeout | Increase timeout in settings; retry |

### Viewing Logs
1. Open **Window > Toggle System Console** (Windows) or launch Blender from terminal (macOS/Linux)
2. Look for `[AIForge]` prefixed messages
3. Enable verbose logging in Settings if needed

### Resetting the Add‑on
1. Disable the add‑on in Preferences
2. Delete the add‑on folder manually
3. Restart Blender
4. Reinstall from ZIP

---

## 🤝 Contributing

We welcome contributions! Here's how:

### Getting Started
1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Make** your changes
5. **Test** thoroughly
6. **Commit** with clear messages
   ```bash
   git commit -m "Add amazing feature that does X"
   ```
7. **Push** to your fork
8. **Open** a Pull Request

### Guidelines
- Follow existing code style
- Write tests for new features
- Update documentation as needed
- Keep PRs focused and atomic
- Be respectful in discussions

See `CONTRIBUTING.md` for full details.

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 AIForge Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙌 Acknowledgements

- **MiniMax** – For providing the powerful LLM API
- **OpenAI** – For alternative model support
- **Blender Foundation** – For the incredible 3D platform
- **Community Contributors** – For testing, feedback, and code contributions

---

## 📞 Support

Need help? Reach out through these channels:

| Channel | Link |
|---------|------|
| 💬 Discord | [Join our community](https://discord.gg/dXAN23NwkM) |
| 🌐 Website | [aiforge3d.com](https://aiforge3d.com) |
| 🐛 Issues | [GitHub Issues](https://github.com/aiforge3d/blender-addon/issues) |
| 📧 Email | support@aiforge3d.com |

---

<p align="center">
  <strong>Made with ❤️ by the AIForge Team</strong>
</p>

<p align="center">
  <a href="#aiforge-3d--aipowered-blender-assistant">⬆️ Back to Top</a>
</p>
