$(document).ready(function(){
    var scriptElement = $('#baseScript')[0];
    var path = scriptElement.getAttribute('data-path');
    $('a[href="'+path+'"]').addClass("active");

    $('select').selectpicker();
    $('[data-toggle="tooltip"]').tooltip()
      
    $('.center').slick({
        centerMode: true,
        slidesToShow: 3,
        responsive: [
            {
            breakpoint: 768,
            settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 3
            }
            },
            {
            breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '40px',
                    slidesToShow: 1
                }
            }
        ]
    });

    var api_key = scriptElement.getAttribute('data-api');
    var imageUrl = "https://spoonacular.com/recipeImages/";
    $(".select_list").on('change', function() {
        var value = $(this).val();
        
        $.ajax({
            method: "GET",
            beforeSend: function(){
                $('#loading').addClass("loading");
            },
            url: 'https://api.spoonacular.com/recipes/search?diet='+value+'&apiKey='+api_key+'',
            contentType: "application/json",
            dataType: 'json',
            success: function(obj){
                $.each( obj.results, function( index, cat ){
                    $("#title_results").html(value);
                    var apiUrl = cat.id;
                    var go = "recipe_details/"+apiUrl+" ";

                    $( "#results .results" ).after(
                        "<div class='col-md-4 mb-5'> \n " +
                            "<div class='card'> \n " +
                                "<img src="+imageUrl+cat.image+" class='on-inview' alt="+cat.title+" /> \n " +
                                "<div class='card-body'> \n " +
                                     "<a href="+go+" class='title-padding'>"+cat.title+"</a>  \n " +
                                "</div> \n " +
                            "</div> \n " +
                        "</div>" 
                    );
                });
            },
            complete: function(){
                $('#loading').removeClass("loading");
                $("html,body").animate({scrollTop:$("#title_results").offset().top}, 500);
            }
        })
    });

    // ADD INPUT INGREDIENTS
    $(".add_ingredients").click(function(){
        add_Ingredient();
        return false;
    });

    function add_Ingredient() {
        var add_div = `<div class= "added-input-ingredients">
                        <input type="text" class="form-control mt-2" name="add_ingredients" placeholder="add ingredient" minlength="1" aria-describedby="ingredients" required/>
                            <span>
                                <i class="icofont-close-circled d-inline"></i>
                            </span>
                        </div>`;
        $(add_div).insertBefore('.add-more-ingredients');
    }

    // REMOVE INGREDIENTS AND DELETE INPUT
    $('.ingredients').on('click', 'span', function () {
        var remove_ingredientes = $(this).closest('div.added-input-ingredients');
        $(remove_ingredientes).remove();
    });

    // ADD INPUT INSTRUCTIONS
    $(".add_instruction").click(function(){
        add_Instruction();
        return false;
    });

    function add_Instruction() {
        var add_div = `<div class= "added-input-instructions">
                        <input type="text" class="form-control mt-2" name="add_instructions" placeholder="add instruction" minlength="1" aria-describedby="add_instructions" required/>
                            <span>
                                <i class="icofont-close-circled d-inline"></i>
                            </span>
                        </div>`;
        $(add_div).insertBefore('.add-more-instructions');
    }

    // REMOVE INSTRUCTIONS AND DELETE INPUT
    $('.instructions').on('click', 'span', function () {
        var remove_instructions = $(this).closest('div.added-input-instructions');
        $(remove_instructions).remove();
    });

});//.doc.ready

