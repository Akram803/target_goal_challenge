$(document).ready(function(){

    $.ajax({
        type: "get",
        url: "http://127.0.0.1:8000/static/data.json",
        data: "data",
        dataType: "json",
        success: function (response) {
            create_table(response.Targets)
        }
    });



});



function create_table(targets) {

    targets.forEach(target => {

        tr = $("<tr></tr>").append(
                    $("<td></td>").addClass("text-left").css("max-width", "10px").text(target.name)
                )

        target.this_week.forEach(value => {
            tr.append(
                $("<td></td>").text(value)
                )
        });

        tr.append(
            $("<td></td>").text( target.this_week.reduce((a, b) => a + b, 0) + "%")
            // 
        )

        $("tbody").append(tr);

    });
    
}



        
