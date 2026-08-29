from bpy.props import StringProperty

from ..helpers.btypes import BOperator
from ..helpers.prefs import get_prefs
from ..helpers.process import format_traceback
from .op_report_message import report_message


@BOperator("asset_bridge")
class AB_OT_set_lib_path(BOperator.type):
    """Browse for the folder to use as the downloads path"""

    directory: StringProperty(subtype="DIR_PATH", options={"HIDDEN"})

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}

    def execute(self, context):
        try:
            get_prefs(context).lib_path = self.directory
        except Exception as e:
            tb = format_traceback(e)
            print(tb)
            report_message("ERROR", message=tb)
        return {"FINISHED"}
