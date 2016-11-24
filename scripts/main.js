$(document).ready(function () {
    $("#searchInput").on('change', function () {
        var body = $("#fbody")
        var rows = body.find("tr").hide();
        var hiddenCell = $('.tools-table-hidden')
        if (this.value !== 'all') {
            rows.filter(":contains('" + this.value + "')").show();
            hiddenCell.css('display', 'table-cell')
            body.find('.rowspan').attr('rowspan', '1')
        } else {
            rows.show();
        }
    });
})
