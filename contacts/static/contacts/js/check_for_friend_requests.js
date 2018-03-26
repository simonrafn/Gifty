(function callAjax() {
	$.ajax({
		url: $('#check_for_friend_requests_script').attr('url'),
		dataType: 'json',
		success: data => {
			if(data.number_of_friend_requests > 0) showNewFriendRequestIcon(data.number_of_friend_requests);

			setTimeout(function() {callAjax();}, 30000);
		}
	})
})()

function showNewFriendRequestIcon(friend_requests_counter) {
	friend_requests_counter_element = $('#friend_requests_counter');

	if(friend_requests_counter >= 10) friend_requests_counter_element.addClass('double_digit');
	else friend_requests_counter_element.addClass('single_digit');

	friend_requests_counter_element.css('display', 'inline');
	friend_requests_counter_element.text(friend_requests_counter);

	$('#navbar_button_contacts .fa-square').css('display', 'inline');
}