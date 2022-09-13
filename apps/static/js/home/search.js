$( function() {
  $("input").keypress(function(){});
  $( "#id_search" ).autocomplete({
    source: '/search/'
  });
} );
$( function() {
  $("input").keypress(function(){});
  $( "#id_location" ).autocomplete({
    source: '/search/'
  });
} );