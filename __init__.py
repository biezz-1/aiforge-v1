"""
AIForge 3D - AI-powered Blender Assistant
Powered by MiniMax AI
"""

bl_info = {
    "name": "AIForge 3D",
    "author": "AIForge",
    "version": (1, 3, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > AIForge 3D",
    "description": "AI-powered Blender assistant powered by MiniMax AI",
    "warning": "",
    "doc_url": "https://aiforge3d.com",
    "category": "Development",
}

import bpy
from bpy.app.handlers import persistent
import importlib
import time

# Module reloading for Blender
from . import api
from . import auth
from . import tools
from . import llm
from . import operators
from . import ui
from . import utils

if "bpy" in locals():
    importlib.reload(api)
    importlib.reload(auth)
    importlib.reload(tools)
    importlib.reload(llm)
    importlib.reload(operators)
    importlib.reload(ui)
    importlib.reload(utils)

from .auth.manager import auth_manager
from .utils.instructions_manager import instruction_manager
from .utils.logger import logger

# Build timestamp for verification
BUILD_TIME = "2026-01-10 00:00:00" # Cognitive Memory & Planning Update

from .utils.settings_manager import settings_manager

# Public API
query = tools.query_scene
execute = tools.execute_code
scene_context = tools.get_scene_context
viewport = tools.viewport
screenshot = tools.screenshot
screenshot_viewport = tools.screenshot_viewport
screenshot_object = tools.screenshot_object


@persistent
def load_auth_and_settings_on_file_load(file):
    try:
        if bpy.context.scene:
            is_authenticated = getattr(bpy.context.window_manager, 'vibe4d_authenticated', False)
            if not is_authenticated:
                auth_manager.initialize_auth(bpy.context)

            settings_manager.initialize_settings(bpy.context)
            instruction_manager.initialize_instruction(bpy.context)
    except Exception as e:
        logger.debug(f"Failed to load auth/settings/instructions on file load: {str(e)}")


@persistent
def recover_ui_overlay_on_file_load(file):

    def delayed_recovery():
        try:
            from .ui.manager import ui_manager
            from .ui.ui_state_manager import ui_state_manager

            recovery_success = ui_state_manager.recover_ui_state(bpy.context, ui_manager)
            if not recovery_success:
                logger.debug("No UI state to recover or recovery not needed")

        except Exception as e:
            logger.error(f"Error in UI recovery: {e}")
            import traceback
            logger.error(traceback.format_exc())

        return None

    try:
        bpy.app.timers.register(delayed_recovery, first_interval=0.1)
    except Exception as e:
        logger.error(f"Failed to schedule UI recovery: {e}")


@persistent
def ensure_viewport_button_handler(file):
    """Ensure viewport button modal handler is running after file load."""

    def delayed_handler_check():
        """Check and start viewport button handler if needed."""
        try:
            if hasattr(bpy.context, 'window_manager') and bpy.context.window_manager:
                try:
                    bpy.ops.vibe4d.viewport_button_handler('INVOKE_DEFAULT')
                    logger.debug("Viewport button modal handler started after file load")
                except RuntimeError as e:
                    if "already running" in str(e).lower():
                        logger.debug("Viewport button modal handler already running")
                    else:
                        logger.warning(f"Failed to start viewport button modal handler: {e}")
        except Exception as e:
            logger.debug(f"Error checking viewport button handler: {e}")
        return None

    try:
        bpy.app.timers.register(delayed_handler_check, first_interval=0.2)
    except Exception as e:
        logger.debug(f"Failed to schedule viewport button handler check: {e}")


@persistent
def auto_open_chat_ui_on_file_load(file):
    """Automatically open the chat UI when a new scene is loaded."""
    if file:
        logger.debug(f"Skipping auto-open for existing file: {file}")
        return

    def delayed_ui_open():
        """Delayed UI opening function to ensure scene is fully loaded."""
        try:
            from .ui.manager import ui_manager

            if ui_manager.is_ui_active():
                logger.debug("Chat UI already active, skipping auto-open")
                return None

            MIN_VIEWPORT_WIDTH = 800
            MIN_VIEWPORT_HEIGHT = 600
            target_area = None
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D' and area.width > MIN_VIEWPORT_WIDTH and area.height > MIN_VIEWPORT_HEIGHT:
                    target_area = area
                    break

            if not target_area:
                logger.debug("No suitable 3D viewport found for auto-opening chat UI")
                return None

            try:
                with bpy.context.temp_override(area=target_area):
                    bpy.ops.vibe4d.show_advanced_ui()
            except Exception as e:
                logger.error(f"Failed to auto-open chat UI using operator: {e}")

        except Exception as e:
            logger.error(f"Error in auto-open chat UI handler: {e}")
            import traceback
            logger.error(traceback.format_exc())

        return None

    try:
        bpy.app.timers.register(delayed_ui_open, first_interval=0.1)
    except Exception as e:
        logger.error(f"Failed to schedule auto-open chat UI: {e}")


def register():
    """Register the addon."""
    print(f"\n[AIForge 3D] REGISTERING VERSION {bl_info['version']} (BUILD: {BUILD_TIME})")
    try:
        logger.info(f"=== Registering AIForge 3D Addon v{'.'.join(map(str, bl_info['version']))} ===")

        ui.register()
        operators.register()
        auth.register()
        api.register()
        llm.register()
        tools.register()
        utils.register()

        if load_auth_and_settings_on_file_load not in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.append(load_auth_and_settings_on_file_load)

        if recover_ui_overlay_on_file_load not in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.append(recover_ui_overlay_on_file_load)

        if ensure_viewport_button_handler not in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.append(ensure_viewport_button_handler)

        if auto_open_chat_ui_on_file_load not in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.append(auto_open_chat_ui_on_file_load)

        def delayed_modal_handler_start():
            try:
                if hasattr(bpy.context, 'window_manager') and bpy.context.window_manager:
                    bpy.ops.vibe4d.viewport_button_handler('INVOKE_DEFAULT')
                else:
                    logger.warning("Context not ready for modal handler, will retry on file load")
            except Exception as e:
                logger.warning(f"Failed to start viewport button modal handler: {e}")
            return None

        try:
            bpy.app.timers.register(delayed_modal_handler_start, first_interval=0.2)
        except Exception as e:
            logger.warning(f"Failed to schedule viewport button modal handler: {e}")

        try:
            if bpy.context.scene:
                auth_manager.initialize_auth(bpy.context)
                settings_manager.initialize_settings(bpy.context)
                instruction_manager.initialize_instruction(bpy.context)
        except Exception as e:
            logger.debug(f"Failed to load initial auth/settings/instructions: {str(e)}")

        logger.info("AIForge 3D addon registered successfully")

    except Exception as e:
        logger.error(f"Failed to register AIForge 3D addon: {str(e)}")
        raise


def unregister():
    """Unregister the addon."""
    try:
        logger.info("=== Unregistering AIForge 3D Addon ===")

        try:
            if bpy.context.scene:
                settings_manager.save_settings(bpy.context)
                instruction_manager.save_instruction(bpy.context)
        except Exception as e:
            logger.debug(f"Failed to save settings/instructions on unregister: {str(e)}")

        if load_auth_and_settings_on_file_load in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.remove(load_auth_and_settings_on_file_load)
        if recover_ui_overlay_on_file_load in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.remove(recover_ui_overlay_on_file_load)
        if ensure_viewport_button_handler in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.remove(ensure_viewport_button_handler)
        if auto_open_chat_ui_on_file_load in bpy.app.handlers.load_post:
            bpy.app.handlers.load_post.remove(auto_open_chat_ui_on_file_load)

        utils.unregister()
        tools.unregister()
        llm.unregister()
        api.unregister()
        auth.unregister()
        operators.unregister()
        ui.unregister()

        logger.info("AIForge 3D addon unregistered successfully")

    except Exception as e:
        logger.error(f"Failed to unregister AIForge 3D addon: {str(e)}")


if __name__ == "__main__":
    register()
