from django.utils.translation import gettext
FLASH_MESSAGES_TEXT = {
    "login_success": gettext('You are logged in'),
    'logout_success': gettext('You are logged out'),
    'change_user_data_auth_failed': gettext('You do not have permission to change another user.'),
    'change_user_data_success': gettext('The user has been successfully modified'),
    'delete_user_success': gettext('The user has been successfully deleted'),
    'user_register_success': gettext('The user has been successfully registered'),
    'status_update_success': gettext('The status has been successfully updated'),
    'status_create_success': gettext('The status has been successfully created'),
    'status_delete_success': gettext('The status has been successfully deleted'),
    'change_task_data_auth_failed': gettext('Only the author can delete the task'),
    'used_status_delete_failed': gettext("It's impossible to delete the status because it's being used."),
    'used_label_delete_failed': gettext("It's impossible to delete the label because it's being used."),
    'label_create_success': gettext('The label has been successfully created'),
    'label_update_success': gettext('The label has been successfully updated'),
    'label_delete_success': gettext('The label has been successfully deleted'),
    'task_create_success': gettext('The task has been successfully created'),
    'task_update_success': gettext('The task has been successfully updated'),
    'task_delete_success': gettext('The task has been successfully deleted'),
}

