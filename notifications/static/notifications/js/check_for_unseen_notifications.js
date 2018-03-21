(function callAjax() {
	$.ajax({
	    url: $('#check_for_unseen_notifications_script').attr('url'),
	    dataType: 'json',
	    success: data => {
	    	notifications_count = data.number_of_unseen_notifications
	    	
	    	if(notifications_count > 0) showNumberOfNotifications(notifications_count);

	    	setTimeout(function() {callAjax();}, 30000)
	    }
	})
})()

function showNumberOfNotifications(notifications_count) {
	notifications_count_element = $('#navbar_button_notifications span');
	
	if(notifications_count >= 10) notifications_count_element.addClass('double_digit')
	else notifications_count_element.addClass('single_digit')

	notifications_count_element.css('display', 'inline')
	notifications_count_element.text(notifications_count)

	$('#navbar_button_notifications .fa-square').css('display', 'inline');
}

