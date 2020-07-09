$(document).ready(function(){
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
    $('.select-list').on('change', function() {
        var value = $(this).val();
        //console.log(value);

        $.ajax({
            url: 'https://api.spoonacular.com/recipes/search?diet='+value+'&apiKey='+api_key+'',
            contentType: "application/json",
            dataType: 'json',
            success: function(obj){
                //console.log(obj.baseUri);
                $("#title-results").html(value);
                //console.log(obj.results[0]);
                $.each( obj.results, function( index, cat ){
                    //console.log(cat, index)
                    $("#results .results").empty();
                    
                     $( "#results .results" ).after(
                        '<a href="' + cat.sourceUrl + '"> \n ' +
                        '<div class="link-preview"> \n ' +
                            '<div class="preview-image" style="background-image:url('+imageUrl+cat.image+');display: block; width: 100%; height: 200px; position: relative; background-repeat: no-repeat; background-size: contain;"></div> \n ' +
                            '<div style="width:70%;" class="link-info"> \n ' +
                            '<h4>' + cat.title +'</h4> \n ' +
                            '<p>' + cat.servings +'</p> \n ' +
                            '</div><br> \n ' +
                            '<a href="' + cat.sourceUrl + '" class="url-info"><i class="far fa-link"></i>' + cat.sourceUrl + '</a> \n ' +
                            '</div></a>'
                        );
                });
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
                        <input type="text" class="form-control mt-2" id="add_ingredients" name="recipe_ingredient" placeholder="" aria-describedby="ingredients" />
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
                        <input type="text" class="form-control mt-2" id="add_instructions" name="recipe_instruction" placeholder="" aria-describedby="instructions" />
                            <span>
                                <i class="icofont-close-circled d-inline"></i>
                            </span>
                        </div>`;
        $(add_div).insertBefore('.add-more-instructions');
    }

    // REMOVE INSTRUCTIONS AND DELETE INPUT
    $('.instructions').on('click', 'span', function () {
        console.log('click')
        var remove_instructions = $(this).closest('div.added-input-instructions');
        $(remove_instructions).remove();
    });
});