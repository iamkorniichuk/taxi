forbiddEmptyFieldsToSend();

function forbiddEmptyFieldsToSend(method='get'){
    $(`form[method='${method}']`).each(function(i) {
        let $form = $(this);
        $form.submit(function () {
            $(this).find('input[name], textarea').filter(function () {
                return !this.value;
            }).prop('name', '');
        });
    });
}