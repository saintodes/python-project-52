from django.utils.translation import gettext

FLASH_MESSAGES_TEXT = {
    "login_success": gettext('You are logged in'),
    'logout_success': gettext('You are logged out'),
    'status_update_success': gettext('Status changed successfully'),
    'status_delete_success': gettext('Status deleted successfully'),
    'change_user_data_auth_failed': gettext('You do not have permission to change another user.'),
    'change_task_data_auth_failed': gettext('Only the author can delete the task'),
    'used_status_delete_failed': gettext("It's impossible to delete the status because it's being used."),
    'label_update_success': gettext('Label updated successfully'),
    'used_label_delete_failed': gettext("It's impossible to delete the label because it's being used."),
    'task_update_success': gettext('Task updated successfully'),
    'label_delete_success': gettext('Label deleted successfully'),
    'task_delete_success': gettext('Task deleted successfully'),
}
