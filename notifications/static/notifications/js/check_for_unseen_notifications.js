(function callAjax() {
	$.ajax({
	    url: $('#check_for_unseen_notifications_script').attr('url'),
	    dataType: 'json',
	    success: data => {
	    	if(data.number_of_unseen_notifications > 0) showNumberOfNotifications(data.number_of_unseen_notifications);

	    	setTimeout(function() {callAjax();}, 30000);
	    }
	})
})()

function showNumberOfNotifications(notifications_counter) {
	// notifications_count_element = $('#navbar_button_notifications span');
	notifications_counter_element = $('#notifications_counter');
	
	if(notifications_counter >= 10) notifications_counter_element.addClass('double_digit');
	else notifications_counter_element.addClass('single_digit');

	notifications_counter_element.css('display', 'inline');
	notifications_counter_element.text(notifications_counter);

	$('#navbar_button_notifications .fa-square').css('display', 'inline');
}

