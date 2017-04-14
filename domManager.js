
		function showForm_onclick() 
		{ 
			$('#new').click(function(){
			$(this).val('Add');
			$('#cancel').show();
			$('#form1').show();
			}
			)

		} 
		function hideForm_onclick() 
		{ 
			$('#cancel').click(function(){
			$(this).hide();
			$('#new').val('New');
			$('#form1').hide();
			}
			)
		}
		$(document).ready (function(){
		$('#SEARCH').click(function(){getAppointments(data));
		}
});		
		function getAppointments(data) {$.ajax({
			url: 'cgi_task.cgi', 
			type: "get",
			data: JSON.stringify(data),
				success:function(data) {
				$.each(data, (function(i, item)
					{
				var $tr = $('<tr>').append(
					$('<td>').text(item.date),
					$('<td>').text(item.time),
					$('<td>').text(item.description));
					});
				})
				fail:function (data) {$('#error').val(data.message);}
				}
					
				)
			}
		$(document).ready (function(){
			if ($('#new').val() == 'ADD'){
		$('#new').click(function(){addAppointment(data));
		}
		}
});		
		function addAppointment(data) {$.ajax({
			url: 'cgi_task.cgi', 
			type: "post",
			data: JSON.stringify(data),
				#reload the page when form is submitted
				success: function(){location.reload();
				}
				#display error message if input is invalid
				fail:function (data) {$('#error').val(data);}
				}
					
				)
			}
