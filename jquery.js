// Run all the jquery code once the document is ready to be used.
$(document).ready(function () {
  console.log("I am in Jquey Section:");

  // Following action should be taken place when the click on p happens.
  // An example of Element selector function.
  $("p").click(function () {
    // Following id holder variable may get hidden once the click is made on it.
    // An example of ID selector.
    $("#this").hide();

    // Other selectors of elements.
    //   $('p.this').click();
    //   $('p:first').click();
  });

  //Events of the Jquery
  //   $("p").dblclick(function () {
  //     console.log("You double clicked on the paragraph", this);
  //   });

  //   $("p").mouseenter(function () {
  //     console.log("Your mouse Has Entered: ", this);
  //   });

  //   $("p").hover(
  //     function () {
  //       console.log("You hovered: ", this);
  //     },
  //     function () {
  //       console.log("Thanks for coming into it:", this);
  //     }
  //   );

  $("p").on({
    click: function () {
      console.log("Thanks for clicking me:", this);
    },
    mouseleave: function () {
      console.log("Thanks for mouse leaving:", this);
    },
  });

  // // Function to toggle the things either to show or to hide
  // $('#butt').click(function(){
  //   $('#wikipedia').toggle(1000, function(){
  //     console.log('The work has been done:', this)
  //   })

  // $('wiikipedia').slideToggle(1000);
  // });

  // Animate Function - Arguments
  $("#butt").click(function () {
    // Animate Function being done on the id weki.
    $("#wikipedia").animate(
      {
        height: "239px",
        width: "233px",
        opacity: 0.1,
      },
      "slow"
    );
  });

  // Functions to queue the things.`
  $("#wikipedia").animate({ opacity: 0.9 }, 1000);
  $("#wikipedia").animate({ opacity: 1.2 }, 2000);
  $("#wikipedia").animate({ height: "240px" }, 2000);

  // Stop the animation or anything in the back-end
  $("#wikipedia").stop();

  // Taking out the text from the HTML
  // $('#wikipedia').text();
  // Getting the text changed.
  // $('#wikipedia').text('This is me Sharjeel');

  // Setting the inner HTMl and taking off the HTML
  // $('body').html('This is me Sharjeel');

  // Taking the HTML
  $("body").html();

  // Setting up the method to change the text of the HTML.
  $("#wikipedia").text("This is me Shrjeel Ashraf");

  // Setting up the method to get the values of forms fields.
  $("#int").val("Please write your Text Here!");
  $("#txt").val("Please write your Text!");

  // AJAX Function
  // $.get("https://code.jquery.com/jquery-3.7.1.js", function (data, status) {
  //   alert(status);
  // });

  // $.get("https://code.jquery.com/jquery-3.7.1.js", function (data, status) {
  //   alert(data);
  // });

  // AJAX using J-Query for post request.
  $.post(
    "https://code.jquery.com/jquery-3.7.1.js",
    { name: "sharjeel", channel: "sharjeel coding" },
    function (data, status) {
      alert(status);
    }
  );
});

// console.log("I am in a new file");
// Exercise too be completed
// Fadein(), fadeout(), fadetoggle(), fadeTo()
