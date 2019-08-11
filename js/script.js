$(document).ready(function(){
$("#auto").autocomplete({
    source: "{{url_for('autocomplete')}}",
    minLength: 1
    });
});