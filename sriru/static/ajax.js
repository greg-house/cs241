$(function(){
	$('#search').keyup(function(){

/*		$.ajax({
			type: "POST",
			url: "/sriru/search/",
			data: {
//				'search_text' : $('#search').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
			},
			success: 'searchSuccess',
			dataType: 'html',
		});
*/		
		var p = $('#search').val();
		if( p != '' ) {
			var a = '/sriru/search/'+ p;
			$.get( a, function(data) {
				$('#search-result').html(data);
			});
		} else {
			$('#search-result').html('');
		}

	});
});
