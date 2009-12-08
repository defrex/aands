

var aands = new Object()

aands.pretty_select = function(select, change_clbk){
    var new_select_id = '';
    for (i=0; i<32; i++) new_select_id += Math.floor(Math.random() * 16).toString(16);
    var select_name = select.attr('name');
    var value = select.children('option:selected').val() || '';
    var new_select = '<input type="hidden" name="'+select_name+'" value="'+value+'" />';
    new_select += '<ul class="ui pretty_select" id="'+new_select_id+'">';
    select.children('option').each(function(){
        new_select += '<li op_val="'+$(this).attr('value')+'"';
        if ($(this).attr('selected') == true)
            new_select += ' class="selected"';
        new_select += '>'+$(this).text()+'</li>';
    });
    new_select += '</ul>';
    select.hide().after(new_select).remove();
    $('#'+new_select_id+' li').click(function(){
        $('#'+new_select_id+' li').removeClass('selected');
        $(this).addClass('selected');
        $('input[name="'+select_name+'"]').val($(this).attr('op_val'));
        if (typeof(change_clbk) == 'function')
            change_clbk($('input[name="'+select_name+'"]'));
    });
};




