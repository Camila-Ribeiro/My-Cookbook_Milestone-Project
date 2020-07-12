$(document).ready(function(){
    var scriptElement = $('#baseScript')[0];
    var path = scriptElement.getAttribute('data-path');

    $('select').selectpicker();
    
    $('a[href="'+path+'"]').addClass("active");
    $('.center').slick({
        centerMode: true,
        // centerPadding: '100px',
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


    var api_key = '7b98ae9af6fe4cc6b9a33b00e08db54d';
    var api_url = '';
    var imageUrl = "https://spoonacular.com/recipeImages/";
    $('.select_list').on('change', function() {
        var value = $(this).val();

        $.ajax({
            method: "GET",
            url: 'https://api.spoonacular.com/recipes/search?diet='+value+'&apiKey='+api_key+'',
            contentType: "application/json",
            dataType: 'json',
            success: function(obj){;
                $("#title-results").html(value);
                $.each( obj.results, function( index, cat ){
                   // $("#results .results").empty();
                   let apiUrl = cat.id;
                //    let urlLink = "$.post(Flask.url_for('recipe_details', recipe_id='"+apiUrl+"'))";
                    $( "#results .results" ).after(
                        "<div class='col-md-3'> \n " +
                            "<div class='card'> \n " +
                                "<img src="+imageUrl+cat.image+" class='on-inview' alt="+cat.title+" /> \n " +
                                "<div class='card-body'> \n " +
                                    "<a href='"+ 
                                    Flask.url_for("recipe_details", "recipe_id="+apiUrl) +" class='title-padding'>"+cat.title+"</a>  \n " +
                                "</div> \n " +
                            "</div> \n " +
                        "</div>" 
                    );
                });
                $("html,body").animate({scrollTop:$("#title-results").offset().top}, 500);
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
                        <input type="text" class="form-control mt-2" name="add_ingredients" placeholder="add ingredient" aria-describedby="ingredients" />
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
                        <input type="text" class="form-control mt-2" name="add_instructions" placeholder="add instruction" aria-describedby="add_instructions" />
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

