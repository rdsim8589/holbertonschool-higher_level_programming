let button = 'DIV#add_item';
$(button).click(function () {
    $('UL.my_list').append('<LI>Item</LI>');
});
