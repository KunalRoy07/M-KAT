odoo.define('sales_inherit.sales_js', function (require) {
"use strict";
var ajax = require('web.ajax');

    $(document).ready(function () {
    $("#end_date").on("input",function (){
           var startDate = $("#start_date").val();
           var endDate = $("#end_date").val();
           if (!startDate) {
           $("#demo1").show();
//                alert("Please fill in the start date first.");
//                $("#end_date").val(""); // Clear the end date input
            }
            else if (startDate > endDate) {
//                alert("End date cannot be earlier than the start date.");
                $("#demo2").show();
            }
        });
        $("#filter_button").on("click", function () {
            console.log("Filter button clicked");

            var startDate = $("#start_date").val();
            var endDate = $("#end_date").val();

            ajax.jsonRpc('/quotation_data_json/', 'call', {'start_date': startDate, 'end_date': endDate}).then(function (response) {
                console.log("Received response:", response);
                 try {
                    var data = JSON.parse(response.response_data);
                    if (data && Array.isArray(data)) {
                        console.log("Data received and parsed:", data);

                        $("#myTable tbody").empty();

                        $.each(data, function (index, quotation) {
                            console.log("Appending row:", quotation);

                            var newRow = $("<tr>");
                            newRow.append("<td>" + quotation.name + "</td>");
                            newRow.append("<td>" + quotation.date_order + "</td>");
                            newRow.append("<td>" + quotation.partner_id + "</td>");
                            newRow.append("<td>" + quotation.user_id + "</td>");
                            newRow.append("<td>" + quotation.amount_total + "</td>");
                            newRow.append("<td>" + quotation.state + "</td>");
                            newRow.append("<td>" + quotation.invoice_status + "</td>");

                            $("#myTable tbody").append(newRow);
                        });
                    } else {
                        console.log('No data found in the response or data is not an array.');
                    }

                } catch (error) {
                    console.error('Error parsing JSON response:', error);
                }
            }).catch(function (error) {
                console.error('Error in AJAX request:', error);


                });
            });


        });

});

