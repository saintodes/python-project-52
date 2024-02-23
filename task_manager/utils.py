from django.utils.translation import gettext

FLASH_MESSAGES_TEXT = {
    "login_success": gettext('You are logged in'),
    'logout_success': gettext('You are logged out'),
    'status_update_success': gettext('Status changed successfully'),
    'status_delete_success': gettext('Status deleted successfully'),
    'change_user_data_auth_failed': gettext('You do not have permission to change another user.')
}
